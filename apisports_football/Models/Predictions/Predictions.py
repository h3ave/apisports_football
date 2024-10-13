from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

from ..BaseModel import BaseResponseModel

from ..Fixtures.Fixtures import FixtureInfo
from ..Leagues.Leagues import League

class Percent(BaseModel):
    home: str
    draw: Optional[str] = Field(default=None)
    away: str

class Goals(BaseModel):
    home: str
    away: str

class Last_Five_Goals(BaseModel):
    total: Union[float, int]
    average: Union[float, int]


class Last_Five(BaseModel):
    played: Optional[int] = Field(default=None)
    form: str
    att: str
    def_: str = Field(alias='def')
    goals: Dict[str, Last_Five_Goals]

class _Lineup(BaseModel):
    formation: str
    played: int

class _League(BaseModel):
    form: str
    fixtures: Dict
    goals: Dict
    biggest: Dict
    clean_sheet: Dict
    failed_to_score: Dict
    penalty: Optional[Dict] = Field(default=None)
    lineups: Optional[List[_Lineup]] = Field(default=None)
    cards: Optional[Dict] = Field(default=None)

class Team(BaseModel):
    id: int
    name: str
    logo: Optional[str] = Field(default=None)
    comment: Optional[Union[str, None]] = Field(default=None)
    last_5: Optional[Last_Five] = Field(default=None)
    league: Optional[_League] = Field(default=None)

class Prediction(BaseModel):
    winner: Team
    win_or_draw: bool
    under_over: Union[str, None]
    goals: Goals
    advice: str
    percent: Percent

class Comparison(BaseModel):
    form: Percent
    att: Percent
    def_: Percent = Field(alias='def')
    poisson_distribution: Percent
    h2h: Percent
    goals: Percent
    total: Percent

class Teams(BaseModel):
    home: Team
    away: Team

class Response(BaseModel):
    predictions: Prediction
    league: League
    teams: Teams
    comparison: Comparison
    h2h: List[FixtureInfo]


class Predictions(BaseResponseModel):
    response: List[Response]
