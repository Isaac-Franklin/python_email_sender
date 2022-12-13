from email.message import EmailMessage
from env import mailPassword, sender, reciever
import ssl
import smtplib

emailSender = sender
emailPassword = mailPassword

emailReciever = reciever
subject = "Do not forget to subscribe -SECOND TRIAL"
body = """
Kindly subscribe to my Youtube channel today
"""

emDetails = EmailMessage()
emDetails['From'] = emailSender
emDetails['To'] = emailReciever
emDetails['subject'] = subject
emDetails.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReciever, emDetails.as_string())
    
    

