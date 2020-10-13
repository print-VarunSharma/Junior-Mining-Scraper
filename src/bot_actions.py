import smtplib
import os
import csv
import ssl
from config import PYBOT_EMAIL, PYBOT_PW
# from dotenv import load_dotenv  
# load_dotenv() 

# PYBOT_EMAIL = os.getenv("PYBOT_EMAIL_ADDRESS")
# PYBOT_PW = os.getenv("PYBOT_EMAIL_PASSWORD")  

def send_emailreport(subject, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(PYBOT_EMAIL, PYBOT_PW)
        message = 'subject: {}\n\n{}'.format(subject, content)
        server.sendmail(PYBOT_EMAIL, recipients, message)
        server.quit()
        print('Success: Email Sent!')
    except Exception as error:
        error = "Failed to connect to server. Email not sent."
        print(error)

subject = 'Test 3'
content = f'Hello,\
    This is a Discord Email Test'
recipients = ['varundevasharma@gmail.com', 'varuns.pybot@gmail.com']

send_emailreport(subject, content)