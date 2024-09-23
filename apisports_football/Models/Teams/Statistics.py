from typing import Dict, List, Union
from pydantic import BaseModel, RootModel

from ..BaseModel import BaseResponseModel
from ..Players.Players import League, Team


class PlayedInfo(BaseModel):
    home: Union[int, str]
    away: Union[int, str]
    total: Union[int, str]


class PenaltyInfo(BaseModel):
    total: Union[int, None]
    percentage: Union[str, None]


class Penalty(BaseModel):
    scored: PenaltyInfo
    missed: PenaltyInfo
    total: int


class Lineup(BaseModel):
    formation: str
    played: int


class Card(RootModel):
    root: Dict[str, PenaltyInfo]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class Cards(BaseModel):
    yellow: Card
    red: Card


class Fixtures(BaseModel):
    played: PlayedInfo
    wins: PlayedInfo
    draws: PlayedInfo
    loses: PlayedInfo


class Response(BaseModel):
    league: League
    team: Team
    form: str
    fixtures: Fixtures
    goals: Dict
    biggest: Dict
    clean_sheet: PlayedInfo
    failed_to_score: PlayedInfo
    penalty: Penalty
    lineups: List[Lineup]
    cards: Cards


class Statistics(BaseResponseModel):
    response: Response
