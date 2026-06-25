QueueStorm

A FastAPI-based customer support ticket classification service.

Features

- Health check endpoint
- Ticket classification endpoint
- Detects:
  - Wrong Transfer
  - Payment Failed
  - Refund Request
  - Phishing / Social Engineering
  - Other Cases

Run Locally

Install dependencies:

pip install fastapi uvicorn

Start server:

python -m uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

API Endpoints

GET /health

POST /sort-ticket

Tech Stack

- Python
- FastAPI
- Uvicorn