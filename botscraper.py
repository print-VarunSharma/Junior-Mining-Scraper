from autoscraper import AutoScraper

url = 'https://www.juniorminingnetwork.com/mining-topics/topic/drill-results.html'
highgrade_scraper = 'high grade scraper'
# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ['High Grade', 'High-Grade']

botscraper = AutoScraper()

highgrade_results = botscraper.build(url, wanted_list)

if(highgrade_results):
    for result in highgrade_results:
        print('BriefHub bot has found results! 🚀')
        print(highgrade_results)

elif(highgrade_results == None):
    print("Hmmm, it doesn't look like we found anything")
    exit(-1)

botscraper.save(highgrade_scraper)
print(f"💿 > Save the model {highgrade_scraper}")

