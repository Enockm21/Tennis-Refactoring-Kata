# -*- coding: utf-8 -*-

class TennisGame6:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]  # Utilisation d'une liste SCORE_NAMES pour stocker les noms des scores, ce qui élimine la duplication de code.

    def init(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0

    def won_point(self, playerName):
        if playerName == "player1":
            self.player1Score += 1
        else:
            self.player2Score += 1

    def score(self):
        if self.player1Score == self.player2Score:
            return self._tie_score()
        elif self.player1Score >= 4 or self.player2Score >= 4:
            return self._end_game_score()
        else:
            return self._regular_score()

    def _tie_score(self):
        if self.player1Score < 3:
            return TennisGame6.SCORE_NAMES[self.player1Score] + "-All"
        else:
            return "Deuce"

    def _end_game_score(self):
        score_diff = self.player1Score - self.player2Score
        if abs(score_diff) == 1:
            leader = self.player1Name if score_diff == 1 else self.player2Name
            return "Advantage " + leader
        else:
            winner = self.player1Name if score_diff >= 2 else self.player2Name
            return "Win for " + winner

    def _regular_score(self):
        return TennisGame6.SCORE_NAMES[self.player1Score] + "-" + TennisGame6.SCORE_NAMES[self.player2Score]


tenis = TennisGame6("toto","tata")
tenis.won_point("titi")
tenis.won_point("toto")
tenis.won_point("toto")

print(tenis.score())
