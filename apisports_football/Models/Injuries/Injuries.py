from pydantic import BaseModel
from typing import List, Union

from ..BaseModel import BaseResponseModel


class Player(BaseModel):
    id: int
    name: str
    photo: str
    type: str
    reason: str


class Team(BaseModel):
    id: int
    name: str
    logo: Union[str, None]


class Fixture(BaseModel):
    id: int
    timezone: str
    date: str
    timestamp: int


class League(BaseModel):
    id: int
    season: int
    name: str
    country: str
    logo: Union[str, None]
    flag: Union[str, None]


class Response(BaseModel):
    player: Player
    team: Team
    fixture: Fixture
    league: League


class Injuries(BaseResponseModel):
    response: List[Response]
