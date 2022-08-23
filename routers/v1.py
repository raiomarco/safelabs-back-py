from fastapi import APIRouter, Depends, Response, status
from typing import Union
from errors.ApiError import ApiError
from errors.ValidatorError import ValidatorError
from schemas.DataEntryModel import DataEntryModel
from schemas.PlaylistOutputModel import PlaylistOutputModel
from schemas.ErrorOutputModel import ErrorOutputModel
from domains.Playlist import get_playlist

router = APIRouter()


@router.get("/", responses={
    status.HTTP_200_OK: {"model": PlaylistOutputModel, "description": "Success"},
    status.HTTP_400_BAD_REQUEST: {"model": ErrorOutputModel, "description": "Bad Request"},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "model": ErrorOutputModel, "description": "Internal Server Error"}
})
async def create_playlist(response: Response, item: DataEntryModel = Depends()) -> Union[PlaylistOutputModel, ErrorOutputModel]:
    try:
        data = get_playlist(item.city, item.lat, item.lon)
        return PlaylistOutputModel(**data)
    except (ApiError, ValidatorError) as error:
        response.status_code = 400
        return ErrorOutputModel(status="error", error=str(error))
