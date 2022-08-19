from typing import List

from pydantic import BaseModel


class PlaylistOutputModel(BaseModel):
    temperature: int
    genre: str
    songs: List[str]
