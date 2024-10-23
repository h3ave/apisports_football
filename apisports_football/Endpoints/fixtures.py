from ..apiclient import ApiClient

from ..Models.Fixtures.Events import Events
from ..Models.Fixtures.Fixtures import Fixtures
from ..Models.Fixtures.Lineups import Lineups
from ..Models.Fixtures.Players import Players
from ..Models.Fixtures.Rounds import Rounds
from ..Models.Fixtures.Statistics import Statistics

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class _Fixtures(ApiClient):
    async def rounds(
            self,
            league: int = None,
            season: int = None,
            current: bool = None,
            dates: bool = None,
            timezone: str = None
    ) -> Rounds:
        """
        Get the rounds for a league or a cup
        https://www.api-football.com/documentation-v3#tag/Fixtures/operation/get-fixtures-rounds

        :param int league: The id of the league
        :param int season: The season of the league
        :param bool current: The current round only
        :param bool dates: Add the dates of each round in the response
        :param str timezone: A valid timezone from the endpoint `Timezone`
        """
        params = {
            'league': league,
            'season': season,
            'current': current,
            'dates': dates,
            'timezone': timezone
        }
        response = await self._make_request('fixtures/rounds', params=params)
        return Rounds.model_validate(response)

    async def get(
            self,
            id: int = None,
            ids: str = None,
            live: str = None,
            date: str = None,
            league: int = None,
            season: int = None,
            team: int = None,
            last: int = None,
            next: int = None,
            _from: str = None,
            to: str = None,
            round: str = None,
            status: str = None,
            venue: int = None,
            timezone: str = None
    ) -> Fixtures:
        """
        Get detail information about fixtures
        https://www.api-football.com/documentation-v3#tag/Fixtures/operation/get-fixtures

        :param int id: The id of the fixture
        :param str ids: One or more fixture ids
        :param str live: All or several leagues ids
        :param str date: A valid date
        :param int league: The id of the league
        :param int season: The season of the league
        :param int team: The id of the team
        :param int last: For the X last fixtures
        :param int next: For the X next fixtures
        :param str _from: A valid date
        :param str to: A valid date
        :param str round: The round of the fixture
        :param str status: One or more fixture status short
        :param int venue: The venue id of the fixture
        :param str timezone: A valid timezone from the endpoint `Timezone`
        """
        params = {
            'id': id,
            'ids': ids,
            'live': live,
            'date': date,
            'league': league,
            'season': season,
            'team': team,
            'last': last,
            'next': next,
            'from': _from,
            'to': to,
            'round': round,
            'status': status,
            'venue': venue,
            'timezone': timezone
        }
        response = await self._make_request('fixtures', params=params)
        return Fixtures.model_validate(response)

    async def headtohead(
            self,
            h2h: str,
            date: str = None,
            league: int = None,
            season: int = None,
            last: int = None,
            next: int = None,
            _from: str = None,
            to: str = None,
            status: str = None,
            venue: int = None,
            timezone: str = None
    ) -> Fixtures:
        """
        Get heads to heads between two teams
        https://www.api-football.com/documentation-v3#tag/Fixtures/operation/get-fixtures

        :param str h2h: The ids of the teams
        :param str date: A valid date
        :param int league: The id of the league
        :param int season: The season of the league
        :param int last: For the X last fixtures
        :param int next: For the X next fixtures
        :param str _from: A valid date
        :param str to: A valid date
        :param str status: One or more fixture status short
        :param int venue: The venue id of the fixture
        :param str timezone: A valid timezone from the endpoint `Timezone`
        """
        params = {
            'h2h': h2h,
            'date': date,
            'league': league,
            'season': season,
            'last': last,
            'next': next,
            'from': _from,
            'to': to,
            'status': status,
            'venue': venue,
            'timezone': timezone
        }
        response = await self._make_request('fixtures/headtohead', params=params)
        return Fixtures.model_validate(response)

    async def statistics(
            self,
            fixture: int,
            team: int = None,
            type: Literal[
                'Shots on Goal',
                'Shots off Goal',
                'Shots insidebox',
                'Shots outsidebox',
                'Total Shots',
                'Blocked Shots',
                'Fouls',
                'Corner Kicks',
                'Offsides',
                'Ball Possession',
                'Yellow Cards',
                'Red Cards',
                'Goalkeeper Saves',
                'Total passes',
                'Passes accurate',
                'Passes %',
                'expected_goals',
                'goals_prevented'
            ] = None,
            half: bool = None
    ) -> Statistics:
        """
        Get the statistics for one fixture
        https://www.api-football.com/documentation-v3#tag/Fixtures/operation/get-fixtures-statistics

        :param int fixture: The id of the fixture
        :param int team: The id of the team
        :param str type: The type of statistics
        :param bool half: Add the halftime statistics in the response
        """
        params = {
            'fixture': fixture,
            'team': team,
            'type': type,
            'half': half
        }
        response = await self._make_request('fixtures/statistics', params=params)
        return Statistics.model_validate(response)

    async def events(
            self,
            fixture: int = None,
            team: int = None,
            player: int = None,
            type: str = None,
    ) -> Events:
        """
        Get the events from a fixture
        https://www.api-football.com/documentation-v3#tag/Fixtures/operation/get-fixtures-events

        :param int fixture: The id of the fixture
        :param int team: The id of the team
        :param int player: The id of the player
        :param str type: The type
        """
        params = {
            'fixture': fixture,
            'team': team,
            'player': player,
            'type': type
        }
        response = await self._make_request('fixtures/events', params=params)
        return Events.model_validate(response)

    async def lineups(
            self,
            fixture: int = None,
            team: int = None,
            player: int = None,
            type: str = None,
    ) -> Lineups:
        """
        Get the lineups for a fixture
        https://www.api-football.com/documentation-v3#tag/Fixtures/operation/get-fixtures-lineups

        :param int fixture: The id of the fixture
        :param int team: The id of the team
        :param int player: The id of the player
        :param str type: The type
        """
        params = {
            'fixture': fixture,
            'team': team,
            'player': player,
            'type': type
        }
        response = await self._make_request('fixtures/lineups', params=params)
        return Lineups.model_validate(response)

    async def players(
            self,
            fixture: int,
            team: int = None
    ) -> Players:
        """
        Get the players statistics from one fixture
        https://www.api-football.com/documentation-v3#tag/Fixtures/operation/get-fixtures-players

        :param int fixture: The id of the fixture
        :param int team: The id of the team
        """
        params = {
            'fixture': fixture,
            'team': team
        }
        response = await self._make_request('fixtures/players', params=params)
        return Players.model_validate(response)
