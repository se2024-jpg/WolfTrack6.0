import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def s_email(company_name,location, Job_Profile,salary, user, passwrd,email,sec_question,sec_answer,notes,date_applied):

    sender_email = "wolftrackproject@gmail.com"
    receiver_email = email
    # App Password of Gmail Account
    password = "dlafyfekdkmdfjdi"

    subject = "WolfTrack - Job added to List"
    body = "WOLFTRACK APPLICATION \n\n" \
           "You have applied to " + company_name + " for the job profile - " + Job_Profile + \
           ". \nPlease find the details below: \n" \
           "Date Applied: " + date_applied + "\n" "Location: " + location + "\n" \
           "Salary: " + salary + "\n"\
           "User_name: " + user + "\n"\
            "Password: " + passwrd + "\n"\
           "Security Question: " + sec_question + "\n" \
            "Security Answer: " + sec_answer + "\n" \
            "Notes: " + notes + "\n\n" \
            "All the best for you Application!\n"\
            "The WolfTrack Team."


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",
                          465,
                          context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)

    return True


def s_comment_email(email,comments):

    sender_email = "wolftrackproject@gmail.com"
    receiver_email = email
    # App Password of Gmail Account
    password = "dlafyfekdkmdfjdi"

    subject = "Resume - Comments"
    body = "Our admin has reviewed your profile. Please check below comments : \n"+ comments;



    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",
                          465,
                          context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)

    return True