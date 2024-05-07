from platform import version
import sys
sys.path.append("../")
from Game.Screen import ScreenMicroRTS
from Game.GameState import GameState

from Game.PhysicalGameState import PhysicalGameState


from Game.UnitTypeTable import UnitTypeTable

import time

class Test0:
    
     @staticmethod
     def test(map):
         utt  = UnitTypeTable(version = 2)
         print(utt.getMoveConflictResolutionStrategy())
         pgs = PhysicalGameState.load(map,utt)
         gs = GameState(pgs,utt)
         screen = ScreenMicroRTS(gs)
         while True:
            screen.draw()
            print("qq")
            time.sleep(0.5) 
        
