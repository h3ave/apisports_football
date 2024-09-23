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


class Statistics(BaseModel):
    type: Literal[
        'Shots on Goal',
        'Shots off Goal',
        'Shots insidebox',
        'Shots outsidebox',
        'Total Shots',
        'Blocked Shots',
        'Fouls',
        'Corner Kicks',
        'Offsides',
        'Ball Possession',
        'Yellow Cards',
        'Red Cards',
        'Goalkeeper Saves',
        'Total passes',
        'Passes accurate',
        'Passes %',
        'expected_goals',
        'goals_prevented'
    ]
    value: Union[int, Union[str, None]]


class Response(BaseModel):
    team: Team
    statistics: List[Statistics]


class Statistics(BaseResponseModel):
    response: List[Response]
