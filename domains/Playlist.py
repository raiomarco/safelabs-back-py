from typing import Union, Optional
import httpx
from errors.ApiError import ApiError
from util.validator import validator
from modules.spotifyApi import spotify_client
import os


def get_temperature(city: Optional[str], lat: Optional[float], lon: Optional[float]) -> float:
    r = httpx.get(
        f"https://api.openweathermap.org/data/2.5/weather?units=metric{'&q=' + city if city != None else ''}&lat={lat}&lon={lon}&appid={os.environ['WEATHER_API_KEY']}")

    if r.status_code == 400:
        raise ApiError("Bad request")
    elif (r.status_code == 404):
        raise ApiError("City not found")
    elif (r.status_code != 200):
        raise ApiError("Something went wrong")

    return r.json()['main']['temp']


def get_songs(genre: str):
    r = spotify_client.get(
        f'https://api.spotify.com/v1/search?q=genre:"{genre}"&type=track')

    if (r.status_code != 200):
        raise ApiError("Something went wrong")

    return list(dict.fromkeys(
        list(map(lambda track: track['name'], r.json()['tracks']['items']))))


def get_playlist(city: Optional[str], lat: Optional[float], lon: Optional[float]) -> dict[str, Union[str, float, list[str]]]:
    city, lat, lon = validator(city, lat, lon)

    temperature = get_temperature(city, lat, lon)

    genre = "classical"
    if (temperature > 30):
        genre = "party"
    elif (temperature >= 15):
        genre = "pop"
    elif (temperature >= 10):
        genre = "rock"

    songs = get_songs(genre)

    return {'temperature': round(temperature), 'genre': genre, 'songs': songs}
