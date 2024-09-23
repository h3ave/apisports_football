from typing import List

from ..BaseModel import BaseResponseModel

from ..Leagues.Leagues import Country


class Countries(BaseResponseModel):
    response: List[Country]
