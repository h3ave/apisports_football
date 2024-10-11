from typing import List
from pydantic import BaseModel

from ..BaseModel import BaseResponseModel

from ..Players.Players import Player


class Response(BaseModel):
    player: Player


class Profiles(BaseResponseModel):
    response: List[Response]
