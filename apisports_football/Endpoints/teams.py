from ..Models.Countries.Countries import Countries
from ..Models.Leagues.Seasons import Seasons
from ..Models.Teams.Statistics import Statistics
from ..Models.Teams.Teams import Teams

from ..apiclient import ApiClient


class _Teams(ApiClient):
    async def get(
            self,
            id: int = None,
            name: str = None,
            league: int = None,
            season: int = None,
            country: str = None,
            code: str = None,
            venue: int = None,
            search: str = None
    ) -> Teams:
        """
        Get the list of available teams
        https://www.api-football.com/documentation-v3#tag/Teams/operation/get-teams

        :param int id: The id of the team
        :param str name: The name of the team
        :param int league: The id of the league
        :param int season: The season of the league
        :param str country: The country name of the team
        :param str code: The code of the team
        :param int venue: The id of the venue
        :param str search: The name or the country of the team
        """
        params = {
            'id': id,
            'name': name,
            'league': league,
            'season': season,
            'country': country,
            'code': code,
            'venue': venue,
            'search': search
        }
        response = await self._make_request('teams', params=params)
        return Teams.model_validate(response)

    async def statistics(
            self,
            league: int,
            season: int,
            team: int,
            date: str = None
    ) -> Statistics:
        """
        Returns the statistics of a team in relation to a given competition and season
        https://www.api-football.com/documentation-v3#tag/Teams/operation/get-teams-statistics

        :param int league: The id of the league
        :param int season: The season of the league
        :param int team: The id of the team
        :param str date: The limit date
        """
        params = {
            'league': league,
            'season': season,
            'team': team,
            'date': date
        }
        response = await self._make_request('teams/statistics', params=params)
        return Statistics.model_validate(response)

    async def seasons(
            self,
            team: int
    ) -> Seasons:
        """
        Get the list of seasons available for a team
        https://www.api-football.com/documentation-v3#tag/Teams/operation/get-teams-seasons

        :param int team: The id of the team
        """
        params = {'team': team}
        response = await self._make_request('teams/seasons', params=params)
        return Seasons.model_validate(response)

    async def countries(
            self
    ) -> Countries:
        """
        Get the list of countries available for the teams endpoint
        https://www.api-football.com/documentation-v3#tag/Teams/operation/get-teams-countries
        """
        response = await self._make_request('teams/countries')
        return Countries.model_validate(response)
