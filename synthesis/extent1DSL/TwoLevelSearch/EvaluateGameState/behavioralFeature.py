from __future__  import annotations

from Game.GameState import GameState
from Game.PhysicalGameState import PhysicalGameState
from Game.PlayerAction import PlayerAction
from Game.Unit import Unit
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.abstrationGS import AbtrationGS


class BehavioralFeature(AbtrationGS) :

	
	
    def __init__(self, w:int=0, l:int=0, r:int=0, h:int=0,  ba:int=0,  br:int=0,  re:int=0) :
        self._worker=w
        self._light=l
        self._ranged=r
        self._heavy=h
        self._base=ba
        self._barrack=br
        self._saved_resource=re
        
           
		
    def  toString(self) ->str:
        s : str = ""
        s+="Worker "+ str(self._worker) +" "
        s+="Light "+ str(self._light) +" "
        s+="Ranged "+ str(self._ranged) +" "
        s+="Heavy "+ str(self._heavy) +" "
        s+="Base "+ str(self._base) +" "
        s+="Barrack "+ str(self._barrack) +" "
        s+="Saved_resource "+ str(self._saved_resource) +" "
        return s
	

    def resert(self) ->None:
        self._worker=0
        self._light=0
        self._ranged=0
        self._heavy=0
        self._base=0
        self._barrack=0
        self._saved_resource=0


	
    def diffType(self, a : float, b : float) ->float:
        if a==0 and b==0: return 0
        delta : float =  abs( a-b)
        return delta /max(a,b)

	
	
    def evaluate(self,  pa : PlayerAction,  play : int )->None :
        
        for  actions in pa.getActions(): 
            if actions[1].getActionName() == "return":self._saved_resource+=1
            if actions[1].getActionName() == "produce" :
                if actions[1].getUnitType().getName() == "Worker": self._worker+=1
                if actions[1].getUnitType().getName() == "Light":self._light+=1
                if actions[1].getUnitType().getName() == "Heavy":self._heavy+=1
                if actions[1].getUnitType().getName() == "Base":self._base+=1
                if actions[1].getUnitType().getName() == "Barracks":self._barrack+=1
                if actions[1].getUnitType().getName() == "Ranged": self._ranged+=1
				
    def  getWorker(self)->int :
        return self._worker
    def setWorker(self, worker : int) ->None:
        self._worker = worker



    def  getLight(self) ->int:
        return self._light
    def setLight(self, light : int) ->None:
        self._light = light
    
        
    def  getRanged(self) ->int:
        return self._ranged
    def setRanged(self, ranged :int) ->None:
        self._ranged = ranged


    def getHeavy(self) ->int:
        return self._heavy
    
    def setHeavy(self, heavy :int) ->None:
        self._heavy = heavy

    def getBase(self) ->int:
        return self._base
    def setBase(self, base : int) ->None:
        self._base = base

    def  getBarrack(self) ->int:
        return self._barrack
    def setBarrack(self, barrack : int) ->None:
        self._barrack = barrack


    def getSaved_resource(self) ->int:
        return self._saved_resource
    def setSaved_resource(self, saved_resource : int) :
        self._saved_resource = saved_resource
