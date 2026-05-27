# Secure AI Gateway

A self-hosted **AI Security Gateway** built to intercept, inspect, and govern prompts before they reach a local LLM — combining Keycloak authentication, role-based access control, threat detection, and a SOC-style monitoring dashboard. Deployed on an Oracle Cloud Ubuntu VM.

---

## Overview

The Secure AI Gateway sits between users and a locally hosted LLM (TinyLlama via Ollama). Every prompt passes through a security filter that scores its risk, blocks malicious inputs, and logs all activity — giving full visibility into AI usage and threats through a role-specific Streamlit dashboard.

```
User Prompt
    ↓
Keycloak Authentication (JWT / RS256)
    ↓
RBAC Authorization (admin / analyst / user)
    ↓
Prompt Injection Detection + Risk Scoring
    ↓
[ BLOCKED ] ──→ Audit Log
    ↓ (if allowed)
Ollama / TinyLlama Inference
    ↓
Response + Audit Log
```

---

## Features

- **JWT Authentication** via Keycloak IAM — no anonymous access
- **Role-Based Access Control (RBAC)** — `admin`, `analyst`, `user` roles with different permissions at both API and UI level
- **Prompt Injection Detection** — pattern matching against known attack phrases with weighted risk scoring
- **Severity Classification** — `LOW` / `MEDIUM` / `HIGH` / `CRITICAL` risk levels
- **Secure LLM Inference** — only clean prompts reach TinyLlama via Ollama
- **Full Audit Logging** — every request (allowed or blocked) persisted to database with timestamp, user, prompt, severity, and detected patterns
- **SOC-style Dashboard** — Streamlit frontend with metrics, charts, audit tables, and role-specific views
- **Cloud Hosted** — deployed on an Oracle Cloud Ubuntu VM with manually managed Linux services

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| Authentication | Keycloak (IAM) + JWT (RS256) |
| Authorization | Realm Roles via RBAC |
| AI Inference | Ollama + TinyLlama |
| Database | SQLAlchemy (SQL) |
| Frontend Dashboard | Streamlit |
| Data Visualisation | Pandas + Matplotlib |
| Deployment | Oracle Cloud VM (Ubuntu) |
| Language | Python 3 |

---

## Project Structure

```
secure-ai-gateway/
│
├── main.py              # FastAPI backend — auth, security engine, inference, audit logging
├── dashboard.py         # Streamlit frontend — role-based dashboards and visualisations
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

## Setup & Installation

### Prerequisites

- Python 3.9+
- [Keycloak](https://www.keycloak.org/) running locally on port `8080`
- [Ollama](https://ollama.com/) running locally with TinyLlama pulled
- A SQL database (PostgreSQL or SQLite)

### 1. Set up Keycloak

- Create a realm called `secure-ai`
- Create a client called `secure-ai-gateway`
- Create realm roles: `admin`, `analyst`, `user`
- Assign roles to your users

## API Endpoints

| Method | Endpoint | Roles Allowed | Description |
|---|---|---|---|
| `GET` | `/` | Public | Health check |
| `POST` | `/chat` | admin, analyst, user | Submit prompt for secure inference |
| `GET` | `/audit` | admin, analyst | View full audit log |
| `GET` | `/blocked` | admin, analyst | View blocked prompt log |
| `GET` | `/stats` | admin, analyst | Security metrics and analytics |

### Example response — allowed

```json
{
  "success": true,
  "model": "tinyllama",
  "blocked": false,
  "risk_score": 0,
  "severity": "LOW",
  "response": "A firewall is a network security system that monitors..."
}
```

### Example response — blocked

```json
{
  "success": false,
  "blocked": true,
  "risk_score": 95,
  "severity": "CRITICAL",
  "detected_patterns": ["jailbreak"],
  "reason": "Prompt blocked due to security policy"
}
```

---

## Threat Detection Engine

Every prompt is normalised (lowercased, special characters stripped) before being matched against a weighted pattern dictionary. Scores are summed and capped at 100. Any prompt scoring **80 or above is blocked** before reaching the model.

| Pattern | Risk Score |
|---|---|
| `bypass security` | 100 |
| `system override` | 100 |
| `reveal system prompt` | 95 |
| `jailbreak` | 95 |
| `ignore previous instructions` | 90 |
| `pretend to be root` | 90 |
| `disable safety` | 85 |
| `forget previous instructions` | 80 |
| `act as administrator` | 75 |

**Severity thresholds:**

| Score Range | Severity |
|---|---|
| 80 – 100 | CRITICAL |
| 50 – 79 | HIGH |
| 20 – 49 | MEDIUM |
| 0 – 19 | LOW |

---

## Dashboard

The Streamlit dashboard authenticates directly against Keycloak and renders a different view based on the user's realm role.

### Admin Dashboard
- **Metrics row** — Total requests, allowed, blocked, critical attacks
- **Pie chart** — Allowed vs blocked request distribution
- **Bar chart** — Severity distribution across all requests
- **Bar chart** — Top 5 most active users
- **Line chart** — Request volume over time
- **Filterable audit log table** — filter by username and severity
- **Filterable blocked prompts table**

### Analyst Dashboard
- Blocked prompt log with full attack metadata

### User Dashboard
- Prompt input box with secure AI assistant interface
- Displays AI response, risk score, and severity for each submission

---

## Deployment

The platform is deployed on an **Oracle Cloud Ubuntu VM** with all services self-hosted and managed manually via Linux process management.

```bash
# Start backend
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start dashboard
nohup streamlit run dashboard.py --server.port 8501 &
```
---

## System Architecture

The platform is structured across five tiers, each with a distinct responsibility.

**Frontend (Streamlit)**
Three separate dashboard views are rendered depending on the authenticated user's Keycloak realm role — admin, analyst, or user. All three views authenticate against the same Keycloak instance before any data is displayed.

**Auth (Keycloak)**
Keycloak issues a signed JWT (RS256) on successful login. That token is passed as a bearer header on every subsequent API call. The FastAPI backend fetches Keycloak's public JWKS to verify the token signature and extracts the user's realm roles from the payload.

**Backend (FastAPI)**
After token verification, the backend enforces RBAC — checking that the caller's roles permit access to the requested endpoint. The user's prompt is then passed to the threat detection engine, which normalises the text and matches it against a weighted pattern dictionary. Any prompt scoring 80 or above is blocked immediately and written to the audit log. Clean prompts continue to inference.

**Inference (Ollama + TinyLlama)**
Prompts that pass the security filter are forwarded to a locally running Ollama instance on port 11434. TinyLlama generates a response, which is trimmed and returned to the caller along with the risk score and severity level.

**Storage (SQLAlchemy)**
Every request — whether blocked or allowed — is persisted to the audit log database with a full record of timestamp, username, prompt, status, risk score, severity, and detected patterns. This table powers the `/audit`, `/blocked`, and `/stats` endpoints that feed the admin and analyst dashboards.

```
Streamlit (admin / analyst / user view)
         ↓  login
    Keycloak IAM  →  JWT (RS256)
         ↓  bearer token
    FastAPI gateway  →  RBAC check
         ↓  prompt
  Threat detection engine
    ↙ score ≥ 80        ↘ score < 80
 Blocked + logged     Ollama / TinyLlama
                           ↓  response
                      Allowed + logged
         ↓  both paths
    SQLAlchemy audit log
         ↑  /stats · /audit · /blocked
    FastAPI → Streamlit dashboards
```
