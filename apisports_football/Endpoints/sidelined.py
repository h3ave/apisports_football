from ..apiclient import ApiClient

from ..Models.Sidelined.Sidelined import Sidelined


class _Sidelined(ApiClient):
    async def get(
            self,
            player: int = None,
            coach: int = None,
    ) -> Sidelined:
        """
        Get all available sidelined for a player or a coach
        https://www.api-football.com/documentation-v3#tag/Sidelined/operation/get-sidelined

        :param int player: The id of the player
        :param int coach: The id of the coach
        """
        params = {
            'player': player,
            'coach': coach
        }
        response = await self._make_request('sidelined', params=params)
        return Sidelined.model_validate(response)
