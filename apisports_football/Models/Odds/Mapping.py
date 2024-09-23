from typing import List
from pydantic import BaseModel

from ..Fixtures.Fixtures import Fixture, League

from ..BaseModel import BaseResponseModel

class Response(BaseModel):
    league: League
    fixture: Fixture
    update: str

class Mapping(BaseResponseModel):
    response: List[Response]
