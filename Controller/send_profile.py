'''
MIT License

Copyright (c) 2023 Shonil B, Akshada M, Rutuja R, Sakshi B

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import email, smtplib, ssl
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def s_profile(data,upcoming_events, profile,emailID):

    sender_email = "wolftrackproject@gmail.com"
    receiver_email = emailID
    # App Password of Gmail Account
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack - Profile Mailing"
    str1=""
    for key,value in data.items():
        print("\n")
        l=[]
        l = value
        str1  = str1 + key +': '+ ' '.join(value) + '\n'
        print("\n")

    body = "WOLFTRACK APPLICATION \n\n" \
           + str1


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    path = 'Controller/resume'

    files = os.listdir(path)

    for filename in files:
        print(filename)
        attachment = open('Controller/resume/'+filename, 'rb')

        part = MIMEBase("application", "octet-stream")

        part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header("Content-Disposition",
        f"attachment; filename= {filename}")

        message.attach(part)

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",
                          465,
                          context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)

    return True