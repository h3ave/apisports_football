from typing import List
from pydantic import BaseModel

from ..BaseModel import BaseResponseModel


class Response(BaseModel):
    league: str
    country: str
    season: str
    place: str


class Trophies(BaseResponseModel):
    response: List[Response]
