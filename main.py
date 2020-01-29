import requests
import sys
import wget
import os.path
from bs4 import BeautifulSoup

def getSeason(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find("h1", class_="title animar").string
    results = soup.find(id='div_capitulos')
    if(results!=None):
        results = results.find_all('a')
        episodes = []
        i=1
        for result in results:
            episode_title = result.find('h2').string
            episode_link = 'https://www.cntv.cl/cntv/site/mm/'+result['data-iframe'].strip('<iframe src="https://www.cntv.cl/cntv/js-local/prontusPlayer/embed/index.html?&src=').strip('" frameborder="0" allowfullscreen ></iframe>').strip('&img')
            episodes.append({"number": str(i).zfill(2),"title": episode_title,"link": episode_link})
            i+=1
        tv_show = {"title": name,"episodes": episodes}
        return tv_show
    else:
        return None

def downloader(tv_show):
    if not os.path.exists(tv_show['title']+"/"+"Season "+tv_show['season']+"/"):
        os.makedirs(tv_show['title']+"/"+"Season "+tv_show['season']+"/")
    for episode in tv_show['episodes']:
        print("\n[!] Descargando el capítulo "+ str(episode['number']) + " : " + episode['title']+"\n")
        filename = tv_show['title']+"/"+"Season "+tv_show['season'] + "/"+tv_show['title']+" - s"+tv_show['season']+"e"+episode['number']+" - "+episode['title']+os.path.splitext(episode['link'])[1]
        wget.download(episode['link'],filename)

def main():
    arguments = sys.argv
    url = ""
    if(len(arguments)>1):
        tv_show = getSeason(arguments[1])
    else:
        url = input("Ingrese el link para descargar: ")
        tv_show = getSeason(url)
    new_name = input('El nombre de la serie es: ' + tv_show['title'] + ' ...Escriba para cambiar el nombre o deje en blanco: ')
    if(len(new_name)>0):
        tv_show['title'] = new_name
    tv_show['season']=str(input("Ingrese el numero de temporada: ")).zfill(2)
    
    downloader(tv_show)
    
if __name__ == "__main__":
    main()