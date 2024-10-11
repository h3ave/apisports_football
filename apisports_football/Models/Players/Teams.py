from typing import List
from pydantic import BaseModel

from ..BaseModel import BaseResponseModel

from ..Fixtures.Players import Team


class Response(BaseModel):
    team: Team
    seasons: List[int]


class Teams(BaseResponseModel):
    response: List[Response]
