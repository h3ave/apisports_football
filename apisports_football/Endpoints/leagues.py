from ..apiclient import ApiClient

from ..Models.Leagues.Leagues import Leagues
from ..Models.Leagues.Seasons import Seasons

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class _Leagues(ApiClient):
    async def get(
            self,
            id: int = None,
            name: str = None,
            country: str = None,
            code: str = None,
            season: int = None,
            team: int = None,
            type: Literal['league', 'cup'] = None,
            current: bool = None,
            search: str = None,
            last: int = None
    ) -> Leagues:
        """
        Get the list of available leagues and cups
        https://www.api-football.com/documentation-v3#tag/Leagues/operation/get-leagues

        :param int id: The id of the league
        :param str name: The name of the league
        :param str country: The country name of the league
        :param str code: The Alpha2 code of the country
        :param int season: The season of the league
        :param int team: The id of the team
        :param str type: The type of the league
        :param bool current: The current league only
        :param str search: The name or the country of the league
        :param int last: The X last leagues/cups added in the API
        """
        params = {
            'id': id,
            'name': name,
            'country': country,
            'code': code,
            'season': season,
            'team': team,
            'type': type,
            'current': current,
            'search': search,
            'last': last
        }
        response = await self._make_request('leagues', params=params)
        return Leagues.model_validate(response)

    async def seasons(self) -> Seasons:
        """
        Get the list of available seasons
        https://www.api-football.com/documentation-v3#tag/Leagues/operation/get-seasons
        """
        response = await self._make_request('leagues/seasons')
        return Seasons.model_validate(response)
