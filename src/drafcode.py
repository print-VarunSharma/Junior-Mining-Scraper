class automated_email:
    def __init__(self, protocol_1, protocol_2, start_tls, bot_login ):
        self.protocol_1 = protocol_1
        self.protocol_2 = protocol_2
        self.start_tls = start_tls
        self.bot_login = bot_login
    
    def protocol_1(self):
        return self.server.smtplib.SMTP('smtp.gmail.com:587')

        self.protocol_1 = server.smtplib.SMTP('smtp.gmail.com:587')
        self.protocol_2 = server.ehlo()
        self.start_tls = server.starttls()
        self.bot_login = server.login(config.EMAIL_ADDRESS, config.PASSWORD)

print(automated_email.protocol_1)
