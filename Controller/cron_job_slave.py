from datetime import datetime, timedelta
import os
from home import upcoming_events
curr_path=os.path.dirname(os.path.abspath(__file__))
myFile = open(curr_path+'/append.txt', 'a') 
myFile.write('\n on ' + str(datetime.now()))

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def s_email():

    sender_email = "wolftrackproject@gmail.com"
    receiver_email = 'wolftrackproject@gmail.com'
    # App Password of Gmail Account
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack - Job added to List"

    body = "Testing the automated email" + str(datetime.now())

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)

    return True

import dateutil.parser
for i in upcoming_events:
    deadline = dateutil.parser.parse(i['duedate'])
    if(deadline.date()==datetime.now().date()):
        s_email()