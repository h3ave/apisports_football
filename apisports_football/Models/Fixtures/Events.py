from pydantic import BaseModel
from typing import List, Union

from ..BaseModel import BaseResponseModel

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class Team(BaseModel):
    id: int
    name: str
    logo: Union[str, None]


class Player(BaseModel):
    id: Union[int, None]
    name: Union[str, None]


class EventsTime(BaseModel):
    elapsed: Union[int, None]
    extra: Union[int, None]


class _Events(BaseModel):
    time: EventsTime
    team: Team
    player: Player
    assist: Player
    type: Literal['Card', 'Goal', 'subst', 'Var', None]
    detail: str
    comments: Union[str, None]


class Events(BaseResponseModel):
    response: List[_Events]
