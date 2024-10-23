from ..apiclient import ApiClient

from ..Models.Odds.Bookmakers import Bookmakers
from ..Models.Odds.Odds import Odds
from ..Models.Odds.LiveBets import LiveBets
from ..Models.Odds.Mapping import Mapping


class _Odds(ApiClient):
    async def get(
            self,
            fixture: int = None,
            league: int = None,
            season: int = None,
            date: str = None,
            timezone: str = None,
            page: int = None,
            bookmaker: int = None,
            bet: int = None
    ) -> Odds:
        """
        Get odds from fixtures, leagues or date
        https://www.api-football.com/documentation-v3#tag/Odds-(Pre-Match)/operation/get-odds

        :param int fixture: The id of the fixture
        :param int league: The id of the league
        :param int season: The season of the league
        :param str date: A valid date.
        :param str timezone: A valid timezone from the endpoint `Timezone`
        :param int page: Use for the pagination
        :param int bookmaker: The id of the bookmaker
        :param int bet: The id of the bet
        """
        params = {
            'fixture': fixture,
            'league': league,
            'season': season,
            'date': date,
            'timezone': timezone,
            'page': page,
            'bookmaker': bookmaker,
            'bet': bet
        }
        response = await self._make_request('odds', params=params)
        return Odds.model_validate(response)

    async def mapping(
            self,
            page: int = None
    ) -> Mapping:
        """
        Get the list of available fixtures id for the endpoint odds
        https://www.api-football.com/documentation-v3#tag/Odds-(Pre-Match)/operation/get-odds-mapping

        :param int page: Use for the pagination
        """
        params = {'page': page}
        response = await self._make_request('odds/mapping', params=params)
        return Mapping.model_validate(response)

    async def bookmakers(
            self,
            id: int = None,
            search: str = None
    ) -> Bookmakers:
        """
        Get all available bookmakers
        https://www.api-football.com/documentation-v3#tag/Odds-(Pre-Match)/operation/get-bookmakers

        :param int id: The id of the bookmaker
        :param str search: The name of the bookmaker
        """
        params = {'id': id, 'search': search}
        response = await self._make_request('odds/bookmakers', params=params)
        return Bookmakers.model_validate(response)

    async def bets(
            self,
            id: int = None,
            search: str = None
    ) -> Bookmakers:
        """
        Get all available bets for pre-match odds
        https://www.api-football.com/documentation-v3#tag/Odds-(Pre-Match)/operation/get-bets
        """
        params = {'id': id, 'search': search}
        response = await self._make_request('odds/bets', params=params)
        return Bookmakers.model_validate(response)

    async def live(
            self,
            fixture: int = None,
            league: int = None,
            bet: int = None
    ):
        """
        This endpoint returns in-play odds for fixtures in progress
        https://www.api-football.com/documentation-v3#tag/Odds-(In-Play)/operation/get-odds-live

        :param int fixture: The id of the fixture
        :param int league: The id of the league
        :param int bet: The id of the bet
        """
        params = {
            'fixture': fixture,
            'league': league,
            'bet': bet
        }
        response = await self._make_request('odds/live', params=params)
        return response

    async def live_bets(
            self,
            id: int = None,
            search: str = None
    ) -> LiveBets:
        """
        Get all available bets for in-play odds
        https://www.api-football.com/documentation-v3#tag/Odds-(In-Play)/operation/get-bets

        :param int id: The id of the bet name
        :param str search: The name of the bet
        """
        params = {'id': id, 'search': search}
        response = await self._make_request('odds/live/bets', params=params)
        return LiveBets.model_validate(response)
