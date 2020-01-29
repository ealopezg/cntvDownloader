#!/usr/bin/env python
import sys
import os
import wget
import scrapper

def downloader(media):
    if media['type'] == 'tv_show' :
        if not os.path.exists(media['title']+"/"+"Season "+str(media['season']).zfill(2)+"/"):
            os.makedirs(media['title']+"/"+"Season "+str(media['season']).zfill(2)+"/")
        for episode in media['episodes']:
            print("\n[!] Downloading the episode "+ str(episode['number']) + " : " + episode['title']+"\n")
            filename = media['title']+"/"+"Season "+str(media['season']).zfill(2) + "/"+media['title']+" - s"+str(media['season']).zfill(2)+"e"+str(episode['number']).zfill(2)+" - "+episode['title']+os.path.splitext(episode['url'])[1]
            print(episode['url'])
            wget.download(episode['url'],filename)
    else:
        if not os.path.exists(media['title']+"/"):
            os.makedirs(media['title']+"/")
        print("\n[!] Downloading the movie "+ media['title']+"\n")
        filename = media['title']+"/"+media['title']+os.path.splitext(media['url'])[1]
        print(media['url'])
        wget.download(media['url'],filename)
    
            


def main():
    arguments = sys.argv
    url = ""
    if(len(arguments)>1):
        url = arguments[1]
    else:
        url = input("URL: ")

    media = scrapper.Scrapper.getMedia(url)
    downloader(media)
    
if __name__ == "__main__":
    main()