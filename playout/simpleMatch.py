
from Game.GameState import GameState
import time
from Game.PlayerAction import PlayerAction
from Game.Screen import ScreenMicroRTS
from ai.ai import AI


class SimpleMatch:
    
    def playout(self,gs_a :GameState,ai0 : AI,ai1:AI,player :int,max_tick : int,show_scream:True)->int:
        gs = gs_a.clone()
        ai0.resert()
        ai1.resert()
        pgs = gs.getPhysicalGameState()
        gameover = False
    
        if show_scream :
            screen = ScreenMicroRTS(gs)
        show = True
        
        while not gs.gameover() and gs.getTime()<max_tick:
            if show and show_scream   :
                    screen.draw()
                    time.sleep(0.1) 

            aux_time = time.time()
            pa0 :  PlayerAction =ai0.getActions(gs,player)
            stop = time.time()- aux_time
            if(stop>0.070):return -1.0
            pa1 = ai1.getActions(gs,1 -player)
            if show_scream:show = gs.updateScream()
              
            gs.issueSafe(pa0)
            gs.issueSafe(pa1)      
            gs.cycle()
          
             
        return gs.winner()

            
