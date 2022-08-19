from typing import Optional

from pydantic import BaseModel


class DataEntryModel(BaseModel):
    city: Optional[str]
    lat: Optional[float]
    lon: Optional[float]
