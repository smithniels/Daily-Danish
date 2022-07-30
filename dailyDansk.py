u'\u2013'.encode('utf-8')
# DAILY DANISH PYTHON CODE
"Alright, I forgot how much I liked working with Python. I put together an automated email sender for sending daily Danish translations. I've been trying to jot down Danish words I run into to look up their translations later. The script I have running will email daily with a few randomly selected translations pulled from a CSV file. Pretty nifty."

# TODO I'm getting an encoding error occasionally "u'\u2013'.encode('utf-8')" might be the solution, but I don't know where to stick that. that's what she said
# TODO Set up Chron Tab to run programs on the daily 
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

print('This is the start! This is the start! This is the start! This is the start! This is the start! ')
allowed = string.ascii_letters +"æøå" #what is this even for? it's not doing what I hoped it would... :(

# Import CSV file
header = []
rows = []
with open(
    "/Users/nielssmith/Documents/GitHub/Daily-Danish/translations.csv", "r",encoding='utf-8-sig') as file:
    csvreader = csv.reader(file)
    header = next(csvreader) # Return the next item from the iterator.
    words = list(csvreader) 
    # print('words[0] type: ',type(words[0]), words[0]) # Type: List
    word1 = choice(words) # choose a random element (type: list)
    # print('word1 type: ',type(word1), word1) #Type: List
    wordA=' : '.join(word1) # Type: String
    wordB = encode(wordA,'utf-8') # Type: Bytes # this is where the string is converted to bytes
    wordC = wordB.decode()  # Type: String # this is where the bytes are converted to string
   
    text= '\n {} \n'.format(wordC)
    for row in csvreader:
        rows.append(row)
        print(row)
    
# What's going on...?
# print('wordA type: ',type(wordA), wordA)
# print('wordB type: ',type(wordB), wordB)
print('wordC type: ',type(wordC), wordC)
# print('text  type: ',type(text), text)

# Email Set Up from local environment
username = os.environ.get("userUSERuser")
password = os.environ.get("PASS")
msg = "Hey, are you reading this message? y/n"
email_sender = username
email_password = password
email_receiver = username
subject = ''' 
''' #just leave this blank. it needs to be here, but it doesn't require any text 🤷
path = "/Users/nielssmith/Documents/GitHub/Daily-Danish"
files=[i for i in os.listdir() if os.path.isfile(i)] # I def can't explain fully how this one liner works... 
d = choice(files)
dataB = open(d, "rb").read()  # read bytes(rb) from file <<<  "rb" mode opens the file in binary format for reading
data_base64 = base64.b64encode(dataB)  # encode to base64 (bytes)
print('this is data_base64 post encode(): ',data_base64)
data_base64 = data_base64.decode()  # convert bytes to string
print('this is type() of data_base64 post decode()',type(data_base64))
print('this is data_base64: ',data_base64)

message = '''From: Niels Smith
To: Niels Smith
Subject: Daily Danish
{}
'''.format(text)

# Turn these into plain (TODO later add in html) MIMEText objects
part1 = MIMEText(message, "plain")
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


