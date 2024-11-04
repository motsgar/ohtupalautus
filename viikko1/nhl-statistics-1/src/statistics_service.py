from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    GOALS = 1
    ASSISTS = 2
    POINTS = 3

class StatisticsService:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_func(player):
            if sort_by == SortBy.GOALS:
                return player.goals
            elif sort_by == SortBy.ASSISTS:
                return player.assists
            return player.goals + player.assists
            
        
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_func
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
