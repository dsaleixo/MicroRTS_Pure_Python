
from Game.GameState import GameState
from Game.Unit import Unit
from synthesis.ai.Interpreter import Interpreter
from synthesis.baseDSL.mainBase.c import C, ChildC
from synthesis.baseDSL.mainBase.node import Node
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy


from synthesis.baseDSL.util.factory import Factory


class Idle(ChildC,Node):
    
    def __init__(self) -> None:
        self._used = False
        pass
        
    
        
    
    def translate(self) -> str:
        return "u.idle()"
    
    def translate2(self) -> str:
        return "u.idle()"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs +"u.idle()"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        
        pgs = gs.getPhysicalGameState()
		
        if u.getPlayer()==player  and automata._memory._freeUnit[u.getID()]  and u.getType().getCanAttack():
            print("sss")
            for  target in pgs.getUnits().values():
                if 1-player == target.getPlayer():
                    print("sss2")
                    dx = target.getX()-u.getX()
                    dy = target.getY()-u.getY()
                    d = (dx*dx+dy*dy)**0.5
                    if d<=u.getAttackRange() :
                       
                        self._used = True
                        automata._core.attack(u,target)
                        automata._memory._freeUnit[u.getID()] = False
                        
                        
    def load(self, l : list[str], f :Factory):
        pass
	

    def save(self, l : list[str]):
        l.append("Idle")
        
    def clone(self, f : Factory) -> Node:
        return f.build_Idle()
    
    def resert(self, f : Factory) -> None:
        self._used = False
        
    def clear(self,father:Node, f : Factory) -> Node:
        return self._used
	
