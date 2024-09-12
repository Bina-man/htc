from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    sender_email: EmailStr
    receiver_email: EmailStr
    subject: str
    body: str
