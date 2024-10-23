from ..apiclient import ApiClient

from ..Models.Players.Players import Players
from ..Models.Players.Profiles import Profiles
from ..Models.Players.Teams import Teams
from ..Models.Leagues.Seasons import Seasons
from ..Models.Players.Squads import Squads

class _Players(ApiClient):
    async def teams(self, player: int) -> Teams:
        """
        Returns the list of teams and seasons in which the player played during his career
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-teams

        :param int player: The id of the player
        """
        params = {'player': player}
        response = await self._make_request('players/teams', params=params)
        return Teams.model_validate(response)

    async def profiles(
            self,
            player: int = None,
            search: str = None,
            page: int = None
    ) -> Profiles:
        """
        Returns the list of all available players
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-profiles

        :param int player: The id of the player
        :param str search: The lastname of the player
        :param int page: Use for the pagination
        """
        params = {'player': player, 'search': search, 'page': page}
        response = await self._make_request('players/profiles', params=params)
        return Profiles.model_validate(response)
    async def seasons(self, player: int = None) -> Seasons:
        """
        Get all available seasons for players statistics
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-seasons

        :param int player: The id of the player
        """
        params = {'player': player}
        response = await self._make_request('players/seasons', params=params)
        return Seasons.model_validate(response)

    async def get(
            self,
            id: int = None,
            team: int = None,
            league: int = None,
            season: int = None,
            search: str = None,
            page: int = None
    ) -> Players:
        """
        Get players statistics
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players

        :param int id: The id of the player
        :param int team: The id of the team
        :param int league: The id of the league
        :param int season: The season of the player
        :param str search: The name of the player
        :param int page: Use for the pagination
        """
        params = {
            'id': id,
            'team': team,
            'league': league,
            'season': season,
            'search': search,
            'page': page
        }
        response = await self._make_request('players', params=params)
        return Players.model_validate(response)

    async def squads(
            self,
            team: int = None,
            player: int = None
    ) -> Squads:
        """
        Return the current squad of a team when the `team` parameter is used.
        When the `player` parameter is used the endpoint returns the set of teams associated with the player
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-squads

        :param int team: The id of the team
        :param int player: The id of the player
        """
        params = {'team': team, 'player': player}
        response = await self._make_request('players/squads', params=params)
        return Squads.model_validate(response)

    async def topscorers(
            self,
            league: int,
            season: int
    ) -> Players:
        """
        Get the 20 best players for a league or cup
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-topscorers

        :param int league: The id of the league
        :param int season: The season of the league
        """
        params = {'league': league, 'season': season}
        response = await self._make_request('players/topscorers', params=params)
        return Players.model_validate(response)

    async def topassists(
            self,
            league: int,
            season: int
    ) -> Players:
        """
        Get the 20 best players assists for a league or cup
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-topassists

        :param int league: The id of the league
        :param int season: The season of the league
        """
        params = {'league': league, 'season': season}
        response = await self._make_request('players/topassists', params=params)
        return Players.model_validate(response)

    async def topyellowcards(
            self,
            league: int,
            season: int
    ) -> Players:
        """
        Get the 20 players with the most yellow cards for a league or cup
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-topassists

        :param int league: The id of the league
        :param int season: The season of the league
        """
        params = {'league': league, 'season': season}
        response = await self._make_request('players/topyellowcards', params=params)
        return Players.model_validate(response)

    async def topredcards(
            self,
            league: int,
            season: int
    ) -> Players:
        """
        Get the 20 players with the most red cards for a league or cup
        https://www.api-football.com/documentation-v3#tag/Players/operation/get-players-topredcards

        :param int league: The id of the league
        :param int season: The season of the league
        """
        params = {'league': league, 'season': season}
        response = await self._make_request('players/topredcards', params=params)
        return Players.model_validate(response)
