from typing import List, Union
from pydantic import BaseModel

from ..BaseModel import BaseResponseModel

from ..Fixtures.Players import Team


class Player(BaseModel):
    id: int
    name: str
    age: Union[int, None]
    number: Union[int, None]
    position: str
    photo: str


class Response(BaseModel):
    team: Team
    players: List[Player]


class Squads(BaseResponseModel):
    response: List[Response]
