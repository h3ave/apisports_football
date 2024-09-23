from typing import List
from pydantic import BaseModel

from ..BaseModel import BaseResponseModel


class Response(BaseModel):
    type: str
    start: str
    end: str


class Sidelined(BaseResponseModel):
    response: List[Response]
