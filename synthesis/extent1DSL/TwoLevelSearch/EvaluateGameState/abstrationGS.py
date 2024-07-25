

from abc import ABC, abstractmethod

from Game import GameState



class AbtrationGS(ABC):

    @abstractmethod
    def evaluate(self, gs : GameState, play :int ):
        pass
    @abstractmethod
    def resert(self):
        pass
    