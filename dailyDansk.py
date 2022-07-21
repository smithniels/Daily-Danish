# DAILY DANISH PYTHON CODE
"Alright, I forgot how much I liked working with Python. I put together an automated email sender for sending daily Danish translations. I've been trying to jot down Danish words I run into to look up their translations. The script I have running will email daily with a few randomly selected translations"

# TODO put those images into a csv file to be read into the emails

import os
import smtplib
import ssl
from random import choice
import subprocess #opens the image files on desktop
import base64
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
 

# Email Set Up from local environment
username=os.environ.get('userUSERuser')
password=os.environ.get('PASS')

msg = 'Hey, are you reading this message? y/n'
email_sender = username
email_password = password
email_receiver = username
subject = '''\
    An email from Niels to Niels
'''

# Image Selection (This needs to be fixed/rewritten!)
path="/Users/nielssmith/Documents/GitHub/Daily-Danish"
files=os.listdir(path)
d=choice(files) 
# subprocess.call(['open', d])

data = open(d, 'rb').read() # read bytes from file
data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
data_base64 = data_base64.decode()    # convert bytes to string 

message = """From: Niels Smith
To: Niels Smith
Subject: Daily Danish niels smith

%s
"""  % (msg)

# Turn these into plain (later html) MIMEText objects
part1 = MIMEText(message, "plain")
em = EmailMessage()
em.attach(part1)
em['From'] = username
em['To'] = username
em['Subject'] = subject
em.set_content(em)

# filename = d  # In same directory as script

#  I never got the below working. I think the initial code is correct, but I wasn't able to figure out how to get it into the email =/
# # # Open file in binary mode
# with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
# # Encode file in ASCII characters to send by email    
# encoders.encode_base64(part1)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(username, password)
    smtp_server.sendmail(username,username, message)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Oh dear, something went wrong….",ex)
