import os
import smtplib
from email import message
from dotenv import load_dotenv
from string import Template
from pathlib import Path # similar to os.path

load_dotenv()

html = Template(Path("index.html").read_text())
email = message.EmailMessage()
email["from"] = "Mueez Khan"
email["to"] = os.getenv("SEND_ADDRESS")
email['subject'] = "Woah this is an email from Python!"

email.set_content(html.substitute({ "name" : "Mueez" }), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(os.getenv("EMAIL_ADDRESS"), os.getenv("PASSWORD"))
    smtp.send_message(email)
    print('All good boss!')