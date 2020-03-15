from item import Scissors
from item import Paper
from item import Rock
import random

class Game:
    def __init__(self):
        self.__currentScore = 0
        self.__player = None
        self.__opponent = None

    @property
    def currentScore(self):
        return self.__currentScore

    @property
    def player(self):
        return self.__player

    @property
    def opponent(self):
        return self.__opponent

    @property
    def isGameOn(self):
        return self.__currentScore < 3 and self.__currentScore > -3

    def fight(self):
        players = [Rock(), Paper(), Scissors()]
        self.__player = random.choice(players)
        self.__opponent = random.choice(players)
        result = self.__player.fight(self.__opponent)
        self.__currentScore += result
        return result
