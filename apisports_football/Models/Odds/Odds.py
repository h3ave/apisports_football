from pydantic import BaseModel, Field
from typing import List, Optional, Union

from ..Fixtures.Fixtures import Fixture, League

from ..BaseModel import BaseResponseModel


class Value(BaseModel):
    value: Union[str, int]
    odd: str


class Bet(BaseModel):
    id: int
    name: str
    values: Optional[List[Value]] = Field(default=None)


class Bookmaker(BaseModel):
    id: int
    name: str
    bets: Optional[List[Bet]] = Field(default=None)


class Response(BaseModel):
    league: League
    fixture: Fixture
    update: str
    bookmakers: List[Bookmaker]


class Odds(BaseResponseModel):
    response: List[Response]
