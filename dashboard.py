import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import jwt
import os
from dotenv import load_dotenv
load_dotenv()

if "TOKEN" not in st.session_state:
	st.session_state["TOKEN"] = None
if "ROLES" not in st.session_state:
	st.session_state["ROLES"] = []

st.set_page_config(page_title="Secure AI Gateway Dashboard", layout="wide")


BASE_URL = os.getenv("BASE_URL")
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
REALM = os.getenv("REALM")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if st.session_state["TOKEN"] is None:
	st.title("Secure AI Gateway")
	st.subheader("Login")
	username = st.text_input("Username")
	password = st.text_input("Password", type="password")

	if st.button("Login"):

		token_response = requests.post(
					f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token",
					headers={"Content-Type": "application/x-www-form-urlencoded"},
					data={
						"client_id": CLIENT_ID,
						"client_secret": CLIENT_SECRET,
						"username": username,
						"password": password,
						"grant_type": "password"
					}
			)

		if token_response.status_code == 200:
			access_token = token_response.json()["access_token"]
			st.session_state["TOKEN"] = access_token
			decoded_token = jwt.decode(access_token, options={"verify_signature":False})
			roles = decoded_token.get("realm_access",{}).get("roles",[])
			st.session_state["ROLES"] = roles
			st.success("Login Successful")
			st.rerun()
		else:
			st.error("Login Failed")
			st.stop()
else:
	HEADERS = {"Authorization": f"Bearer {st.session_state['TOKEN']}"}
	st.sidebar.title("Navigation")
	st.sidebar.subheader("Current Roles")
	st.sidebar.write(st.session_state["ROLES"])
	if "admin" in st.session_state["ROLES"]:
		st.title("Admin Security Dashboard")
		stats_response = requests.get(f"{BASE_URL}/stats",headers=HEADERS)
		if stats_response.status_code == 200:
			stats_data = stats_response.json()["stats"]
			col1,col2,col3,col4 = st.columns(4)
			col1.metric("Total Requests", stats_data["total_requests"])
			col2.metric("Allowed Requests", stats_data["allowed_requests"])
			col3.metric("Blocked Requests", stats_data["blocked_requests"])
			col4.metric("Critical Attacks", stats_data["critical_attacks"])
			st.divider()

			row1_col1, row1_col2 = st.columns(2)
			with row1_col1:
				st.subheader("Request Distribution")
				labels = ["Allowed","Blocked"]

				values = [stats_data["allowed_requests"], stats_data["blocked_requests"]]
				fig, ax = plt.subplots(figsize=(5,4))
				ax.pie(values,labels=labels, autopct='%1.1f%%')
				ax.set_title("Allowed vs Blocked Requests")
				plt.tight_layout()
				st.pyplot(fig)
			with row1_col2:
				st.subheader("Severity Distribution")
				severity_data = stats_data["severity_distribution"]
				severity_labels = list(severity_data.keys())
				severity_values = list(severity_data.values())

				fig2, ax2 = plt.subplots(figsize=(5,4))
				ax2.bar(severity_labels, severity_values)
				ax2.set_xlabel("Severity")
				ax2.set_ylabel("Count")
				ax2.set_title("Attack Severity Distribution")
				plt.tight_layout()
				st.pyplot(fig2)

			st.divider()
			row2_col1, row2_col2 = st.columns(2)
			with row2_col1:
				st.subheader("Top Active Users")
				top_users = [user for user in stats_data["top_users"] if user["username"] is not None]
				usernames = [user["username"] for user in top_users]
				request_counts = [user["request_count"] for user in top_users]

				fig3, ax3 = plt.subplots(figsize=(5,4))

				ax3.bar(usernames, request_counts)
				ax3.set_xlabel("Users")
				ax3.set_ylabel("Requests")
				ax3.set_title("Top Active Users")
				plt.xticks(rotation=20)
				plt.tight_layout()
				st.pyplot(fig3)

			with row2_col2:
				st.subheader("Request Timeline")
				timeline_data = stats_data["request_timeline"]
				times = [item["time"] for item in timeline_data]
				request_values = [item["requests"] for item in timeline_data]

				fig4, ax4 = plt.subplots(figsize=(5,4))
				ax4.plot(times, request_values, marker="o")

				ax4.set_xlabel("Time")
				ax4.set_ylabel("Requests")
				ax4.set_title("Requests Over Time")

				plt.xticks(rotation=45)
				plt.tight_layout()
				st.pyplot(fig4)

			st.divider()
			st.subheader("Audit Logs")
			audit_response = requests.get(f"{BASE_URL}/audit", headers=HEADERS)

			if audit_response.status_code == 200:
				audit_logs = audit_response.json()["logs"]
				with st.sidebar.expander("Filters", expanded=True):
					usernames = list(set(log["username"] for log in audit_logs if log["username"] is not None))
					selected_user = st.selectbox("Flter by Username", ["All"] + usernames)
					selected_severity = st.selectbox("Filter by Severity", ["All", "LOW", "MEDIUM", "HIGH", "CRITICAL"])
				filtered_logs = audit_logs
				if selected_user != "All":
					filtered_logs = [log for log in filtered_logs if log["username"] == selected_user]
				if selected_severity != "All":
					filtered_logs = [log for log in filtered_logs if log["severity"] == selected_severity]
				audit_df = pd.DataFrame(filtered_logs)
				st.dataframe(audit_df,width="stretch")
			else:
				st.error("Failed to load audit logs")

			st.divider()
			st.subheader("Blocked Prompt Attacks")

			blocked_response = requests.get(f"{BASE_URL}/blocked", headers=HEADERS)

			if blocked_response.status_code == 200:
				blocked_logs = blocked_response.json()["blocked_logs"]
				if selected_user != "All":
					blocked_logs = [log for log in blocked_logs if log["username"] == selected_user]
				if selected_severity != "All":
					blocked_logs = [log for log in blocked_logs if log["severity"] == selected_severity]
				blocked_df = pd.DataFrame(blocked_logs)
				st.dataframe(blocked_df,width="stretch")
			else:
				st.error("Failed to load blocked logs")

	elif "analyst" in st.session_state["ROLES"]:
		st.title("Analyst Security Dashboard")
		st.subheader("Blocked Prompt Attacks")
		blocked_response = requests.get(f"{BASE_URL}/blocked",headers=HEADERS)
		if blocked_response.status_code == 200:
			blocked_logs = blocked_response.json()["blocked_logs"]
			blocked_df = pd.DataFrame(blocked_logs)
			st.dataframe(blocked_df,width="stretch")

	elif "user" in st.session_state["ROLES"]:
		st.title("Secure AI Assistant")
		user_prompt = st.text_area("Enter Prompt")
		if st.button("Send"):
			response = requests.post(
					f"{BASE_URL}/chat",
					headers={
						"Authorization": f"Bearer {st.session_state['TOKEN']}"
						},
					json={
						"prompt": user_prompt
					}
				)
			if response.status_code == 200:
				data = response.json()
				if data["blocked"]:
					st.error("Prompt Blocked")
					st.write(data)
				else:
					st.success("Response Generated")
					st.write(data["response"])
					st.write(f"Severity: {data['severity']}")
					st.write(f"Risk Score: {data['risk_score']}")
			else:
				st.error(f"Request Failed")
	else:
		st.error("Access Denied: No valid role assigned")

	if st.sidebar.button("Logout"):
		st.session_state["TOKEN"] = None
		st.session_state["ROLES"] = []
		st.rerun()
