from ..apiclient import ApiClient

from ..Models.Predictions.Predictions import Predictions


class _Predictions(ApiClient):
    async def get(self, fixture: int) -> Predictions:
        """
        Get predictions about a fixture
        https://www.api-football.com/documentation-v3#tag/Predictions/operation/get-predictions

        :param int fixture: The id of the fixture
        """
        params = {
            'fixture': fixture
        }
        response = await self._make_request('predictions', params=params)
        return Predictions.model_validate(response)
