import bs4 as bs
import urllib.request
import schedule
import time
from datetime import datetime

URL = 'https://www.voetbalkrant.com'
source = urllib.request.urlopen('https://www.voetbalkrant.com/').read()
soup = bs.BeautifulSoup(source, 'lxml')

artikels = soup.find('div', id="more_news")

gent_artikels = {}

def artikel_toevoegen(artikel_dict, artikel_titel, artikel_link):
    if artikel_titel not in artikel_dict:
        artikel_dict[artikel_titel] = artikel_link
        print(f'[{datetime.now():%d-%m-%Y %H:%M}]{artikel_titel}')
        print(f'{artikel_link}\n')
    else:
        pass


def ophalen():
    for artikel in artikels.find_all('div', class_="item-content"):
        for logo in artikel.find_all('a', class_='rel_team_logo'):
            if logo.img['alt'] == 'KAA Gent':
            # if logo.img['alt'] == 'Borussia Dortmund': # ! Test case, indien geen Gent Artikels beschikbaar
                titel = str(artikel.h3.text).strip()
                link = (URL+artikel.h3.find('a')['href']).strip()
                artikel_toevoegen(gent_artikels, titel, link)

schedule.every().hour.do(ophalen)

while True:
    schedule.run_pending()
    time.sleep(1)