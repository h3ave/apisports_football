from typing import List
from pydantic import BaseModel

from .Odds import Bet
from ..Fixtures.Fixtures import Fixture, League

from ..BaseModel import BaseResponseModel


class Status(BaseModel):
    stopped: bool
    blocked: bool
    finished: bool


class Team(BaseModel):
    id: int
    goals: int


class Teams(BaseModel):
    home: Team
    away: Team


class Response(BaseModel):
    fixture: Fixture
    league: League
    teams: Teams
    status: Status
    update: str
    odds: List[Bet]


class Live(BaseResponseModel):
    response: List[Response]
