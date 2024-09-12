import os
from fastapi import APIRouter, Depends
from models import EmailRequest
from services.email_service import EmailService

router = APIRouter()

# @router.post("/send_email", response_model=None)
# async def send_email(email_request: EmailRequest):
#     response = email_service.send_email(
#         sender_email=email_request.sender_email,
#         receiver_email=email_request.receiver_email,
#         subject=email_request.subject,
#         body=email_request.body
#     )
#     return response


import os

@router.get("/checkemailsend/{sender_email}")
async def check_email_send(sender_email: str):
    try:
        # Get email credentials from environment variables
        email_password = os.getenv('EMAIL_PASSWORD', 'default_password')  # Provide default as fallback
        base_email = os.getenv('BASE_EMAIL', 'binyamsisay01@gmail.com')   # Provide default as fallback

        # Initialize the EmailService with credentials from environment variables
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
