from pydantic import BaseModel
from typing import List, Union

from ..BaseModel import BaseResponseModel

from ..Fixtures.Players import Team
from ..Players.Players import Player


class Career(BaseModel):
    team: Team
    start: str
    end: Union[str, None]


class Response(Player):
    team: Team
    career: List[Career]


class Coachs(BaseResponseModel):
    response: List[Response]
