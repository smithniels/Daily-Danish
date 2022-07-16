
# DAILY DANISH PYTHON CODE

import os
import smtplib
import ssl
import random
import subprocess
import base64
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders


# Email Set Up
username=os.environ.get('userUSERuser')
password=os.environ.get('PASS')
print(password, username)

email_sender = username
email_password = password
email_receiver = username
subject = '''this is from Niels to Niels'''


# Image Selection (This needs to be fixed/rewritten!)
path="/Users/nielssmith/Documents/GitHub/Daily-Danish"
files=os.listdir(path)
d=random.choice(files) 
# subprocess.call(['open', d])


data = open(d, 'rb').read() # read bytes from file
data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
data_base64 = data_base64.decode()    # convert bytes to string 
text = ''' Howdy, hey'''
html = '<img src="data:image/png;base64,' + data_base64 + '">' # embed in html
open('output-png.html', 'w').write(html)
 


# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

em = EmailMessage()

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
em.attach(part1)
em.attach(part2)


em['From'] = username
em['To'] = username
em['Subject'] = subject
em.set_content(html)
 
filename = d  # In same directory as script

# # Open file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part2)


try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(username, password)
    smtp_server.sendmail(username,username, html)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Oh dear, something went wrong….",ex)