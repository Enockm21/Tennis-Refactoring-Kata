import unittest

from tennis6 import TennisGame6


import os
class GoldenMasterTest(unittest.TestCase):

    DIR = "./golden-master"
    LANG = 'fr'

    @staticmethod
    def play_game(p1Points, p2Points, p1Name, p2Name,lang=LANG):
        game = TennisGame6(p1Name, p2Name,lang)
        for i in range(max(p1Points, p2Points)):
            if i < p1Points:
                game.won_point(p1Name)
            if i < p2Points:
                game.won_point(p2Name)
        return game.score()

    def make_file_name(self, score_player_1, score_player_2):
        return f"{self.DIR}/{self.LANG}/{score_player_1}_{score_player_2}.txt"

    def _test_record(self):
        for score_player_1 in list(range(0, 16)):
            for score_player_2 in list(range(0, 16)):
                with self.subTest(f"{score_player_1}, {score_player_2}"):
                    sortie = self.play_game(score_player_1, score_player_2, "player1", "player2")
                    file = open(self.make_file_name(score_player_1, score_player_2), "w")
                    file.writelines(sortie)
                    file.close()

    def test_replay(self):
        for score_player_1 in list(range(0, 16)):
            for score_player_2 in list(range(0, 16)):
                with self.subTest(f"{score_player_1}, {score_player_2}"):
                    sortie = self.play_game(score_player_1, score_player_2, "player1", "player2")
                    file = open(self.make_file_name(score_player_1, score_player_2), "r")
                    attendu = file.read()
                    file.close()
                    self.assertEqual(attendu, sortie)

