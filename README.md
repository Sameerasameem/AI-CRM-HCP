# AI-First CRM HCP Module

An AI-powered Customer Relationship Management (CRM) application designed for Healthcare Professional (HCP) interaction management. The application enables field representatives to log, search, edit, summarize, and manage HCP interactions using an AI assistant powered by LangGraph and Groq LLM.

# Features

- AI-powered conversational interface
- Structured interaction logging
- Search previous HCP interactions
- Edit existing interaction records
- Generate interaction summaries
- Recommend next follow-up actions
- PostgreSQL database integration
- FastAPI REST API
- React + Redux frontend
- LangGraph AI Agent with Tool Calling

# Technology Stack

## Frontend

- React
- Redux
- HTML5
- CSS3
- JavaScript

## Backend

- Python
- FastAPI
- LangGraph
- LangChain
- Groq LLM (Gemma 2)

## Database

- PostgreSQL
- SQLAlchemy ORM


# LangGraph Agent

The LangGraph agent acts as the intelligent workflow engine of the application.

It understands user requests, decides which tool should be executed, invokes the appropriate tool, and returns a natural language response.

The agent supports the following tools:

1. Log Interaction
2. Edit Interaction
3. Search Interaction
4. Generate Summary
5. Recommend Next Action


# Project Structure

```
AI-CRM-HCP
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
├── backend
│   ├── app.py
│   ├── agent.py
│   ├── graph.py
│   ├── tools.py
│   ├── database.py
│   ├── models.py
│   ├── create_tables.py
│   ├── requirements.txt
│   └── .env
│
└── README.md


# AI Workflow
User

↓

React Frontend

↓

FastAPI Backend

↓

LangGraph Agent

↓

Groq LLM

↓

Tool Selection

↓

PostgreSQL Database

↓

Response to User
```

---

# Database Schema

## interactions

| Column | Type |
|---------|------|
| id | Integer |
| hcp_name | String |
| interaction_type | String |
| notes | Text |
| created_at | DateTime |

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/your-username/AI-CRM-HCP.git
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the backend folder.

```env
GROQ_API_KEY=your_groq_api_key

DATABASE_URL=postgresql://postgres:your_password@localhost:5432/ai_crm
```

---

## Create Database

```sql
CREATE DATABASE ai_crm;
```

---

## Create Tables

```bash
python create_tables.py
```

---

## Run Backend

```bash
uvicorn app:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# API Endpoint

## POST /chat

Example Request

```json
{
  "message": "Log interaction with Dr. Kumar about diabetes medicine."
}
```

Example Response

```json
{
  "response": "Interaction logged successfully."
}
```

---

# Implemented LangGraph Tools

### Log Interaction

Logs HCP interaction details into PostgreSQL.

### Edit Interaction

Updates interaction notes.

### Search Interaction

Retrieves previous interactions from PostgreSQL.

### Generate Summary

Generates a concise summary of previous interactions.

### Recommend Next Action

Provides AI-generated recommendations for future follow-ups.

---

# Project Highlights

- AI-first CRM architecture
- LangGraph-based agent workflow
- Tool Calling using LangChain
- PostgreSQL persistence
- FastAPI REST APIs
- React frontend
- Groq LLM integration
- Modular backend architecture

---

# Future Enhancements

- User authentication
- Role-based access control
- Dashboard analytics
- File attachment support
- Calendar integration
- Email notifications
- Multi-HCP management
- Interaction timeline visualization

---

# Author

Sameera Sameem

 