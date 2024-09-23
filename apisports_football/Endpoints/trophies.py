from ..apiclient import ApiClient

from ..Models.Trophies.Trophies import Trophies


class _Trophies(ApiClient):
    async def get(
            self,
            player: int = None,
            coach: int = None,
    ) -> Trophies:
        """
        Get all available trophies for a player or a coach
        https://www.api-football.com/documentation-v3#tag/Trophies/operation/get-trophies

        :param int player: The id of the player
        :param int coach: The id of the coach
        """
        params = {'player': player, 'coach': coach}
        response = await self._make_request('trophies', params=params)
        return Trophies.model_validate(response)
