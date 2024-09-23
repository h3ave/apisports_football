from ..apiclient import ApiClient

from ..Models.Standings.Standings import Standings


class _Standings(ApiClient):
    async def get(
            self,
            season: int,
            league: int = None,
            team: int = None
    ) -> Standings:
        """
        Get the standings for a league or a team
        https://www.api-football.com/documentation-v3#tag/Standings/operation/get-standings

        :param int season: The season of the league
        :param int league: The id of the league
        :param int team: The id of the team
        """
        params = {
            'season': season,
            'league': league,
            'team': team
        }
        response = await self._make_request('standings', params=params)
        return Standings.model_validate(response)
