from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name):
        self._name = name

    def fight(item):
        pass

    @property
    def name(self):
        return self._name

class Rock(Item):
    def __init__(self):
        self._name = "rock"

    def fight(self, item):
        if item.name == "rock":
            return 0
        if item.name == "scissors":
            return 1
        if item.name == "paper":
            return -1

class Scissors(Item):
    def __init__(self):
        self._name = "scissors"

    def fight(self, item):
        if item.name == "rock":
            return -1
        if item.name == "scissors":
            return 0
        if item.name == "paper":
            return 1


class Paper(Item):
    def __init__(self):
        self._name = "paper"

    def fight(self, item):
        if item.name == "rock":
            return 1
        if item.name == "scissors":
            return -1
        if item.name == "paper":
            return 0
