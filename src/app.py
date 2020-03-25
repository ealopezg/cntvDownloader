#!/usr/bin/env python
import scrapper
import os
from flask import Flask, request, jsonify,send_file


app = Flask(__name__,
        static_url_path='', 
            static_folder='static',)

@app.route('/')
def index():
    url = request.args.get("url", None)
    if url==None:
        return send_file("static/index.html")
    else:
        media =  scrapper.Scrapper.getMedia(url)
        if media == None:
            return "Bad request", 400
        else:
            return jsonify(media)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)