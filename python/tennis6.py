# -*- coding: utf-8 -*-

class TennisGame6:
    SCORE_NAMES = {
        "Love": {"en": "Love", "fr": "Zéro"},
        "Fifteen": {"en": "Fifteen", "fr": "Quinze"},
        "Thirty": {"en": "Thirty", "fr": "Trente"},
        "Forty": {"en": "Forty", "fr": "Quarante"},
        "Deuce": {"en": "Deuce", "fr": "Égalité"},
        "All": {"en": "All", "fr": "Partout"},
        "Advantage": {"en": "Advantage", "fr": "Avantage"},
        "Win for": {"en": "Win for ", "fr": "Victoire pour "}
    }
    def __init__(self, player1Name, player2Name,lang):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1Score = 0
        self.player2Score = 0
        self.lang = lang  # Nouveau: Choix de la langue

    def translate(self, term):
        # Retourne la traduction du terme dans la langue choisie
        return self.SCORE_NAMES[term][self.lang]

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
            return self.translate(self._score_to_string(self.player1Score)) + "-" + self.translate("All")
        else:
            return self.translate("Deuce")

    def _end_game_score(self):
        score_diff = self.player1Score - self.player2Score
        if abs(score_diff) == 1:
            leader = self.player1Name if score_diff == 1 else self.player2Name
            return self.translate("Advantage") + leader
        else:
            winner = self.player1Name if score_diff >= 2 else self.player2Name
            return self.translate("Win for") + winner

    def _regular_score(self):
       return self.translate(self._score_to_string(self.player1Score)) + "-" + self.translate(self._score_to_string(self.player2Score))

    def winning_player(self):
        if self.player1Score >= 4 and self.player1Score - self.player2Score >= 2:
            return self.player1Name
        elif self.player2Score >= 4 and self.player2Score - self.player1Score >= 2:
            return self.player2Name
        else:
            return None

    @staticmethod
    def _score_to_string(score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"


