from pickle import FALSE
import sys

from Game.Screen import ScreenMicroRTS
sys.path.append("../..")
sys.path.append("../")
from xml.etree.ElementTree import tostring

from ai.abstraction.AbstractionLayerAI import AbstractionLayerAI
from ai.rush.CombatRush import CombatRush

from Game.UnitTypeTable import  UnitTypeTable
from Game.PhysicalGameState import PhysicalGameState
from Game.UnitType import UnitType
from Game.GameState import GameState
from Game.PlayerAction import PlayerAction
from Game.UnitAction import UnitAction
from Game.Unit import Unit
from Game.UnitActionAssignment import UnitActionAssignment
from Game.AStarPathFinding import AStarPathFinding


import random



import time



import psutil
class Test6:
        def __init__(self):
            pass 

        @staticmethod
        def test_aux0(self,map,utt):
            
            #pgs = PhysicalGameState.load("../maps/basesWorkers32x32A.xml",utt);
            #pgs = PhysicalGameState.load("../maps/mapadavid2.xml",utt);
            #pgs = PhysicalGameState.load("../maps/BWDistantResources32x32.xml",utt)
           
            pgs = PhysicalGameState.load(map,utt)
            gs = GameState(pgs,utt)
            ai0 = CombatRush(pgs,utt,"Light")
            ai1 = CombatRush(pgs,utt,"Heavy")
        @staticmethod
        def test_aux(gs,utt,exi):
        
            #pgs = PhysicalGameState.load("../maps/basesWorkers32x32A.xml",utt);
            #pgs = PhysicalGameState.load("../maps/mapadavid2.xml",utt);
            #pgs = PhysicalGameState.load("../maps/BWDistantResources32x32.xml",utt)
           
            
            #gs2 = gs
            
            gs2 = gs.clone()
            print("dd")
            pgs = gs2.getPhysicalGameState()
            ai0 = CombatRush(pgs,utt,"Light")
            ai1 = CombatRush(pgs,utt,"Heavy")
            if exi :
                screen = ScreenMicroRTS(gs2)
            cont = 0
            show = False;
            
            print(pgs.getWidth())
            while not gs2.gameover() and cont<3000:
          
                if show and exi   :
                    screen.draw()
                    time.sleep(0.1) 
                
                #print("jogador0")
           
         
                pa0 = ai0.getActions(gs2,0)
                #print("jogador1")
               
                
                   
                pa1 = ai1.getActions(gs2,1)
                
              
                show = gs2.updateScream()
              
                gs2.issueSafe(pa0)
        
                gs2.issueSafe(pa1)
                
                
                gs2.cycle()
          
                
                cont+=1;
            
            return " win ="+str( gs2.winner()) +" "+str(gs2.getTime())
           
            
            
        @staticmethod
        def test(map):
            utt = UnitTypeTable(2)
            
            pgs = PhysicalGameState.load(map,utt)
            print("dd")
            gs = GameState(pgs,utt)
            
          
            process = psutil.Process()
            ant = process.memory_info().rss/(1024*1024) # in bytes 
            ini = time.time()
            for i in range (10):
                
               
                ini0 = time.time()
                print(Test6.test_aux(gs, utt,False))
               
                fim = time.time()
            
                
                
                     
               
                

        