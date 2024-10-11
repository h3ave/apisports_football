from pydantic import BaseModel, Field
from typing import List, Optional, Union

from ..BaseModel import BaseResponseModel


class Team(BaseModel):
    id: Union[int, None]
    name: Union[str, None]
    code: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    logo: Union[str, None]
    update: Optional[str] = Field(default=None)


class Player(BaseModel):
    id: int
    name: str
    photo: Union[str, None]


class Games(BaseModel):
    minutes: Union[int, None]
    number: Union[int, None]
    position: str
    rating: Union[str, None]
    captain: bool
    # substitute: bool


class Shots(BaseModel):
    total: Union[int, None]
    on: Union[int, None]


class Goals(BaseModel):
    total: Union[int, None]
    conceded: Union[int, None]
    assists: Union[int, None]
    saves: Union[int, None]


class Passes(BaseModel):
    total: Union[int, None]
    key: Union[int, None]
    accuracy: Union[int, str, None]


class Tackles(BaseModel):
    total: Union[int, None]
    blocks: Union[int, None]
    interceptions: Union[int, None]


class Duels(BaseModel):
    total: Union[int, None]
    won: Union[int, None]


class Dribbles(BaseModel):
    attempts: Union[int, None]
    success: Union[int, None]
    past: Union[int, None]


class Fouls(BaseModel):
    drawn: Union[int, None]
    committed: Union[int, None]


class Cards(BaseModel):
    yellow: Union[int, None]
    yellowred: Optional[Union[int, None]] = Field(default=None)
    red: Union[int, None]


class Penalty(BaseModel):
    won: Union[int, None]
    commited: Union[int, None]
    scored: Union[int, None]
    missed: Union[int, None]
    saved: Union[int, None]


class Statistics(BaseModel):
    games: Games
    offsides: Optional[Union[int, None]] = Field(default=None)
    shots: Shots
    goals: Goals
    passes: Passes
    tackles: Tackles
    duels: Duels
    dribbles: Dribbles
    fouls: Fouls
    cards: Cards
    penalty: Penalty


class Players(BaseModel):
    player: Player
    statistics: List[Statistics]


class Response(BaseModel):
    team: Team
    players: List[Players]


class Players(BaseResponseModel):
    response: List[Response]
