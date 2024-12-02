scoreNames = ["Love", "Fifteen", "Thirty", "Forty"]
tieNames = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
advantageNames = ["Advantage player1", "Advantage player2"]
winNames = ["Win for player1", "Win for player2"]

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return tieNames[self.player1_score] if self.player1_score < 3 else tieNames[-1]
        
        if self.player1_score >= 4 or self.player2_score >= 4:
            score_diff = self.player1_score - self.player2_score
            if score_diff == 1:
                return advantageNames[0]
            elif score_diff == -1:
                return advantageNames[1]
            elif score_diff >= 2:
                return winNames[0]
            else:
                return winNames[1]
        
        return f"{scoreNames[self.player1_score]}-{scoreNames[self.player2_score]}"
