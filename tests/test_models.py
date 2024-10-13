import json
import os

from apisports_football.Models.Coachs.Coachs import Coachs
from apisports_football.Models.Countries.Countries import Countries
from apisports_football.Models.Fixtures.Events import Events
from apisports_football.Models.Fixtures.Fixtures import Fixtures
from apisports_football.Models.Fixtures.Lineups import Lineups
from apisports_football.Models.Fixtures.Players import Players as FixturesPlayers
from apisports_football.Models.Fixtures.Statistics import Statistics as FixturesStatistics
from apisports_football.Models.Fixtures.Rounds import Rounds
from apisports_football.Models.Injuries.Injuries import Injuries
from apisports_football.Models.Leagues.Leagues import Leagues
from apisports_football.Models.Leagues.Seasons import Seasons
from apisports_football.Models.Odds.Odds import Odds
from apisports_football.Models.Odds.Bookmakers import Bookmakers
from apisports_football.Models.Odds.Live import Live
from apisports_football.Models.Odds.LiveBets import LiveBets
from apisports_football.Models.Odds.Mapping import Mapping
from apisports_football.Models.Players.Players import Players
from apisports_football.Models.Players.Profiles import Profiles
from apisports_football.Models.Players.Squads import Squads
from apisports_football.Models.Players.Teams import Teams as PlayersTeams
from apisports_football.Models.Predictions.Predictions import Predictions
from apisports_football.Models.Sidelined.Sidelined import Sidelined
from apisports_football.Models.Standings.Standings import Standings
from apisports_football.Models.Teams.Statistics import Statistics as TeamsStatistics
from apisports_football.Models.Teams.Teams import Teams
from apisports_football.Models.Timezone.Timezone import Timezone
from apisports_football.Models.Transfers.Transfers import Transfers
from apisports_football.Models.Trophies.Trophies import Trophies
from apisports_football.Models.Venues.Venues import Venues

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
            FixturesStatistics.model_validate(json_data)

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
            Live.model_validate(json_data)

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
    
    def test_players_seasons(self):
        with open(f'{API_RESPONSES_PATH}/players_seasons.json') as file:
            json_data = json.load(file)
            Seasons.model_validate(json_data)
    
    def test_players_squads(self):
        with open(f'{API_RESPONSES_PATH}/players_squads.json') as file:
            json_data = json.load(file)
            Squads.model_validate(json_data)

    def test_players_teams(self):
        with open(f'{API_RESPONSES_PATH}/players_teams.json') as file:
            json_data = json.load(file)
            PlayersTeams.model_validate(json_data)
    
    def test_players_topassists(self):
        with open(f'{API_RESPONSES_PATH}/players_topassists.json') as file:
            json_data = json.load(file)
            Players.model_validate(json_data)
    
    def test_players_topredcards(self):
        with open(f'{API_RESPONSES_PATH}/players_topredcards.json') as file:
            json_data = json.load(file)
            Players.model_validate(json_data)
    
    def test_players_topscorers(self):
        with open(f'{API_RESPONSES_PATH}/players_topscorers.json') as file:
            json_data = json.load(file)
            Players.model_validate(json_data)
    
    def test_players_topyellowcards(self):
        with open(f'{API_RESPONSES_PATH}/players_topyellowcards.json') as file:
            json_data = json.load(file)
            Players.model_validate(json_data)
    
    def test_predictions(self):
        with open(f'{API_RESPONSES_PATH}/predictions.json') as file:
            json_data = json.load(file)
            Predictions.model_validate(json_data)

    def test_sidelined(self):
        with open(f'{API_RESPONSES_PATH}/sidelined.json') as file:
            json_data = json.load(file)
            Sidelined.model_validate(json_data)

    def test_standings(self):
        with open(f'{API_RESPONSES_PATH}/standings.json') as file:
            json_data = json.load(file)
            Standings.model_validate(json_data)

    def test_teams(self):
        with open(f'{API_RESPONSES_PATH}/teams.json') as file:
            json_data = json.load(file)
            Teams.model_validate(json_data)
    
    def test_teams_countries(self):
        with open(f'{API_RESPONSES_PATH}/teams_countries.json') as file:
            json_data = json.load(file)
            Countries.model_validate(json_data)
    
    def test_teams_seasons(self):
        with open(f'{API_RESPONSES_PATH}/teams_seasons.json') as file:
            json_data = json.load(file)
            Seasons.model_validate(json_data)

    def test_teams_statistics(self):
        with open(f'{API_RESPONSES_PATH}/teams_statistics.json') as file:
            json_data = json.load(file)
            TeamsStatistics.model_validate(json_data)

    def test_timezone(self):
        with open(f'{API_RESPONSES_PATH}/timezone.json') as file:
            json_data = json.load(file)
            Timezone.model_validate(json_data)

    def test_transfers(self):
        with open(f'{API_RESPONSES_PATH}/transfers.json') as file:
            json_data = json.load(file)
            Transfers.model_validate(json_data)
    
    def test_trophies(self):
        with open(f'{API_RESPONSES_PATH}/trophies.json') as file:
            json_data = json.load(file)
            Trophies.model_validate(json_data)

    def test_venues(self):
        with open(f'{API_RESPONSES_PATH}/venues.json') as file:
            json_data = json.load(file)
            Venues.model_validate(json_data)
