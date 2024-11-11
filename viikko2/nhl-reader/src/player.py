import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict["name"],
                            player_dict["nationality"],
                            player_dict["assists"],
                            player_dict["goals"],
                            player_dict["team"],
                            player_dict["games"])
            
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, playerReader):
        self.players = playerReader.get_players()

    def top_scorers_by_nationality(self, nationality):
        return [player for player in self.players if player.nationality == nationality]
    
    def get_available_nationalities(self):
        return sorted(set([player.nationality for player in self.players]))

class Player:
    def __init__(self, name, nationality, assists, goals, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
        self.games = games
        self.id = id
        
    
    def __str__(self):
        return f"{self.name:20} team {self.team:3} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"
