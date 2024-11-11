class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
    
    def __str__(self):
        return f"{self.name:20} team {self.team:3} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"
    

    @staticmethod
    def filter_players_by_nationality(players, nationality):
        return [player for player in players if player.nationality == nationality]