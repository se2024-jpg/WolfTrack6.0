'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import os
import smtplib
import ssl
import logging
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, List

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = os.getenv("SENDER_EMAIL")  # Environment variable for sender's email
PASSWORD = os.getenv("EMAIL_PASSWORD")    # Environment variable for sender's password
RESUME_PATH = "Controller/resume"         # Directory containing resume files

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def attach_files(message: MIMEMultipart, path: str):
    """
    Attaches files from the specified directory to the email message.
    """
    try:
        files = os.listdir(path)
        for filename in files:
            file_path = os.path.join(path, filename)
            with open(file_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {filename}")
                message.attach(part)
        logging.info("All files attached successfully.")
    except FileNotFoundError as e:
        logging.error(f"Directory {path} not found: {e}")
    except Exception as e:
        logging.error(f"Error attaching files: {e}")

def send_email(subject: str, body: str, receiver_email: str, path: str) -> bool:
    """
    Sends an email with the specified subject, body, and attachments from the given path.
    """
    if not SENDER_EMAIL or not PASSWORD:
        logging.error("Sender email or password is not set in environment variables.")
        return False

    # Create the email message
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email
    message.attach(MIMEText(body, "plain"))

    # Attach files from the specified path
    attach_files(message, path)

    # Send the email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
        logging.info(f"Email sent successfully to {receiver_email}.")
        return True
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {receiver_email}: {e}")
        return False

def s_profile(data: Dict[str, List[str]], upcoming_events: List[str], profile: str, email_id: str) -> bool:
    """
    Sends a profile summary email with event details to the specified email.
    """
    subject = "WolfTrack - Profile Mailing"
    profile_details = "\n".join([f"{key}: {' '.join(value)}" for key, value in data.items()])
    body = f"WOLFTRACK APPLICATION\n\n{profile_details}"

    # Send the email
    return send_email(subject, body, email_id, RESUME_PATH)
