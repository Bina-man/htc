import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import HTTPException

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, email_user: str, email_password: str):
        """
        Initializes the email service with SMTP server details and login credentials.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def create_email(self, sender_email: str, receiver_email: str, subject: str, body: str) -> MIMEMultipart:
        """
        Creates an HTML MIME email message.
        """
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Define HTML content
        html_content = f"""
        <html>
        <head></head>
        <body>
            <h2 style="color:blue;">Hello from {sender_email}</h2>
            <p>{body}</p>
        </body>
        </html>
        """

        # Attach the HTML content to the email
        msg.attach(MIMEText(html_content, 'html'))
        return msg

    def create_taxi_request_email(self, sender_email: str, receiver_email: str, subject: str, body: str, name: str) -> MIMEMultipart:
        """
        Creates an HTML MIME email message for a taxi request, specifically for the admin.
        """
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Define HTML content
        html_content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    background-color: #ffffff;
                    margin: 20px auto;
                    padding: 20px;
                    border-radius: 10px;
                    max-width: 600px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                .email-header {{
                    text-align: center;
                    background-color: #4CAF50;
                    padding: 15px;
                    color: #ffffff;
                    border-top-left-radius: 10px;
                    border-top-right-radius: 10px;
                }}
                .email-body {{
                    padding: 20px;
                    font-size: 16px;
                    line-height: 1.5;
                }}
                .email-footer {{
                    text-align: center;
                    font-size: 12px;
                    color: #999999;
                    margin-top: 20px;
                }}
                .email-footer a {{
                    color: #4CAF50;
                    text-decoration: none;
                }}
                h2 {{
                    color: #4CAF50;
                    margin-bottom: 20px;
                }}
                .content {{
                    margin-bottom: 20px;
                }}
                .footer-link {{
                    text-decoration: none;
                    color: #4CAF50;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="email-header">
                    <h1>New Taxi Request Notification</h1>
                </div>
                <div class="email-body">
                    <h2>Dear Admin,</h2>
                    <p>You have received a new taxi service request. Please review the details below:</p>
                    
                    <div class="content">
                        <p><strong>Request Details:</strong></p>
                        <p><strong>Name:</strong> {name or sender_email}</p>
                        <p><strong>Email:</strong> {sender_email}</p>
                        <p><strong>Message:</strong> {body}</p>
                    </div>

                    <p>If any further action is required or you would like to follow up, feel free to reply to this email or contact the requester directly.</p>
                </div>
                <div class="email-footer">
                    <p>Powered by <a href="#" class="footer-link">Your Taxi Company</a> | © {2024}</p>
                </div>
            </div>
        </body>
        </html>
        """

        # Attach the HTML content to the email
        msg.attach(MIMEText(html_content, 'html'))
        return msg



    def send_email(self, sender_email: str , receiver_email: str, subject: str,body: str, name: str = None):
        """
        Sends an email using the SMTP server.
        """
        try:
            # Create email
            email_message = self.create_taxi_request_email(sender_email, receiver_email, subject, body, name)

            # Connect to SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection with TLS
                server.login(self.email_user, self.email_password)  # Login to the email server
                server.send_message(email_message)  # Send the email
            return {"message": "Email sent successfully!"}
        except smtplib.SMTPAuthenticationError:
            raise HTTPException(status_code=401, detail="Authentication failed. Please check your email credentials.")
        except smtplib.SMTPRecipientsRefused:
            raise HTTPException(status_code=400, detail="Invalid recipient email address.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred while sending the email: {str(e)}")