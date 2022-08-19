from typing import List

from pydantic import BaseModel


class ErrorOutputModel(BaseModel):
    status: str
    error: str
