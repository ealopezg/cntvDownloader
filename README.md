# A tool to download series and movies from the Consejo Nacional de Televisión website

A basic python scrapper tool to download series and movies from the CNTV (Consejo Nacional de Television or *National Television Council*) website. It receives the link from the tv show and asks for the name of the tvshow and the season number. It uses BeatifulSoup to scrap the website and wget to download the files.

## How to use it

Clone the repository
```
git clone https://github.com/ealopezg/cntvDownloader && cd cntvDownloader
```
Install the requerimients using [Pipenv](https://github.com/pypa/pipenv)
```
pipenv install
```

Then run the program using first argument the URL of the tv show or movie
```
pipenv run src/cntvdownloader.py URL
```

The program will start to download the tv show using a folder hierarchy (format also compatible with Kodi/Plex!!!!!)

## Testing as an API

Using a simple deploy in Heroku you can check operation of the scrapper, replace **URL** with the url of the movie/tvshow.
```
GET http://capintv.herokuapp.com/?url=URL
```
