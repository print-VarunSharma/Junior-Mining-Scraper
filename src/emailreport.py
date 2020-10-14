import smtplib
import config
# from gold_reports import gold_pan_bot
import csv
import ssl

# Testing Emai bot function
def send_email(subject, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        # subject = input("Please enter the subject for the email: ")
        # content = input("Please write the content for the email: ")
        message = 'subject: {}\n\n{}'.format(subject, content)
        server.sendmail(config.EMAIL_ADDRESS, recipients, message)
        server.quit()
        print('Success: Email Sent!')
    except Exception as error:
        error = "Failed to connect to server. Email not sent."
        print(error)

# sample test parameters for send_mail function
subject = 'Test 3'
content = f'Hello,\
    here are your 43-101 reports for the day!'
recipients = ['varundevasharma@gmail.com', 'varuns.pybot@gmail.com']

send_email(subject, content)


# Option 1 Secure SSL
import smtplib, ssl
port = 465
password = input("Type password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smpt.gmail.com", port, context=context) as server:
    server.login("varunspybot@gmail.com", password)

#Send Email TODO


# Option 2  Using .starttls()

import smtplib, ssl

def send_pymail(subject, content):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "varunspybot@gmail.com"
    password = input("Type password here: ")

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log into server and send emaikl
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context) #Secures the connection
        server.ehlo()
        server.login(sender_email, password)
        message = 'subject: {}\n\n{}'.format(subject, content)
        
        # Send Email here
    except Exception as error:
        error = "Failed to connect to server. Email not sent."
        print(error)
    finally:
        server.quit()

send_pymail('Test', 'Hello there')



message = """Subject: Gold Reports

Hi {name}, here are your gold reports"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmal.com', 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, report in reader:
            server.sendmain(
                from_address,
                email,
                message,format(name=name, report = report),
            )