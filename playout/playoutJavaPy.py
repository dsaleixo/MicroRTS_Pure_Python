import jpype 
import jpype.imports
from jpype import *

from ai.rush.CombatRush import CombatRush
from huntingTerritory.GameStateJavaPy import GameStateJavaPy


class PlayoutJavaPy():
    def __init__(self):
        pass

    def playout(self,gs : GameStateJavaPy,aiJava,aiPy,playerJava,max_tick : int)->int:
        
        
        
           
            while not gs.gameOver() and gs.getTime()<max_tick:
                pa0 = aiJava.getAction(playerJava,gs.getGsJava())
                pa1 = aiPy.getActions(gs.getGsPy(),1-playerJava)
           
                gs.issueSafe(pa0,playerJava)
                gs.issueSafe(pa1,1-playerJava) 
            
                gs.cycle()
                gs.updateScreen()
                gs.isConsistent()
            return gs.winner()
    @staticmethod
    def test():   
        
        LightRushJ = jpype.JClass("ai.abstraction.LightRush");
        WorkerRushJ = jpype.JClass("ai.abstraction.WorkerRush");
        NaiveMCTS = jpype.JClass("ai.mcts.naivemcts.NaiveMCTS");
        SimpleSqrtEvaluationFunction3 = jpype.JClass("ai.evaluation.SimpleSqrtEvaluationFunction3");
        RandomBiasedAI = jpype.JClass("ai.RandomBiasedAI");
        map = "maps/basesWorkers32x32A.xml"
        gs = GameStateJavaPy(map,True,True)
        aiJ= NaiveMCTS(100, -1, 100,10,0.3, 1.0, 0.0, 1.0, 0.4, 1.0,  RandomBiasedAI(),  SimpleSqrtEvaluationFunction3(),False)
            #ai0 =  WorkerRushJ(gs.getUttJava());
        aiPy = CombatRush(gs.getPgsPy(), gs.getUttPy(), "Heavy") 
        playout = PlayoutJavaPy()
        playout.playout(gs,aiJ,aiPy,0,3000)