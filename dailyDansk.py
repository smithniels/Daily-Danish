u'\u2013'.encode('utf-8')
# DAILY DANISH PYTHON CODE

# TODO Add in the HTML MIME for part2 --> MIMEText(message, "html")
# TODO Add in dansk ord fra din dansk oversætter list


import os
import smtplib
import csv
import string
import sys
import base64
from random import choice
from email.message import EmailMessage
from email.mime.text import MIMEText
from email import encoders
from codecs import decode, encode, open


allowed = string.ascii_letters +"æøå" #what is this even for? it's not doing what I hoped it would... :(

# Import CSV file
header = []
rows = []
with open(
    "/Users/nielssmith/Documents/GitHub/Daily-Danish/translations.csv", "r",encoding='utf-8-sig') as file:
    csvreader = csv.reader(file)
    header = next(csvreader) # Return the next item from the iterator.
    words = list(csvreader) 
    word1 = choice(words) # choose a random element (type: list)
    wordA=' : '.join(word1) # Type: String
    wordB = encode(wordA,'utf-8') # Type: Bytes # this is where the string is converted to bytes
    wordC = wordB.decode()  # Type: String # this is where the bytes are converted to string
   
    text= '\n {} \n IF YOU\'RE READING THIS THAN CRONTAB WORKED! WOOH'.format(wordC)
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
subject = ''' 
''' # THERE MUST BE AN OBJECT. EVEN AN EMPTY ONE! 🤷
path = "/Users/nielssmith/Documents/GitHub/Daily-Danish"
files=[i for i in os.listdir() if os.path.isfile(i)] # I def can't explain fully how this one liner works... 
d = choice(files)
dataB = open(d, "rb").read()  # read bytes(rb) from file <<<  "rb" mode opens the file in binary format for reading
data_base64 = base64.b64encode(dataB)  # encode to base64 (bytes)
data_base64 = data_base64.decode()  # convert bytes to string

message = '''From: Niels Smith
To: Niels Smith
Subject: Daily Danish
{}
'''.format(text)

message=message.encode('utf-8')
# Turn these into plain (TODO later add in html) MIMEText objects
part1 = MIMEText(message, "plain", "utf-8")
em = EmailMessage()
em.attach(part1)
em['Subject'] = subject
em["From"] = username
em["To"] = username
em.set_content(em)

try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo() # Hostname to send for this command defaults to the FQDN of the local host.
    smtp_server.login(username, password)
    smtp_server.sendmail(username, username, message)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Oh dear, something went wrong...", ex)


