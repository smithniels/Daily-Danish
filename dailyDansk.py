#  coding: utf-8
# DAILY DANISH PYTHON CODE
"Alright, I forgot how much I liked working with Python. I put together an automated email sender for sending daily Danish translations. I've been trying to jot down Danish words I run into to look up their translations later. The script I have running will email daily with a few randomly selected translations pulled from a CSV file. Pretty nifty."


# TODO I'm getting an encoding error occasionally "u'\u2013'.encode('utf-8')" might be the solution, but I don't know where to stick that. that's what she said
# TODO Set up chrontab to run programs on the daily 
# TODO Add in the HTML MIME for part2
# TODO Add in dansk ord fra din dansk oversætter list

u'\u2013'.encode('utf-8')
import os
import smtplib
import csv
from random import choice
import base64
from email.message import EmailMessage
from email.mime.text import MIMEText

# Import CSV file
header = []
rows = []
with open(
    "/Users/nielssmith/Documents/GitHub/Daily-Danish/translations.csv", "r"
) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    words = list(csvreader)
    word1 = choice(words)
    word2 = choice(words)
    word3 = choice(words)
    # print('these are the word: \n {} \n {} \n {}'.format(word1,word2,word3))
    for row in csvreader:
        rows.append(row)
        print(row)



# Email Set Up from local environment
username = os.environ.get("userUSERuser")
password = os.environ.get("PASS")
msg = "Hey, are you reading this message? y/n"
email_sender = username
email_password = password
email_receiver = username
text= '{} \n {} \n {}'.format(word1,word2,word3)
subject = ''' 
''' #just leave this blank. it needs to be here, but it doesn't require text 🤷
path = "/Users/nielssmith/Documents/GitHub/Daily-Danish"
files=[i for i in os.listdir() if os.path.isfile(i)]
d = choice(files)
dataB = open(d, "rb").read()  # read bytes from file
data_base64 = base64.b64encode(dataB)  # encode to base64 (bytes)
data_base64 = data_base64.decode()  # convert bytes to string
message = '''From: Niels Smith
To: Niels Smith
Subject: Daily Danish Words
{}
'''.format(text)

# Turn these into plain (later html) MIMEText objects
part1 = MIMEText(message, "plain")
em = EmailMessage()
em.attach(part1)
em['Subject'] = subject
em["From"] = username
em["To"] = username
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
