from typing import List, Optional, Union
from pydantic import BaseModel, Field

from .Events import _Events
from .Lineups import Lineup
from ..BaseModel import BaseResponseModel


class FixtureStatus(BaseModel):
    long: str
    short: Optional[str] = Field(default=None)
    elapsed: Union[int, None]
    extra: Optional[Union[int, None]] = Field(default=None)
    seconds: Optional[str] = Field(default=None)


class FixturePeriods(BaseModel):
    first: Union[int, None]
    second: Union[int, None]


class FixtureVenue(BaseModel):
    id: Union[int, None]
    name: Union[str, None]
    city: Union[str, None]


class Fixture(BaseModel):
    id: int
    referee: Optional[Union[str, None]] = Field(default=None)
    timezone: Optional[str] = Field(default=None)
    date: Optional[str] = Field(default=None)
    timestamp: Optional[int] = Field(default=None)
    periods: Optional[FixturePeriods] = Field(default=None)
    venue: Optional[FixtureVenue] = Field(default=None)
    status: Optional[FixtureStatus] = Field(default=None)


class League(BaseModel):
    id: int
    name: Optional[str] = Field(default=None)
    type: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    logo: Optional[Union[str, None]] = Field(default=None)
    flag: Optional[Union[str, None]] = Field(default=None)
    season: Optional[int] = Field(default=None)
    round: Optional[str] = Field(alias='round', default=None)


class Team(BaseModel):
    id: int
    name: str
    logo: Union[str, None]
    winner: Optional[bool] = Field(default=None)


class Teams(BaseModel):
    home: Team
    away: Team


class Goals(BaseModel):
    home: Union[int, None]
    away: Union[int, None]


class Score(BaseModel):
    halftime: Goals
    fulltime: Goals
    extratime: Goals
    penalty: Goals


class Player(BaseModel):
    id: int
    name: str


class EventsTime(BaseModel):
    elapsed: Union[int, None]
    extra: Union[int, None]


class Paging(BaseModel):
    current: int
    total: int


class Lineups(BaseModel):
    response: List[Lineup]


class FixtureInfo(BaseModel):
    fixture: Fixture
    league: League
    teams: Teams
    goals: Goals
    score: Score
    events: Optional[List[_Events]] = Field(default=None)
    lineups: Optional[List[Lineup]] = Field(default=None)
    statistics: Optional[List] = Field(default=None)
    players: Optional[List] = Field(default=None)


class Fixtures(BaseResponseModel):
    response: List[FixtureInfo]
