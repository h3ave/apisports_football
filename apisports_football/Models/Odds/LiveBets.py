from pydantic import BaseModel
from typing import List

from ..BaseModel import BaseResponseModel

class Bet(BaseModel):
    id: int
    name: str

class LiveBets(BaseResponseModel):
    response: List[Bet]
