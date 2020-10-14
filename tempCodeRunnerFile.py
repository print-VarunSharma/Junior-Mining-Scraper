
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