from fastapi import FastAPI, Depends
from pydantic import BaseModel
import requests

import json
from datetime import datetime

import re

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import JWTError

from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.encoders import jsonable_encoder

from sqlalchemy import func, desc

from collections import Counter

app = FastAPI()

KEYCLOAK_URL = "http://localhost:8080/realms/secure-ai"
JWKS_URL = f"{KEYCLOAK_URL}/protocol/openid-connect/certs"
ALGORITHM = "RS256"


DATABASE_URL= "YOUR DATABASE URL"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

Base = declarative_base()

class AuditLog(Base):

	__tablename__ = "audit_logs"
	id = Column(Integer, primary_key=True, index=True)
	timestamp = Column(Text)
	username = Column(Text)
	prompt = Column(Text)
	status = Column(Text)
	risk_score = Column(Integer)
	severity = Column(Text)
	detected_patterns = Column(Text)
	model = Column(Text)

Base.metadata.create_all(bind=engine)

security = HTTPBearer()

class PromptRequest(BaseModel):
	prompt: str

risk_patterns = {
	"ignore previous instructions": 90,
	"reveal system prompt": 95,
	"bypass security": 100,
	"act as administrator": 75,
	"disable safety": 85,
	"forget previous instructions": 80,
	"jailbreak": 95,
	"pretend to be root": 90,
	"system override": 100
}

def normalize_prompt(prompt):
	prompt = prompt.lower()
	prompt = re.sub(r'[^a-zA-Z0-9\s]','',prompt)
	prompt = prompt.replace(" ","")
	return prompt

def get_severity(risk_score):
	if risk_score >=80:
		return "CRITICAL"
	elif risk_score >= 50:
		return "HIGH"
	elif risk_score >= 20:
		return "MEDIUM"
	return "LOW"


def write_log(log_data):
	db = SessionLocal()
	audit_entry = AuditLog(
		timestamp =log_data.get("timestamp"),
		username=log_data.get("username"),
		prompt=log_data.get("prompt"),
		status=log_data.get("status"),
		risk_score=log_data.get("risk_score"),
		severity=log_data.get("severity"),
		detected_patterns=str(log_data.get("detected_patterns")),
		model=log_data.get("model")
	)
	db.add(audit_entry)
	db.commit()
	db.close()


def get_public_key():
	jwks = requests.get(JWKS_URL).json()
	return jwks


def verify_token(token: str):

	try:
		jwks = get_public_key()
		unverified_header = jwt.get_unverified_header(token)
		rsa_key = {}

		for key in jwks["keys"]:
			if key["kid"] == unverified_header["kid"]:
				rsa_key = {
						"kty": key["kty"],
						"kid": key["kid"],
						"use": key["use"],
						"n": key["n"],
						"e": key["e"]
					}

		if rsa_key:
			payload = jwt.decode(
					token,
					rsa_key,
					algorithms=[ALGORITHM],
					audience="account",
					issuer=KEYCLOAK_URL
					)
			return payload

		raise JWTError("Unable to find Matching Key")
	except JWTError as e:
		raise Exception(f"Invalid token: {str(e)}")


@app.get("/")

def home():
	return{
		"message": "Secure AI Gateway is running"
	}

@app.post("/chat")

async def chat(request: PromptRequest, credentials: HTTPAuthorizationCredentials = Depends(security)):

	token = credentials.credentials
	payload =  verify_token(token)
	username = payload.get("preferred_username")
	roles = payload["realm_access"]["roles"]
	print(f"Authenticated user: {username}")
	print(f"User Roles: {roles}")

	print("TOKEN PAYLOAD:", payload)
	print("ROLES:", roles)
	allowed_roles = ["admin", "analyst", "user"]
	if not any (role in roles for role in allowed_roles):
		raise HTTPException(
			status_code=403,
			detail="Access Denied"
		)

	user_prompt = request.prompt

	normalized_prompt = normalize_prompt(user_prompt)

	timestamp = datetime.utcnow().isoformat()

	risk_score = 0

	detected_patterns = []

	for phrase, score in risk_patterns.items():

		normalized_phrase = normalize_prompt(phrase)

		if normalized_phrase in normalized_prompt:

			risk_score += score

			detected_patterns.append(phrase)

	risk_score = min(risk_score, 100)

	severity = get_severity(risk_score)

	if risk_score  >= 80:

		blocked_log = {
				"timestamp": timestamp,
				"username": username,
				"prompt": user_prompt,
				"status": "blocked",
				"risk_score": risk_score,
				"severity": severity,
				"detected_patterns": detected_patterns,
				"reason": "prompt injection detected"
				}

		write_log(blocked_log)

		return{
			"success": False,
			"blocked": True,
			"risk_score": risk_score,
			"severity": severity,
			"detected_patterns": detected_patterns,
			"reason": "Prompt blocked due to security policy"
		}
	# Ollama
	ollama_payload = {
		"model": "tinyllama",
		"prompt": user_prompt,
		"stream": False
		}

	ollama_request = requests.post(
		"http://localhost:11434/api/generate",
		json=ollama_payload
		)

	data  = ollama_request.json()

	formatted_response = data.get("response","").strip()
	formatted_response = formatted_response.replace("\n"," ")
	formatted_response = formatted_response[:500]

	allowed_log = {
		"timestamp": timestamp,
		"username": username,
		"prompt": user_prompt,
		"status": "allowed",
		"risk_score": risk_score,
		"severity": severity,
		"model": "tinyllama"
	}

	write_log(allowed_log)

	return {
	"success":True,
	"model":"tinyllama",
	"blocked":False,
	"risk_score": risk_score,
	"severity": severity,
	"response": formatted_response
	}

