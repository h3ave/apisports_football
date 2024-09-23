from typing import List

from ..BaseModel import BaseResponseModel


class Timezones(BaseResponseModel):
    response: List[str]
