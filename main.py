from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Ticket(BaseModel):
    ticket_id: str
    channel: str = None
    locale: str = None
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/sort-ticket")
def sort_ticket(ticket: Ticket):

    msg = ticket.message.lower()

    case_type = "other"
    severity = "low"
    department = "customer_support"
    review = False
    confidence = 0.80

    if "wrong" in msg and "number" in msg:
        case_type = "wrong_transfer"
        severity = "high"
        department = "dispute_resolution"
        review = True
        confidence = 0.95

    elif "payment failed" in msg or "balance deducted" in msg:
        case_type = "payment_failed"
        severity = "high"
        department = "payments_ops"
        confidence = 0.90

    elif "refund" in msg:
        case_type = "refund_request"
        severity = "low"
        department = "customer_support"
        confidence = 0.90

    elif "otp" in msg or "pin" in msg or "password" in msg:
        case_type = "phishing_or_social_engineering"
        severity = "critical"
        department = "fraud_risk"
        review = True
        confidence = 0.99

    return {
        "ticket_id": ticket.ticket_id,
        "case_type": case_type,
        "severity": severity,
        "department": department,
        "agent_summary": f"Customer reported: {ticket.message}",
        "human_review_required": review,
        "confidence": confidence
    }