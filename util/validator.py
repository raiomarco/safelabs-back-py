from typing import Tuple, Union, Optional
import urllib.parse
from errors.ValidatorError import ValidatorError


def validator(city: Optional[str], lat: Optional[float], lon: Optional[float]) -> Tuple[Union[str, None], Union[float, None], Union[float, None]]:
    if (city == None and (lat == None or lon == None)):
        raise ValidatorError("City or lat and lon are required")
    if (lat != None and lon != None):
        if (lat not in range(-90, 91) or lon not in range(-180, 181)):
            raise ValidatorError(
                "Lat must be in range [-90,90] and lon must be in range [-180,180]")

    return (urllib.parse.quote(city, safe='') if city != None else None, float(lat) if lat != None else None, float(lon) if lon != None else None)
