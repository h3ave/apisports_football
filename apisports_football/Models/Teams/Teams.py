from typing import List
from pydantic import BaseModel

from ..BaseModel import BaseResponseModel

from ..Players.Players import Team
from ..Venues.Venues import Venue


class Response(BaseModel):
    team: Team
    venue: Venue


class Teams(BaseResponseModel):
    response: List[Response]
