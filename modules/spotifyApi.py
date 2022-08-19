import httpx
from httpx import Response, Request
from errors.ApiError import ApiError
import os

spotify_token = None


def update_spotify_token():
    global spotify_token

    r = httpx.post("https://accounts.spotify.com/api/token",
                   data={"grant_type": "client_credentials"},
                   auth=(os.environ['SPOTIFY_API_ID'], os.environ['SPOTIFY_API_SECRET']))
    spotify_token = r.json()["access_token"]


def apply_token(request: Request):
    global spotify_token

    if (spotify_token is None):
        update_spotify_token()

    request.headers["Authorization"] = f"Bearer {spotify_token}"


def check_token(response: Response):
    global spotify_token

    if response.status_code == 401:
        update_spotify_token()
        response.request
        response = httpx.request(response.request.method, response.request.url, headers={
            **response.request.headers, "Authorization": f"Bearer {spotify_token}"})


spotify_client = httpx.Client(
    event_hooks={'request': [apply_token], 'response': [check_token]})
