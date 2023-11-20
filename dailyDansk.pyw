# CD /Users/nielssmith/Documents/GitHub/Daily-Danish && pyinstaller --onefile --noconsole dailyDansk.pyw
# DAILY DANISH PYTHON CODE
#  TODO  add to each row in the CSV so it has:
# -1- Word with translation
# -2- Example sentence
# -3- Pronunciation

import base64
from random import choice
import csv
from codecs import encode
from email.message import EmailMessage
from email.mime.text import MIMEText
import smtplib
import os
import helper

# Get logger
log = helper.logHelper("logfile.log")
log.info("Got logger")

# Import CSV file
header = []
rows = []
with open(
    "/Users/nielssmith/Documents/GitHub/Daily-Danish/translations.csv",
    "r",
    encoding='utf-8'
) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Return the next item from the iterator.
    words = list(csvreader)
    word1 = choice(words)  # choose a random element (type: list)
    wordA = " ~ ".join(word1)
    wordB = encode(
        wordA, "utf-8"
    )
    word_decoded = (
        wordB.decode()
    )
    text = f'\n {word_decoded} \n'
    for row in csvreader:
        rows.append(row)
        print(row)

# Email Set Up from local environment
key = 'userUSERuser'
pwkey = "PASS"
username = os.environ.get(key)
password = os.environ.get(pwkey)

# Message set up
email_sender = username
email_password = password
email_receiver = username
subject = """
"""  # THERE MUST BE A SUBJECT HERE EVEN IF IT'S AN EMPTY ONE!
path = "/Users/nielssmith/Documents/GitHub/Daily-Danish"
files = [
    i for i in os.listdir() if os.path.isfile(i)
]
d = choice(files)
dataB = open(
    d, "rb"
).read()  # read bytes(r.b.) from file <<<  "rb" mode opens the file in binary format for reading
data_base64 = base64.b64encode(dataB)  # encode to base64 (bytes)
data_base64 = data_base64.decode()  # convert bytes64 to string
# f-strings "Formatted string literals"
message = f"""From: Niels Smith
To: Niels Smith
Subject: Daily Danish
{text}
"""
message = message.encode("utf-8")
part1 = MIMEText(message, "plain", "utf-8")
em = EmailMessage()
em.attach(part1)
em["Subject"] = subject
em["From"] = username
em["To"] = username
em.set_content(em)

try:
    # Hostname to send for this command defaults to the FQDN of the local host.
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo()
    smtp_server.login(username, password)
    smtp_server.sendmail(username, username, message)
    smtp_server.close()
    print("Email sent successfully!")
# noinspection PyBroadException
except Exception as EX:
    print("Oh dear, something went wrong...", EX)
