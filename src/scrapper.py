import requests
import json
from bs4 import BeautifulSoup

def getTitles(url):
    with open('video_library.json') as json_file:
        library = json.load(json_file)
        try:
            media = list(filter(lambda x:x["url"]==url,library))[0]
        except IndexError:
            media = None
    json_file.close()
    return media

class Scrapper(object):        
    @staticmethod
    def getMedia(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        media = getTitles(url)
        if media == None:
            media = {}
            media['title'] = soup.find("h1", class_="title animar").string
            media['type'] = "tv_show"
            media['season'] = 1
        results = soup.find(id='div_capitulos')
        if(results!=None):
            results = results.find_all('a')
            episodes = []
            i=1
            for result in results:
                episode_title = result.find('h2').string
                episode_url = 'https://www.cntv.cl/cntv/site/mm/'+result['data-iframe'].strip('<iframe src="https://www.cntv.cl/cntv/js-local/prontusPlayer/embed/index.html?&src=').strip('" frameborder="0" allowfullscreen ></iframe>').strip('&img')
                episodes.append({"number": str(i).zfill(2),"title": episode_title,"url": episode_url})
                i+=1
            if media['type']=="movie" :
                    del media['season']
                    media['url'] = episodes[0]['url']
                    media['type'] = media['type']
                    media['title'] = media['title']
                    
            else:
                media['episodes'] = episodes
                media['url'] = url
                media['type'] = media['type']
                media['season'] = media['season']
                media['title'] = media['title']
            return media
        else:
            return None
        
