import aiohttp
from .utils import prepare_params
from .exceptions import ApiError


class ApiClient:
    BASE_URL = 'https://v3.football.api-sports.io'
    BASE_HEADERS = {'x-rapidapi-host': BASE_URL, 'x-rapidapi-key': ''}

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.BASE_HEADERS['x-rapidapi-key'] = api_key

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        return None

    async def _make_request(self, endpoint: str, params: dict = None, **kwargs) -> dict:
        async with aiohttp.ClientSession(headers=self.BASE_HEADERS) as session:
            params = prepare_params(params=params)
            response = await session.request('GET', f'{self.BASE_URL}/{endpoint}', params=params, **kwargs)
            data = await response.json()
            if len(data.get('errors')) > 0:
                raise ApiError(data['errors'])
            return data