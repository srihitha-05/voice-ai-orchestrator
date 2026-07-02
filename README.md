# Multi-Tenant Agentic Voice Orchestrator

An AI-powered multi-tenant Voice SaaS platform that automates outbound lead qualification calls using Vapi AI, LangGraph, FastAPI, MongoDB Atlas, React, and Docker.

---

## Features

- Multi-tenant architecture
- Company-specific lead management
- Outbound campaign triggering
- AI-powered transcript evaluation using LangGraph + LLM
- Customer status updates
- Call log storage
- Responsive React dashboard
- Dockerized backend
- Cloud-ready deployment

---

## Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS
- Axios

### Backend
- FastAPI
- LangGraph
- Groq LLM
- Vapi AI
- MongoDB Atlas
- Motor

### Deployment
- Docker
- Render (Cloud Ready)

---

# Database Schema

## Company

```
{
  _id,
  name,
  prompt
}
```

## Customer

```
{
  _id,
  company_id,
  name,
  phone,
  status
}
```

Status values:

- PENDING
- CALL_INITIATED
- QUALIFIED
- NOT_INTERESTED
- NEEDS_REVIEW
- FAILED

## Call Logs

```
{
  _id,
  customer_id,
  transcript,
  summary,
  status,
  created_at
}
```

---

# LangGraph Architecture

The workflow consists of three nodes:

## 1. Evaluation Node

- Receives transcript from the Vapi webhook
- Sends transcript to the LLM
- Predicts lead qualification status

Possible outputs:

- QUALIFIED
- NOT_INTERESTED
- NEEDS_REVIEW

---

## 2. State Update Node

Updates the customer status inside MongoDB.

---

## 3. Call Log Node

Stores:

- Transcript
- Final status
- Timestamp

---

# Project Structure

```
VoiceAI/

backend/
    api/
    routes/
    services/
    langgraph_flow/
    Dockerfile
    requirements.txt
    main.py

frontend/
    src/
    components/
    services/

README.md
```

---

# Environment Variables

Create a `.env` file inside the backend folder.

```
MONGODB_URI=

GROQ_API_KEY=

VAPI_API_KEY=

VAPI_ASSISTANT_ID=
```

Do not commit the `.env` file.

---

# Running Locally

## Backend

```
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python seed.py

uvicorn main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## Frontend

```
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# Docker

Build

```
docker build -t voiceai-backend .
```

Run

```
docker run -p 8000:8000 --env-file .env voiceai-backend
```

---

# Deployment

Backend:
- Docker
- Render Web Service

Frontend:
- Render Static Site

Secrets are configured through Render Environment Variables.

---

# Testing

1. Select a company.
2. View customers.
3. Trigger Campaign.
4. Simulate a Vapi webhook.
5. LangGraph evaluates transcript.
6. Customer status updates.
7. Dashboard reflects updated status.

---

# Human-in-the-Loop

If the LLM cannot confidently determine customer intent, the lead is marked as:

```
NEEDS_REVIEW
```

This allows a human administrator to manually review the conversation before taking action.

---

# Known Limitation

The application integrates with Vapi AI for outbound calling.

However, during testing, the free Vapi phone numbers available at the time of development did not support outbound calls to Indian (+91) mobile numbers due to international calling restrictions on the free tier.

The complete outbound calling workflow, webhook integration, LangGraph orchestration, transcript evaluation, database updates, and dashboard functionality are fully implemented.

Webhook payloads can be tested through FastAPI Swagger or by using supported Vapi phone numbers available on paid plans.

---

# Future Improvements

- Real-time WebSocket updates
- Authentication
- Admin roles
- Campaign history
- Analytics dashboard
- Native GCP Cloud Run deployment
