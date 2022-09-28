import os, requests

"""Load the Environment Variables"""
from dotenv import load_dotenv
load_dotenv()

"""This function is used for any API requests"""
def API_proxy(album_name):
    url = os.environ.get('url')
    api_key = os.environ.get('api_key')
    params = {"method":"album.search","album": album_name, "api_key":api_key,"format":"json"}
    response = requests.get(url, params=params)
    return response


