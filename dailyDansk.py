#!python /Users/nielssmith/Documents/GitHub/Daily-Danish/dailyDansk.py

# DAILY DANISH PYTHON CODE

# TODO Figure out what's not working with the environmental variables
# TODO Figure out what's not working with Crontab
# TODO display more than 1 pair of words
# TODO Add in the HTML MIME for part2 --> MIMEText(message, "html")

import os
import csv
import smtplib
import base64
from random import choice
from email.message import EmailMessage
from email.mime.text import MIMEText
from email import encoders
from codecs import decode, encode, open
import logging
import helper


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
filename = os.path.join(dir_path, 'logfile.log')
print(filename)


# Get logger
log = helper.logHelper("logfile.log")
log.info("Got logger")

# Import CSV file
header = []
rows = []
with open(
    "/Users/nielssmith/Documents/GitHub/Daily-Danish/translations.csv",
    "r",
   encoding='utf-8', # this was 'utf-8-sig', but I switched it to just 'utf-8', and it still works /shrugemoji
) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Return the next item from the iterator.
    words = list(csvreader)
    word1 = choice(words)  # choose a random element (type: list)
    wordA = " : ".join(word1)  # Type: String
    wordB = encode( #  Transforms to type: string to bytes 
        wordA, "utf-8"
    )
    wordC = ( # Transforms to type: bytes to string
        wordB.decode() 
    )
    # Why exactly is all of that necessary? ...THE BYTES!
    text = "\n {} \n ".format(wordC)
    for row in csvreader: 
        rows.append(row)
        print(row)

# Email Set Up from local environment
key='userUSERuser' # There's not really a point to setting this as a var. it just breaks up the procedure a bit... /big_shrugs
username = os.environ.get(key)
print('username isn\'t working. Look:',username) # return 'none', which isn't the coolest thing right now...
password = os.environ.get("PASS")
print(username,' FUCK YOU LOREM IPSUM FUCK YOU ',password) # 'none' & 'none'  ._.

# Message set up
msg = "Hey, are you reading this message? y/n"
email_sender = username
email_password = password
email_receiver = username
subject = """ 
"""  # THERE MUST BE A SUBJECT. EVEN AN EMPTY ONE! 🤷
path = "/Users/nielssmith/Documents/GitHub/Daily-Danish"
files = [
    i for i in os.listdir() if os.path.isfile(i)
]  # I def can't explain fully how this one liner works... #TODO how does it work?
d = choice(files)
dataB = open(
    d, "rb"
).read()  # read bytes(rb) from file <<<  "rb" mode opens the file in binary format for reading
# print(dataB)
data_base64 = base64.b64encode(dataB)  # encode to base64 (bytes)
# print(type(data_base64))
# print(data_base64)
data_base64 = data_base64.decode()  # convert bytes64 to string

message = """From: Niels Smith
To: Niels Smith
Subject: Daily Danish
{}
""".format(
    text
)

message = message.encode("utf-8")
part1 = MIMEText(message, "plain", "utf-8")  # turn these into plain (TODO later add in html) MIMEText objects
em = EmailMessage()
# print('this is em on line 86', em)
em.attach(part1)
em["Subject"] = subject
em["From"] = username
em["To"] = username
em.set_content(em)


try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo()  # Hostname to send for this command defaults to the FQDN of the local host.
    print('does line 97 get run?')
    smtp_server.login(username, password) #  <<<<----- THIS IS THE LINE WHERE ERRORS ARE THROWN APPARENTLY. There's probably an issue with the env variables...?
    print('does line 99 get run?') # no
    smtp_server.sendmail(username, username, message)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Oh dear, something went wrong...", ex)

#  TEST AREA (feel free to destroy)
user = os.environ['USER']
print(user)
print(username) #None
user