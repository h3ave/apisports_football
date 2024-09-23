from typing import List, Union
from pydantic import BaseModel

from ..BaseModel import BaseResponseModel

from ..Fixtures.Fixtures import League


class Fixtures(BaseModel):
    events: bool
    lineups: bool
    statistics_fixtures: bool
    statistics_players: bool


class Coverage(BaseModel):
    fixtures: Fixtures
    standings: bool
    players: bool
    top_scorers: bool
    top_assists: bool
    top_cards: bool
    injuries: bool
    predictions: bool
    odds: bool


class Country(BaseModel):
    name: str
    code: Union[str, None]
    flag: Union[str, None]


class Season(BaseModel):
    year: int
    start: str
    end: str
    current: bool
    coverage: Coverage


class Response(BaseModel):
    league: League
    country: Country
    seasons: List[Season]


class Leagues(BaseResponseModel):
    response: List[Response]
