from ..apiclient import ApiClient

from ..Models.Countries.Countries import Countries


class _Countries(ApiClient):
    async def get(
            self,
            name: str = None,
            code: str = None,
            search: str = None
    ) -> Countries:
        """
        Get the list of available countries for the `leagues` endpoint
        https://www.api-football.com/documentation-v3#tag/Countries/operation/get-countries

        :param str name: The name of the country
        :param str code: The Alpha2 code of the country
        :param str search: The name of the country
        """
        params = {
            'name': name,
            'code': code,
            'search': search
        }
        response = await self._make_request('countries', params=params)
        return Countries.model_validate(response)