@app.get("/audit")
async def get_audit_logs(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
	token = credentials.credentials
	payload = verify_token(token)
	username = payload.get("preferred_username")
	roles = payload.get("realm_access", {}).get("roles", [])
	print(f"Audit API Access by: {username}")
	print(f"Roles: {roles}")

	if not any(role in roles for role in ["admin","analyst"]):
		raise HTTPException(
			status_code=403,
			detail="Access denied"
		)
	logs = db.query(AuditLog).order_by(AuditLog.id.desc()).all()

	return {
		"success": True,
		"total_logs": len(logs),
		"logs": jsonable_encoder(logs)
	}


@app.get("/blocked")
async def get_blocked_logs(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
	token = credentials.credentials
	payload = verify_token(token)
	username = payload.get("preferred_username")
	roles = payload.get("realm_access", {}).get("roles", [])
	print(f"Blocked Logs Access by: {username}")
	if not any (role in roles for role in ["admin","analyst"]):
		raise HTTPException(
		status_code=403,
		detail= "Access denied"
		)

	blocked_logs = db.query(AuditLog).filter(AuditLog.status == "blocked").order_by(AuditLog.id.desc()).all()
	return {
		"success": True,
		"blocked_count": len(blocked_logs),
		"blocked_logs": jsonable_encoder(blocked_logs)
	}


@app.get("/stats")
async def get_stats(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):

	token = credentials.credentials
	payload = verify_token(token)

	username = payload.get("preferred_username")
	roles = payload.get("realm_access", {}).get("roles", [])

	print(f"Stats API Access by: {username}")

	if "analyst" not in roles and "admin" not in roles:
		return {
		"success": False,
		"message": "Access denied"
		}

	total_requests = db.query(AuditLog).count()
	allowed_requests = db.query(AuditLog).filter(AuditLog.status == "allowed").count()

	blocked_requests = db.query(AuditLog).filter(AuditLog.status == "blocked").count()

	critical_attacks = db.query(AuditLog).filter(AuditLog.status == "CRITICAL").count()


	low_count = db.query(AuditLog).filter(AuditLog.severity == "LOW").count()
	medium_count = db.query(AuditLog).filter(AuditLog.severity == "MEDIUM").count()
	high_count = db.query(AuditLog).filter(AuditLog.severity == "HIGH").count()
	critical_count = db.query(AuditLog).filter(AuditLog.severity == "CRITICAL").count()


	top_users_query = (
			db.query(
				AuditLog.username,
				func.count(AuditLog.id).label("request_count")
				)
				.group_by(AuditLog.username)
				.order_by(desc("request_count"))
				.limit(5)
				.all()
			)


	top_users = []
	for user in top_users_query:
		top_users.append({"username": user.username, "request_count": user.request_count})


	timeline_query = (db.query(AuditLog.timestamp).order_by(AuditLog.timestamp.asc()).all())

	timestamps = [str(entry.timestamp)[11:16] for entry in timeline_query]
	timeline_counter = Counter(timestamps)
	request_timeline = []

	for time,count in timeline_counter.items():
		request_timeline.append({"time": time, "requests": count})

	return {
		"success": True,
		"stats": {
			"total_requests": total_requests,
			"allowed_requests": allowed_requests,
			"blocked_requests": blocked_requests,
			"critical_attacks": critical_attacks,
			"severity_distribution":{"LOW": low_count, "MEDIUM": medium_count, "HIGH": high_count, "CRITICAL": critical_count},
			"top_users": top_users,
			"request_timeline": request_timeline
		}
	}
