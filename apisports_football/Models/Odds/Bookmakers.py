from typing import List

from ..BaseModel import BaseResponseModel

from .Odds import Bookmaker



class Bookmakers(BaseResponseModel):
    response: List[Bookmaker]
