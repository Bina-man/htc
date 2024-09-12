import os
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter
from services.email_service import EmailService

router = APIRouter()

class HTCTaxi(BaseModel):
    name:  Optional[str]
    email: Optional[str]
    body: str

@router.post("/send_email", response_model=None)
async def send_email(email_request: HTCTaxi):
    email_password = os.getenv('EMAIL_PASSWORD', 'default_password')
    base_email = os.getenv('BASE_EMAIL', 'binyamsisay01@gmail.com')
    
    email_service = EmailService(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        email_user=base_email,
        email_password=email_password
    )
    
    response = email_service.send_email(
        sender_email=email_request.email,
        receiver_email='binasisayet8790@gmail.com',
        subject="Taxi Request",
        body=email_request.body,
        name = email_request.name
    )
    
    return response

@router.get("/checkemailsend/{sender_email}")
async def check_email_send(sender_email: str):
    try:
        email_password = os.getenv('EMAIL_PASSWORD', 'default_password')
        base_email = os.getenv('BASE_EMAIL', 'binyamsisay01@gmail.com') 
        email_service = EmailService(
            smtp_server="smtp.gmail.com",
            smtp_port=587,
            email_user=base_email,
            email_password=email_password
        )

        # Send email with hardcoded sender and recipient emails
        email_service.send_email(
            sender_email=base_email,  # Sender is fixed to base_email
            receiver_email="binasisayet8790@gmail.com",  # Receiver is always this email
            subject="Test Email",
            body=f"This is a test email from {sender_email} to binasisayet8790@gmail.com to check email sending functionality."
        )
        return {"message": "Email sending check successful!"}
    except Exception as e:
        return {"message": f"Email sending failed: {e}"}
