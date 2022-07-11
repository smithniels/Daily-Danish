import os
import smtplib
import ssl
from email.message import EmailMessage

username=os.environ.get('userUSERuser')
print(username)
password=os.environ.get('PASS')
print(password, username)

email_sender = username
email_password = password
email_receiver = username


subject = 'this is from Niels to Niels'
body = """
Let's try to send an email
"""

em = EmailMessage()
em['From'] = username
em['To'] = username
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',  997 , context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())