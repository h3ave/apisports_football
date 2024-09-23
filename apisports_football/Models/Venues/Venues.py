from typing import List, Optional, Union
from pydantic import BaseModel, Field

from ..BaseModel import BaseResponseModel


class Venue(BaseModel):
    id: int
    name: str
    address: Union[str, None]
    city: str
    country: Optional[str] = Field(default=None)
    capacity: int
    surface: str
    image: str


class Venues(BaseResponseModel):
    response: List[Venue]
