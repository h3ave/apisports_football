from typing import Dict, List
from pydantic import BaseModel, Field

from ..BaseModel import BaseResponseModel

from ..Fixtures.Fixtures import FixtureInfo


class Tavers(BaseModel):
    total: int
    average: str


class Last_5_Goals(BaseModel):
    for_: Tavers
    against: Tavers


class Last_5(BaseModel):
    played: int
    form: str
    att: str
    def_: str = Field(alias='def')
    goals: Last_5_Goals


class Team(BaseModel):
    id: int
    name: str
    logo: str
    last_5: Last_5 = Field(default=None)
    league: Dict = Field(default=None)


class Teams(BaseModel):
    home: str
    away: str


class Comparison(BaseModel):
    form: Teams  # use Teams class
    att: Teams
    def_: Teams = Field(alias='def')
    poisson_distribution: Teams
    h2h: Teams
    goals: Teams
    total: Teams


class Response(BaseModel):
    teams: Dict[str, Dict[str, str]] = {
        'home': Team,
        'away': Team
    }
    comparison: Comparison
    h2h: List[FixtureInfo]


class Predictions(BaseResponseModel):
    response: List[Response]
