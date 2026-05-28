# Secure AI Gateway

A self-hosted **AI security gateway** that intercepts and governs every prompt before it reaches a local LLM — combining Keycloak IAM, JWT authentication, role-based access control, a threat detection engine, and a SOC-style monitoring dashboard.

> Built to solve a real problem: LLMs should never receive unvalidated input directly from users.

---

## What It Does

The gateway sits between users and a locally hosted language model (TinyLlama via Ollama). Every prompt is authenticated, authorised, scored for risk, and either blocked or forwarded to inference — with every decision logged to a database and surfaced through a role-specific dashboard.

```
User Prompt
    ↓
Keycloak Authentication  (JWT · RS256)
    ↓
RBAC Authorisation  (admin / analyst / user)
    ↓
Prompt Injection Detection + Risk Scoring
    ↓
Score ≥ 80 → BLOCKED ──→ Audit Log
Score < 80 → Ollama / TinyLlama Inference
                ↓
           Response + Audit Log
```
## Demo Videos

### Admin Dashboard

[Admin-Login-Dashboard.webm](https://github.com/user-attachments/assets/07daf403-a174-498e-b61c-0190fa674057)

Shows:

* Full SOC-style dashboard
* Metrics and visualisations
* Audit monitoring
* User activity analytics

---

### Analyst Dashboard

[Analyst-Login-Dashboard.webm](https://github.com/user-attachments/assets/7c06ed2a-8600-420f-a840-3e2bee21619e)

Shows:

* Threat monitoring workflow
* Blocked prompt visibility
* Security-focused analyst interface

---

### Allowed Prompt Flow

[Employee1-Login-Allowed-Prompt.webm](https://github.com/user-attachments/assets/c506feac-a959-4cfd-847b-1cafe513a7fc)

Shows:

* Successful authenticated inference
* Risk scoring and severity classification
* TinyLlama response generation

---

### Blocked Prompt Detection

[Employee1-Login-Blocked-Prompt-1.webm](https://github.com/user-attachments/assets/5809bcd5-ce72-462d-ad18-f08c52757c4f)

[Employee1-Login-Blocked-Prompt-2.webm](https://github.com/user-attachments/assets/adcf890a-76b5-47e6-bf61-c313901fcb08)

Shows:

* Prompt injection detection
* Real-time risk scoring
* Automatic blocking of high-risk prompts
* Audit logging of attacks

---

### Failed Login Attempt

[Failed-Login-Wrong-Password.webm](https://github.com/user-attachments/assets/31fe7a8b-e8c5-4ce0-9748-8e392ad84b64)

Shows:

* Authentication enforcement through Keycloak
* Rejection of invalid credentials

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| Authentication | Keycloak (IAM) + JWT (RS256) |
| Authorisation | Realm Roles via RBAC |
| AI Inference | Ollama + TinyLlama |
| Database | SQLAlchemy (PostgreSQL / SQLite) |
| Frontend Dashboard | Streamlit |
| Data Visualisation | Pandas + Matplotlib |
| Deployment | Oracle Cloud VM (Ubuntu) |
| Language | Python 3 |

---

## Features

- **JWT Authentication** — Keycloak issues RS256-signed tokens; the backend fetches the public JWKS to verify every request. No anonymous access to any endpoint.
- **Role-Based Access Control** — `admin`, `analyst`, and `user` roles enforced at both the API layer (FastAPI) and the UI layer (Streamlit). Each role sees a different dashboard.
- **Prompt Injection Detection** — prompts are normalised (lowercased, punctuation stripped, spaces removed) then matched against a weighted pattern dictionary. Scores are summed and capped at 100.
- **Severity Classification** — every request is classified as `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL` based on its risk score.
- **Secure Inference** — only prompts scoring below 80 reach TinyLlama. Responses are trimmed to 500 characters before being returned.
- **Full Audit Logging** — every request (allowed or blocked) is persisted to the database with timestamp, username, prompt, status, risk score, severity, and detected patterns.
- **SOC-style Dashboard** — role-specific Streamlit views with metrics, charts, filterable audit tables, and a user chat interface.

---

## Project Structure

```
secure-ai-gateway/
│
├── main.py          # FastAPI backend — auth, RBAC, threat detection, inference, audit logging
├── dashboard.py     # Streamlit frontend — role-based dashboards and visualisations
├── requirements.txt
├── .env_example
├── .gitignore
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Roles | Description |
|---|---|---|---|
| `GET` | `/` | Public | Health check |
| `POST` | `/chat` | admin, analyst, user | Submit prompt — runs threat detection, forwards to inference if clean |
| `GET` | `/audit` | admin, analyst | Full audit log — all requests, allowed and blocked |
| `GET` | `/blocked` | admin, analyst | Blocked prompts only, with detected patterns |
| `GET` | `/stats` | admin, analyst | Aggregated metrics, severity distribution, top users, request timeline |

### Example: Allowed Response

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

### Example: Blocked Response

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

Prompts are normalised before matching — lowercased, all non-alphanumeric characters stripped, spaces removed. This prevents trivial bypasses like `byp@ss security` or `JAILBREAK`. Pattern scores are summed and hard-capped at 100.

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

| Score Range | Severity | Action |
|---|---|---|
| 80 – 100 | CRITICAL | Blocked, logged |
| 50 – 79 | HIGH | Allowed, logged |
| 20 – 49 | MEDIUM | Allowed, logged |
| 0 – 19 | LOW | Allowed, logged |

---

## Dashboard Views

Authentication happens in the Streamlit frontend itself — the app calls Keycloak's token endpoint with the user's credentials, decodes the JWT to extract realm roles, and renders the appropriate view.

### Admin
- Metrics row: total requests, allowed, blocked, critical attacks
- Pie chart: allowed vs blocked distribution
- Bar chart: severity distribution
- Bar chart: top 5 most active users
- Line chart: request volume over time (grouped by HH:MM)
- Filterable audit log table (filter by username and severity)
- Filterable blocked prompts table

### Analyst
- Blocked prompt log with full attack metadata (prompt, patterns, risk score, severity, timestamp)

### User
- Prompt input with secure AI assistant interface
- Response displayed with risk score and severity classification

---

## Setup & Installation

### Prerequisites

- Python 3.9+
- [Keycloak](https://www.keycloak.org/) running on port `8080`
- [Ollama](https://ollama.com/) running locally with TinyLlama pulled (`ollama pull tinyllama`)
- PostgreSQL or SQLite

### 1. Clone and Install

```bash
git clone https://github.com/your-username/secure-ai-gateway.git
cd secure-ai-gateway
pip install -r requirements.txt
```

### 2. Configure Keycloak

- Create a realm: `secure-ai`
- Create a client: `secure-ai-gateway`
- Create realm roles: `admin`, `analyst`, `user`
- Assign roles to users

### 3. Environment Variables

Create a `.env` file:

```env
# Backend (main.py)
KEYCLOAK_BASE_URL=
DATABASE_URL=

# Frontend (dashboard.py)
BASE_URL=
KEYCLOAK_URL=
REALM=
CLIENT_ID=
CLIENT_SECRET=
```

### 4. Run

```bash
# Start backend
uvicorn main:app --host 0.0.0.0 --port 8000

# Start dashboard
streamlit run dashboard.py --server.port 8501
```

For background deployment on a Linux VM:

```bash
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
nohup streamlit run dashboard.py --server.port 8501 &
```

---

## System Architecture

Five distinct tiers, each with a clear responsibility.

**Frontend (Streamlit)**
Three dashboard views rendered based on the authenticated user's Keycloak realm role. All three authenticate against the same Keycloak instance before any data is fetched.

**Auth (Keycloak)**
Keycloak issues a signed JWT (RS256) on successful login. That token is passed as a Bearer header on every subsequent API call. The backend caches the public JWKS (`lru_cache`) and verifies the token signature on each request, extracting realm roles from the payload.

**Backend (FastAPI)**
After token verification, the backend enforces RBAC — checking that the caller's roles permit the requested endpoint. The prompt then passes to the threat detection engine: normalised, pattern-matched, scored. Any prompt scoring ≥ 80 is blocked and logged immediately. Clean prompts continue to inference.

**Inference (Ollama + TinyLlama)**
Prompts that pass the security filter are forwarded to a locally running Ollama instance on port `11434`. TinyLlama generates a response, which is trimmed to 500 characters and returned with the risk score and severity.

**Storage (SQLAlchemy)**
Every request — blocked or allowed — is persisted to the audit log with a full record. This table powers the `/audit`, `/blocked`, and `/stats` endpoints that feed the admin and analyst dashboards.

---

## Design Decisions Worth Noting

**Why normalise prompts before matching?**
Raw string matching is trivially bypassed — `JAILBREAK`, `j4ilbreak`, `jailbreak!` all evade a case-sensitive exact match. Normalisation (lowercase + strip non-alphanumeric + remove spaces) collapses most surface-level obfuscation attempts before the pattern check runs.

**Why cache the JWKS?**
The public key doesn't change on every request. Fetching it from Keycloak on every API call adds unnecessary latency and a network dependency in the hot path. `lru_cache(maxsize=1)` fetches it once and reuses it.

**Why block at ≥ 80 rather than any non-zero score?**
`act as administrator` scores 75 — this phrase might appear legitimately in a prompt about IAM or system design. A hard threshold at 80 gives the engine some tolerance for ambiguous language while still blocking high-confidence attack patterns.

---

## Key Takeaways

- Built a working **AI security gateway** that intercepts and governs prompts before they reach a language model
- Implemented **end-to-end authentication and authorisation** using Keycloak IAM, RS256 JWT verification, and RBAC enforced at both the API and UI layers
- Designed a **threat detection engine from scratch** — normalisation, pattern matching, weighted risk scoring, and severity classification — without relying on any third-party security library
- Understood **secure inference architecture**: why an LLM should never receive unvalidated input directly from a user
- Operated a **multi-service Linux environment** on cloud infrastructure — managing processes, ports, and networking on an Oracle Cloud Ubuntu VM
- Built **role-aware dashboards** that surface different data depending on who is logged in, reflecting how real security operations tools work

---

## Real-World Relevance

**Prompt injection is a real attack vector.** As organisations integrate LLMs into their products, attackers attempt to override system instructions, extract sensitive data, or bypass content policies through crafted prompts. This gateway implements a defence layer that mirrors what production AI security tools do.

**RBAC is standard in enterprise software.** Any platform handling sensitive data — internal AI assistants, security tooling, financial systems — needs to control who can see what. The role-based separation here reflects how real enterprise platforms are structured.

**Audit logging is a compliance requirement.** In regulated industries, every action on a system must be traceable. Logging every prompt, its risk score, the user who sent it, and whether it was blocked is the foundation of AI governance — a growing requirement as AI regulation matures.

**Self-hosted LLM inference is increasingly relevant.** Many organisations cannot send sensitive data to external APIs for legal or compliance reasons. Running a local model behind a security gateway is a pattern used in enterprise and government deployments.

