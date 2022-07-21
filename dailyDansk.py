# DAILY DANISH PYTHON CODE
"Alright, I think it's been about a whole minute. I forgot how much I liked writing Python! I put together an automated email sender that sends daily Danish translations for words that I've come across. The script I have running will email daily with a few randomly selected translations. >Link to code repo<"

# TODO put those images into a csv file to be read into the emails
# TODO I don't think all of these imports are being used (encoder/subprocess/ CSV should probably be swapped for pandas)

import os
import smtplib
import ssl
import csv
from random import choice
import subprocess  # opens the image files on desktop
import base64
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

# Import CSV file
header = []
rows = []
with open(
    "/Users/nielssmith/Documents/GitHub/Daily-Danish/translations.csv", "r"
) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        print(row)

# print(rows)


# Email Set Up from local environment
username = os.environ.get("userUSERuser")
password = os.environ.get("PASS")

msg = "Hey, are you reading this message? y/n"
email_sender = username
email_password = password
email_receiver = username
subject = """\
    An email from Niels to Niels
"""

# Image Selection (This needs to be fixed/rewritten!)
path = "/Users/nielssmith/Documents/GitHub/Daily-Danish"
files = os.listdir(path)
d = choice(files)
dataB = open(d, "rb").read()  # read bytes from file
data_base64 = base64.b64encode(dataB)  # encode to base64 (bytes)
data_base64 = data_base64.decode()  # convert bytes to string

message = """From: Niels Smith
To: Niels Smith
Subject: Daily Danish niels smith


{}{}
""".format('text will go here',' and then  more text will go here')

# Turn these into plain (later html) MIMEText objects
part1 = MIMEText(message, "plain")
em = EmailMessage()
em.attach(part1)
em["From"] = username
em["To"] = username
em["Subject"] = subject
em.set_content(em)


try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo()
    smtp_server.login(username, password)
    smtp_server.sendmail(username, username, message)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Oh dear, something went wrong….", ex)
