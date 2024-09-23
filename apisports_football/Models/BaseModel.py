from pydantic import BaseModel, RootModel
from typing import Dict, List, Union


class Parameters(RootModel):
    root: Union[Dict[str, Union[str, int]], List]


class Errors(RootModel):
    root: Union[Dict, List]


class Paging(BaseModel):
    current: int
    total: int


class BaseResponseModel(BaseModel):
    get: str
    parameters: Parameters
    errors: Union[List[Errors], None]
    results: int
    paging: Paging
