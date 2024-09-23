from typing import List

from ..BaseModel import BaseResponseModel


class Rounds(BaseResponseModel):
    response: List[str]
