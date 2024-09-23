from ..apiclient import ApiClient

from ..Models.Transfers.Transfers import Transfers


class _Transfers(ApiClient):
    async def get(
            self,
            player: int = None,
            team: int = None,
    ) -> Transfers:
        """
        Get all available transfers for players and teams
        https://www.api-football.com/documentation-v3#tag/Transfers/operation/get-transfers

        :param int player: The id of the player
        :param int team: The id of the team
        """
        params = {'player': player, 'team': team}
        response = await self._make_request('transfers', params=params)
        return Transfers.model_validate(response)
