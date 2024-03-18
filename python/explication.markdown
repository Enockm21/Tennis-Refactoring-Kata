# Journal de bord Tennis Version 6


La fonction score de la version 6 est beaucoup trop longue et complexe, on a donc choisi de faire une modification majeure sur cette fonction ainsi que quelques détails mineurs sur d’autres parties du code.
Score(self) : Dans le code de base, la fonction score utilisait des instructions if, elif et else pour déterminer le type de score. Dans le code refactorisé, cette logique est déplacée sur d’autres fonctions pour améliorer la lisibilité et la maintenabilité. La nouvelle logique d’implémentation est l’ajout des fonctions _tie_score(self), _end_game_score(self) et regular_score(self) pour obtenir le score en fonction de la situation dans la partie en cours.
_tie_score(self) : Cette fonction gère le cas où les scores des deux joueurs sont égaux. Elle utilise la liste SCORE_NAMES pour obtenir les noms des scores éliminant ainsi la duplication dans le code
_end_game_score(self) : Cette fonction gère les cas où l’un des joueurs a atteint un score de fin de partie. Elle détermine si un joueur a un avantage ou s’il a remporté la partie en fonction de la différence de score.
_regular_score(self) : Cette fonction gère les cas où les scores des joueurs sont différents et qu’aucun n’a atteint un score de fin de partie. Elle utilise comme _tie_score(self) la liste SCORE_NAMES.



D’autres changements mineurs ont été apportés tels que des espaces autour de ‘==’ ou des accolades qui n’étaient pas nécessaires dans certaines conditions if.
