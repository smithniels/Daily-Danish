import os
import smtplib
import ssl
from email.message import EmailMessage

username=os.environ.get('userUSERuser')
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


try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(username, password)
    smtp_server.sendmail(username,username, body)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
