from abc import ABC, abstractmethod

from MicroRTS_NB import GameState, PlayerAction

class AI(ABC):
    @abstractmethod
    def getActions(self, gs : GameState,player : int)->PlayerAction:
        pass
    
    @abstractmethod
    def resert(self)->None:
        pass
    
    