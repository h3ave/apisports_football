from typing import List, Optional, Union
from pydantic import BaseModel, Field

from ..BaseModel import BaseResponseModel

from ..Fixtures.Fixtures import League
from ..Fixtures.Players import Statistics, Team


class _Birth(BaseModel):
    date: Union[str, None]
    place: Union[str, None]
    country: Union[str, None]


class Player(BaseModel):
    id: int
    name: str
    firstname: Optional[str] = Field(default=None)
    lastname: Optional[str] = Field(default=None)
    age: Optional[int] = Field(default=None)
    birth: _Birth
    nationality: Optional[str] = Field(default=None)
    height: Union[str, None]
    weight: Union[str, None]
    number: Optional[Union[int, None]] = Field(default=None)
    position: Optional[Union[str, None]] = Field(default=None)
    injured: Optional[bool] = Field(default=None)
    photo: str


class Substitutes(BaseModel):
    in_: Union[int, None] = Field(alias='in')
    out: Union[int, None]
    bench: Union[int, None]


class _Statistics(Statistics):
    team: Team
    league: League
    substitutes: Substitutes


class Response(BaseModel):
    player: Player
    statistics: List[_Statistics]


class Players(BaseResponseModel):
    response: List[Response]
