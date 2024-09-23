from typing import List

from ..BaseModel import BaseResponseModel


class Seasons(BaseResponseModel):
    response: List[int]
