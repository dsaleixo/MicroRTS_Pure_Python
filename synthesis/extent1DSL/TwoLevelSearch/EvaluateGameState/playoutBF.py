

import time
from Game.GameState import GameState
from Game.PhysicalGameState import PhysicalGameState
from Game.PlayerAction import PlayerAction
from Game.Screen import ScreenMicroRTS
from Game.UnitTypeTable import UnitTypeTable
from ai.ai import AI
from ai.rush.CombatRush import CombatRush
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.behavioralFeature import BehavioralFeature


class PlayoutBF:


    def __init__(self,):
        pass
	
    def run(self, gs  : GameState , utt : UnitTypeTable,  player : int,  max_cycle :int,  ai0 : AI,  ai1 : AI,  show_screen : bool) -> tuple[float,BehavioralFeature]:
        eval : BehavioralFeature=  BehavioralFeature()
        ai1.resert()
        ai0.resert()
        gs2 : GameState =  gs.clone()
        if show_screen :
            screen = ScreenMicroRTS(gs2)
        show = True
        #itbroke : bool= False 
        
     
		
        while not gs2.gameover() and gs2.getTime()<max_cycle:
            if show and show_screen   :
                    screen.draw()
                    time.sleep(0.1) 
            aux_time = time.time()
            pa0 :  PlayerAction =ai0.getActions(gs2,player)
            stop = time.time()- aux_time
            if(stop>0.070):return (-1.0, BehavioralFeature())
            pa1 : PlayerAction=ai1.getActions( gs2,1-player)
            eval.evaluate(pa0, player)
            gs2.issueSafe(pa0)
            gs2.issueSafe(pa1)
             
            if show_screen:show = gs2.updateScream()
            
             
            gs2.cycle()
          
                
            
               
                
       
        r=0
        if gs2.winner()==player: r= 1
        elif gs2.winner()==-1:r= 0.5
  
        return  (r,eval)
        


    @staticmethod
    def test():
        utt = UnitTypeTable(2)
        pgs = PhysicalGameState.load("./maps/basesWorkers32x32A.xml",utt);
        #pgs = PhysicalGameState.load("../maps/mapadavid2.xml",utt);
        #pgs = PhysicalGameState.load("../maps/BWDistantResources32x32.xml",utt)
        gs = GameState(pgs,utt)
        
        ai0 = CombatRush(pgs,utt,"Light")
        ai1 = CombatRush(pgs,utt,"Heavy")
        sp = PlayoutBF()
        resp = sp.run(gs,utt,0,3000,ai1,ai0,True)
        print(resp[0],resp[1].toString())
      