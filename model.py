import json
from api_proxy import API_proxy

class Album:
    """ Contains details of the album related info"""
    def __init__(self, album_name, artist_name):
        self.album_name = album_name
        self.artist_name = artist_name

    def get_artist(self):
        """This function sets the artist name"""

        response = API_proxy(self.album_name)

        # Parse the response in to the Album object
        if response.status_code != 200:
            print("Status code", response.status_code)
            print("Error Respose")
        else:
            result = json.loads(response.text)
            self.artist_name = result['results']['albummatches']['album'][0]['artist']