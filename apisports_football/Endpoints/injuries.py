from ..apiclient import ApiClient

from ..Models.Injuries.Injuries import Injuries


class _Injuries(ApiClient):
    async def get(
            self,
            league: int = None,
            season: int = None,
            fixture: int = None,
            team: int = None,
            player: int = None,
            date: str = None,
            ids: str = None,
            timezone: str = None
    ) -> Injuries:
        """
        Get the list of players not participating in the fixtures for various reasons such as suspended, injured for example
        https://www.api-football.com/documentation-v3#tag/Injuries/operation/get-injuries

        :param int league: The id of the league
        :param int season: The season of the league, required with `league`, `team` and `player` parameters
        :param int fixture: The id of the fixture
        :param int team: The id of the team
        :param int player: The id of the player
        :param str date: A valid date
        :param str ids: One or more fixture ids
        :param str timezone: A valid timezone from the endpoint `Timezone`
        """
        params = {
            'league': league,
            'season': season,
            'fixture': fixture,
            'team': team,
            'player': player,
            'date': date,
            'ids': ids,
            'timezone': timezone
        }
        response = await self._make_request('injuries', params=params)
        return Injuries.model_validate(response)
