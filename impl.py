import json
from flask import Flask, request
from model import Album

app = Flask(__name__)


@app.route('/searchAlbum/')
def search_album():

    album_name = request.args.get('album')
    album = Album(album_name, "")

    #Get artist for the given album
    album.get_artist()

    # Send class object with album name and album artist
    return json.dumps(album.__dict__)

@app.route('/health')
def hello_world():
    return "It works"

if __name__ == '__main__':
   app.run()

