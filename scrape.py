import re
import requests
from bs4 import BeautifulSoup

def scrapejp():
    return __scrape('https://fate-go.cirnopedia.org/quest_event.php')
    
def scrapeen():
    return __scrape('https://fate-go.cirnopedia.org/quest_event_us.php')

def scrapeall():
    enlist = scrapeen()
    jplist = scrapejp()
    return (enlist, jplist, __merge(enlist, jplist))

def __scrape(url):
    eventlist = list()
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.findAll('table')
    for table in tables:
        body = table.find('tbody')
        rows = body.findAll('tr')
        for row in rows:
            eventdict = dict()
            datacells = row.findAll('td') # bannercell, servantcell, craftessencecell
            craftessencehtml = str(datacells[2])
            eventdict['craftessencelist'] = __craftessenceparse(BeautifulSoup(craftessencehtml, "html.parser"))
            servanthtml = str(datacells[1]).replace(craftessencehtml, '') # replace() because cells are nested
            eventdict['servantlist'] = __servantparse(BeautifulSoup(servanthtml, "html.parser"))
            bannerhtml = str(datacells[0]).replace(craftessencehtml, '').replace(servanthtml, '') # replace() because cells are nested
            eventdict['bannerdict'] = __bannerparse(BeautifulSoup(bannerhtml, "html.parser"))
            eventlist.append(eventdict)
    return eventlist

def __craftessenceparse(soup):
    craftessencedata = soup.findAll('a')
    craftessencelist = list()
    for craftessencedatum in craftessencedata:
        d = dict()
        d['img'] = 'https://fate-go.cirnopedia.org/' + craftessencedatum.find('span')['style'].split(',')[2].split("'")[1]
        d['name'] = craftessencedatum.find('ch1').decode_contents()
        d['rarity'] = craftessencedatum.find('ch3').decode_contents()
        d['desc'] = " ".join(craftessencedatum.find('ch2').decode_contents().split('<br/>'))
        craftessencelist.append(d)
    return craftessencelist

def __servantparse(soup):
    servantdata = soup.findAll('a')
    servantlist = list()
    for servantdatum in servantdata:
        d = dict()
        d['img'] = 'https://fate-go.cirnopedia.org/' + servantdatum.find('span')['style'].split(',')[2].split("'")[1]
        d['name'] = servantdatum.find('ch1').decode_contents()
        d['rarity'] = servantdatum.find('ch3').decode_contents()
        d['desc'] = " ".join(servantdatum.find('ch2').decode_contents().replace('<strong>', '').replace('</strong>', '').split('<br/>'))
        servantlist.append(d)
    return servantlist
    
def __bannerparse(soup):
    bannerdata = soup.find('td').decode_contents().split('<br/>')
    bannerdict = dict()
    bannerlink = soup.find('a')
    bannerdict['img'] = 'https://fate-go.cirnopedia.org/' + bannerlink.find('img')['src']
    bannerdict['name'] = bannerdata[1]
    bannerdict['time'] = bannerdata[2].strip() # MM/DD (Day) HH:MM to MM/DD (Day) HH:MM to TZ
    bannerdict['date'] = re.search('\d+', bannerdict['img']).group(0) # YYYYMMDD
    return bannerdict

def __merge(enlist, jplist):
    bothlist = list()
    return bothlist

if __name__ == "__main__":
    pass