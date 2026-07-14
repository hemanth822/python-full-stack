'''

                        DAY 18 - PYTHON CONCEPTS
SMTP module
email.message
rjyq twgi htwe idzc

'''

import smtplib
import ssl
from email.message import EmailMessage
sender_email = "ekanthvarma2005@gmail.com"
password = "rjyqtwgihtweidzc"

reciever_email = "kalyankorada16@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = "Welcome Mail"
message.set_content("welcome to vizag")
context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.send_message(message)
    
