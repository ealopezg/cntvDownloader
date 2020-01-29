#!/usr/bin/env python
import scrapper
import os
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    url = request.args.get("url", None)
    return jsonify(scrapper.Scrapper.getMedia(url))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)