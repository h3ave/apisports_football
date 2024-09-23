from ..apiclient import ApiClient

from ..Models.Coachs.Coachs import Coachs


class _Coachs(ApiClient):
    async def get(
            self,
            id: int = None,
            team: int = None,
            search: str = None
    ) -> Coachs:
        """
        Get all the information about the coachs and their careers
        https://www.api-football.com/documentation-v3#tag/Coachs/operation/get-coachs

        :param int id: The id of the coach
        :param int team: The id of the team
        :param str search: The name of the coach
        """
        params = {
            'id': id,
            'team': team,
            'search': search
        }
        response = await self._make_request('coachs', params=params)
        return Coachs.model_validate(response)
