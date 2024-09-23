from ..Models.Timezone.Timezones import Timezones

from ..apiclient import ApiClient


class _Timezone(ApiClient):
    async def get(self) -> Timezones:
        """
        Get the list of available timezone to be used in the fixtures endpoint
        https://www.api-football.com/documentation-v3#tag/Timezone/operation/get-timezone
        """
        response = await self._make_request('timezone')
        return Timezones.model_validate(response)
