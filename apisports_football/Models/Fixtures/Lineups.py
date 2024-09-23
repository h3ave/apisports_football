from pydantic import BaseModel
from typing import List, Union

from ..BaseModel import BaseResponseModel


class Player(BaseModel):
    id: int
    name: str
    number: int
    pos: str
    grid: Union[str, None]


class LineupStartXI(BaseModel):
    player: Player


class Substitutes(BaseModel):
    player: Player


class Colors(BaseModel):
    primary: str
    number: str
    border: str


class PlayerColors(BaseModel):
    player: Colors
    goalkeeper: Colors


class Team(BaseModel):
    id: int
    name: str
    logo: Union[str, None]
    colors: PlayerColors


class Coach(BaseModel):
    id: int
    name: str
    photo: Union[str, None]


class Lineup(BaseModel):
    team: Team
    formation: str
    startXI: List[LineupStartXI]
    substitutes: List[Substitutes]
    coach: Coach


class Lineups(BaseResponseModel):
    response: List[Lineup]
