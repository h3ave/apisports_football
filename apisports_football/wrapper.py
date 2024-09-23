from .apiclient import ApiClient

from .Endpoints.coachs import _Coachs
from .Endpoints.countries import _Countries
from .Endpoints.fixtures import _Fixtures
from .Endpoints.injuries import _Injuries
from .Endpoints.leagues import _Leagues
from .Endpoints.odds import _Odds
from .Endpoints.players import _Players
from .Endpoints.predictions import _Predictions
from .Endpoints.sidelined import _Sidelined
from .Endpoints.standings import _Standings
from .Endpoints.teams import _Teams
from .Endpoints.timezone import _Timezone
from .Endpoints.transfers import _Transfers
from .Endpoints.trophies import _Trophies
from .Endpoints.venues import _Venues


class Wrapper(ApiClient):
    def coachs(self) -> _Coachs:
        return _Coachs(self.api_key)

    def countries(self) -> _Countries:
        return _Countries(self.api_key)

    def fixtures(self) -> _Fixtures:
        return _Fixtures(self.api_key)

    def injuries(self) -> _Injuries:
        return _Injuries(self.api_key)

    def leagues(self) -> _Leagues:
        return _Leagues(self.api_key)

    def odds(self) -> _Odds:
        return _Odds(self.api_key)

    def players(self) -> _Players:
        return _Players(self.api_key)

    def predictions(self) -> _Predictions:
        return _Predictions(self.api_key)

    def sidelined(self) -> _Sidelined:
        return _Sidelined(self.api_key)

    def standings(self) -> _Standings:
        return _Standings(self.api_key)

    def teams(self) -> _Teams:
        return _Teams(self.api_key)

    def timezone(self) -> _Timezone:
        return _Timezone(self.api_key)

    def transfers(self) -> _Transfers:
        return _Transfers(self.api_key)

    def trophies(self) -> _Trophies:
        return _Trophies(self.api_key)

    def venues(self) -> _Venues:
        return _Venues(self.api_key)
