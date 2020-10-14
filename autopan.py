from autoscraper import AutoScraper
import config

def autopan_bot():
    url = 'https://www.juniorminingnetwork.com/mining-topics/topic/drill-results.html'
    highgrade_scraper = 'high grade scraper'
    # We can add one or multiple candidates here.
    # You can also put urls here to retrieve urls.
    wanted_list = ['High Grade', 'High-Grade']
    botscraper = AutoScraper()
    highgrade_results = botscraper.build(url, wanted_list)
    print(highgrade_results)
    if(highgrade_results):
        for result in highgrade_results:
            print('BriefHub bot has found results! 🚀')
            print(highgrade_results)
    elif(highgrade_results == None):
        print("Hmmm, it doesn't look like we found anything")
        exit(-1)
    botscraper.save(highgrade_scraper)
    print(f"💿 > Save the model {highgrade_scraper}")

def send_email(subject, content, recipients):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'subject: {}\n\n{}'.format(subject, content)
        server.sendmail(config.EMAIL_ADDRESS, recipients, message)
        server.quit()
        print('Success: Email Sent!')
    except Exception as error:
        error = "Failed to connect to server. Email not sent."
        print(error)

# sample test parameters for send_mail function
# subject = 'Test 3'
# content = f'Hello,\
#     here are your 43-101 reports for the day!'
# recipients = ['varundevasharma@gmail.com', 'varuns.pybot@gmail.com']