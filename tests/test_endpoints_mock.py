import pytest
import os
import json

from aioresponses import aioresponses
from apisports_football.wrapper import Wrapper
from typing import List
from .utils import dict_to_query_params, get_api_method

API_RESPONSES_PATH = f'{os.getcwd()}/tests/data/api_responses'
BASE_URL = 'https://v3.football.api-sports.io'

METHODS = [file_name.replace('.json', '')
           for file_name in os.listdir(API_RESPONSES_PATH)]


@pytest.fixture
def api_wrapper():
    return Wrapper(api_key='demo')


@pytest.mark.asyncio
@pytest.mark.parametrize('method', METHODS)
async def test_endpoint(api_wrapper, method: str):
    with open(f'{API_RESPONSES_PATH}/{method}.json', mode='r') as file:
        expected_response = json.loads(file.read())
        params = expected_response['parameters']
        method_names = method.split('_')
        method = get_api_method(api_wrapper, method_names)

        query_params = dict_to_query_params(params)

        if isinstance(params, List):
            params = {}
            url = BASE_URL + f'/{"/".join(method_names)}'
        else:
            url = BASE_URL + f'/{"/".join(method_names)}?{query_params}'

        with aioresponses() as mock:
            mock.get(url=url, payload=expected_response, status=200)
            await method(**params)
