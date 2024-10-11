from pydantic import BaseModel
from typing import List

from ..BaseModel import BaseResponseModel

class Round(BaseModel):
    round: str
    dates: List[str]

class Rounds(BaseResponseModel):
    response: List[Round]
