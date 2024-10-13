from typing import List

from ..BaseModel import BaseResponseModel


class Timezone(BaseResponseModel):
    response: List[str]
