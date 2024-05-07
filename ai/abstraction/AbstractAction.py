
from Game.Unit import Unit
from Game.GameState import GameState
from Game.UnitAction import UnitAction
from Game.ResourceUsage import ResourceUsage


class AbstractAction:
    
    def __init__(self, u : Unit):
        self._unit :Unit = u
        
    def toString(self)->str:
        pass

    def  getUnit(self) -> Unit:
        return self._unit
    
    
    def setUnit(self, u : Unit) -> None:
        self._unit = u
    
    
    def completed(self, pgs : GameState) -> bool:
        pass
    
    
    def execute(self, pgs : GameState)->None:
        return self.execute(pgs,None)
    


    #def toxml(XMLWriter w);
    
    
    #def fromXML(Element e, PhysicalGameState gs, UnitTypeTable utt)
    
    
    
    def execute(self, pgs : GameState,  ru : ResourceUsage)->UnitAction:
        pass
        