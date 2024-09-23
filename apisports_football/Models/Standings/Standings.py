from typing import Dict, List, Union
from pydantic import BaseModel, Field

from ..BaseModel import BaseResponseModel

from ..Fixtures.Fixtures import League, Team


class Goals(BaseModel):
    for_: int = Field(alias='for')
    against: int


class StandingInfo(BaseModel):
    played: int
    win: int
    draw: int
    lose: int
    goals: Goals


class Standing(BaseModel):
    rank: int
    team: Team
    points: int
    goalsDiff: int
    group: str
    form: str
    status: Union[str, None]
    description: Union[str, None]
    all: StandingInfo
    home: StandingInfo
    away: StandingInfo
    update: str


class _League(League):
    standings: List[List[Standing]]


class Standings(BaseResponseModel):
    response: List[Dict[str, _League]]
