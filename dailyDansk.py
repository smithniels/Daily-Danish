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
import base64


from random import choice
from email.message import EmailMessage
from email.mime.text import MIMEText
from email import encoders

allowed = string.ascii_letters +"æøå"




# Import CSV file
header = []
rows = []
with open(
    "/Users/nielssmith/Documents/GitHub/Daily-Danish/translations.csv", "r"
) as file:
    csvreader = csv.reader(file)
    header = next(csvreader) # Return the next item from the iterator.
    words = list(csvreader) 
    word1 = choice(words) # choose a random element 
    # word2 = choice(words)
    # word3 = choice(words)
    # print('these are the words: \n {} \n {} \n {}'.format(word1,word2,word3))
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
''' #just leave this blank. it needs to be here, but it doesn't require any text 🤷
path = "/Users/nielssmith/Documents/GitHub/Daily-Danish"
files=[i for i in os.listdir() if os.path.isfile(i)] # I def can't explain fully how this one liner works... 
d = choice(files)
dataB = open(d, "rb").read()  # read bytes(rb) from file <<<  "rb" mode opens the file in binary format for reading
data_base64 = base64.b64encode(dataB)  # encode to base64 (bytes)
data_base64 = data_base64.decode()  # convert bytes to string


text= '\n {} \n'.format(word1)
# text.decode('iso-8859-1')
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
    
    
def tell_me_about(s): 
    print(s) 
    return (type(s), s)

# v = "\xC4pple"
# uv = v.bytes.decode("iso-8859-1")
# print(tell_me_about(v)