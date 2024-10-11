import json
import os

from apisports_football.Models.Coachs.Coachs import Coachs
from apisports_football.Models.Countries.Countries import Countries
from apisports_football.Models.Fixtures.Events import Events
from apisports_football.Models.Fixtures.Fixtures import Fixtures
from apisports_football.Models.Fixtures.Lineups import Lineups
from apisports_football.Models.Fixtures.Players import Players as FixturesPlayers
from apisports_football.Models.Fixtures.Statistics import Statistics
from apisports_football.Models.Fixtures.Rounds import Rounds
from apisports_football.Models.Injuries.Injuries import Injuries
from apisports_football.Models.Leagues.Leagues import Leagues
from apisports_football.Models.Leagues.Seasons import Seasons
from apisports_football.Models.Odds.Odds import Odds
from apisports_football.Models.Odds.Bookmakers import Bookmakers
from apisports_football.Models.Odds.LiveBets import LiveBets
from apisports_football.Models.Odds.Mapping import Mapping
from apisports_football.Models.Players.Players import Players
from apisports_football.Models.Players.Profiles import Profiles
from apisports_football.Models.Players.Teams import Teams

API_RESPONSES_PATH = f'{os.getcwd()}/tests/data/api_responses'


class TestPydanticModels:
    def test_coachs(self):
        with open(f'{API_RESPONSES_PATH}/coachs.json') as file:
            json_data = json.load(file)
            Coachs.model_validate(json_data)

    def test_countries(self):
        with open(f'{API_RESPONSES_PATH}/countries.json') as file:
            json_data = json.load(file)
            Countries.model_validate(json_data)

    def test_fixtures_rounds(self):
        with open(f'{API_RESPONSES_PATH}/fixtures_rounds.json') as file:
            json_data = json.load(file)
            Rounds.model_validate(json_data)

    def test_fixtures(self):
        with open(f'{API_RESPONSES_PATH}/fixtures.json') as file:
            json_data = json.load(file)
            Fixtures.model_validate(json_data)

    def test_fixtures_headtohead(self):
        with open(f'{API_RESPONSES_PATH}/fixtures_headtohead.json') as file:
            json_data = json.load(file)
            Fixtures.model_validate(json_data)

    def test_fixtures_statistics(self):
        with open(f'{API_RESPONSES_PATH}/fixtures_statistics.json') as file:
            json_data = json.load(file)
            Statistics.model_validate(json_data)

    def test_fixtures_events(self):
        with open(f'{API_RESPONSES_PATH}/fixtures_events.json') as file:
            json_data = json.load(file)
            Events.model_validate(json_data)

    def test_fixtures_lineups(self):
        with open(f'{API_RESPONSES_PATH}/fixtures_lineups.json') as file:
            json_data = json.load(file)
            Lineups.model_validate(json_data)

    def test_fixtures_players(self):
        with open(f'{API_RESPONSES_PATH}/fixtures_players.json') as file:
            json_data = json.load(file)
            FixturesPlayers.model_validate(json_data)

    def test_injuries(self):
        with open(f'{API_RESPONSES_PATH}/injuries.json') as file:
            json_data = json.load(file)
            Injuries.model_validate(json_data)

    def test_leagues(self):
        with open(f'{API_RESPONSES_PATH}/leagues.json') as file:
            json_data = json.load(file)
            Leagues.model_validate(json_data)

    def test_leagues_seasons(self):
        with open(f'{API_RESPONSES_PATH}/leagues_seasons.json') as file:
            json_data = json.load(file)
            Seasons.model_validate(json_data)

    def test_odds(self):
        with open(f'{API_RESPONSES_PATH}/odds.json') as file:
            json_data = json.load(file)
            Odds.model_validate(json_data)

    def test_odds_bets(self):
        with open(f'{API_RESPONSES_PATH}/odds_bets.json') as file:
            json_data = json.load(file)
            Bookmakers.model_validate(json_data)

    def test_odds_bookmakers(self):
        with open(f'{API_RESPONSES_PATH}/odds_bookmakers.json') as file:
            json_data = json.load(file)
            Bookmakers.model_validate(json_data)

    def test_odds_live(self):
        with open(f'{API_RESPONSES_PATH}/odds_live.json') as file:
            json_data = json.load(file)
            ...

    def test_odds_live_bets(self):
        with open(f'{API_RESPONSES_PATH}/odds_live_bets.json') as file:
            json_data = json.load(file)
            LiveBets.model_validate(json_data)

    def test_odds_mapping(self):
        with open(f'{API_RESPONSES_PATH}/odds_mapping.json') as file:
            json_data = json.load(file)
            Mapping.model_validate(json_data)

    def test_players(self):
        with open(f'{API_RESPONSES_PATH}/players.json') as file:
            json_data = json.load(file)
            Players.model_validate(json_data)

    def test_players_profiles(self):
        with open(f'{API_RESPONSES_PATH}/players_profiles.json') as file:
            json_data = json.load(file)
            Profiles.model_validate(json_data)

    def test_players_teams(self):
        with open(f'{API_RESPONSES_PATH}/players_teams.json') as file:
            json_data = json.load(file)
            Teams.model_validate(json_data)
