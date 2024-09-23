from ..apiclient import ApiClient

from ..Models.Venues.Venues import Venues


class _Venues(ApiClient):
    async def get(
            self,
            id: int = None,
            name: str = None,
            city: str = None,
            country: str = None,
            search: str = None
    ) -> Venues:
        """
        Get the list of available venues
        https://www.api-football.com/documentation-v3#tag/Venues/operation/get-venues

        :param int id: The id of the venue
        :param str name: The name of the venue
        :param str city: The city name of the venue
        :param str country: The country name of the venue
        :param str search: The name, city or the country of the venue
        """
        params = {
            'id': id,
            'name': name,
            'city': city,
            'country': country,
            'search': search
        }
        response = await self._make_request('venues', params=params)
        return Venues.model_validate(response)
