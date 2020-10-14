from bs4 import BeautifulSoup
import requests
import csv

result = requests.get('http://juniorminingnetwork.com/').text
# src = result.content
soup = BeautifulSoup(result, 'html.parser')

# urls = []
# for h4_tag in soup.find_all('h4'):
#     a_tag = h4_tag.find('a')
#     urls.append(a_tag.attrs['href'])
#     print(urls)

# gold_pan_bot scrapes JrMiningNetwork for 43-101 reports
def gold_pan_bot ():
    for report_43 in soup.find_all('h4', class_='mod-articles-category-title'):
        if 'Reports' in report_43:
            report_link = report_43.a.href.text
            return (f'Success! Here are the gold report links: /n {report_link}')
        else:
            if '43-101' not in report_43:
                return ('No 43-101 Reports today. Keep on Panning!')
gold_pan_bot()

# links = soup.find_all('a')
# report43 = []
# for link in links:
#     if '43-101' in link.text:
#         print(report43.append(link.attrs['href']))

#-----------------------------------------------------------------------------#
csv_file = open('goldReport_scrapes.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['gold_headlines', 'gold_links', 'video_link'])


for article in soup.find_all('h4', class_='mod-articles-category-title'):
    gold_headlines = article.h4.a.text
    print(gold_headlines)

    gold_links= article.a.text
    print(gold_links)
    print()


for article in soup.find_all('results'):
    # print(article.prettify())
    gold_headlines = article.h4.a.text 
    print(gold_headlines)

    gold_links = article.find('h4', class_='mod-articles-category-title').a.text
    print(gold_links)
    print()

    csv_writer.writerow([gold_headlines, gold_links])

csv_file.close()
