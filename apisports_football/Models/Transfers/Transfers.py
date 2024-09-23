from typing import List, Union
from pydantic import BaseModel, Field

from ..BaseModel import BaseResponseModel


class Player(BaseModel):
    id: int
    name: str


class Team(BaseModel):
    id: Union[int, None]
    name: Union[str, None]
    logo: Union[str, None]


class Teams(BaseModel):
    in_: Team = Field(alias='in')
    out: Team


class Transfer(BaseModel):
    date: str
    type: Union[str, None]
    teams: Teams


class Response(BaseModel):
    player: Player
    update: str
    transfers: List[Transfer]


class Transfers(BaseResponseModel):
    response: List[Response]
