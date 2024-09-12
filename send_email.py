import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = 'binyamsisay01@gmail.com'
receiver_email = 'binasisayet8790@gmail.com'
subject = "Subject of the Email"
body = "This is the body of the email."

# Create a MIMEText message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message body
msg.attach(MIMEText(body, 'plain'))

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
password = 'gdwm kgig xcwk mhuk'

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start the TLS encryption
    server.login(sender_email, password)  # Login to your email
    server.send_message(msg)  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
finally:
    server.quit()  # Close the connection
