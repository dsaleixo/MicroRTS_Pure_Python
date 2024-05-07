import sys
sys.path.append("../..")

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

from Game.Screen import ScreenMicroRTS

import time

class Test2:


        @staticmethod
        def getMove(u : Unit, gs : GameState) -> UnitAction:
            a = Test2.getAttack(u,gs)
            if a !=None:
                return a
            pgs = gs.getPhysicalGameState()
            w  = pgs.getWidth()
            h = pgs.getHeight()
        
            pf  = AStarPathFinding(w,h)
            player_ad = 1 - u.getPlayer()
            u_ad = None
            for uu in pgs.getUnits().values():
                if uu.getPlayer() == player_ad and   uu.getType().getName() == "Base":
                    u_ad = uu
            if u_ad !=None:
                a = pf.findPathToPositionInRange(u, u_ad.getX()+u_ad.getY()*w,1, gs)
                print("ee",a.toString())
                print(u.toString(),u_ad.toString())
                return a
            return UnitAction.build_None()

        @staticmethod
        def getAttack(u : Unit, gs : GameState) -> UnitAction:
            a = None
            actions = u.getUnitActions(gs);
            for aa in actions:
                if aa.getActionName() == "attack_location":
                    return aa
            return a
        


        @staticmethod
        def getActionsSimples(gs : GameState, player :int ) -> PlayerAction:
            pgs = gs.getPhysicalGameState()
            pa = PlayerAction()

            for u in pgs.getUnits().values():
                
                if u.getPlayer()==player  and gs.getActionAssignment(u)==None and  u.getType().getName() == "Worker" :
                  
                   actions = u.getUnitActions(gs);
            
                   a = Test2.getMove(u,gs)
        
                   pa.addUnitAction(u,a)
            return pa
        

        @staticmethod
        def test(map):
            utt = UnitTypeTable(2);
            #pgs = PhysicalGameState.load("../maps/basesWorkers32x32A.xml",utt);
            #pgs = PhysicalGameState.load("../maps/mapadavid2.xml",utt);
            #pgs = PhysicalGameState.load("../maps/BWDistantResources32x32.xml",utt)
            pgs = PhysicalGameState.load(map,utt)
            gs = GameState(pgs,utt)
            screen = ScreenMicroRTS(gs)
            cont = 0
            show = True;
            while not gs.gameover() and cont<1000:
                print("time ",cont)   
                if show :
                    screen.draw()
                    time.sleep(0.2) 
                print("jogador0")
                
                pa0 = Test2.getActionsSimples(gs,0)
                
                for p0 in pa0.getActions():
                    print(p0[0].toString(),p0[1].toString())
                print("ww")
                print("jogador1")
                pa1 = Test2.getActionsSimples(gs,1)
                for p1 in pa1.getActions():
                    print(p1[0].toString(),p1[1].toString())
                show = gs.getTime()==gs.getNextChangeTime()
                
                gs.issueSafe(pa0)
                gs.issueSafe(pa1)
                
                
                
                gs.cycle()
                
                cont+=1;
            
                
                    
             
            print("winner = ", gs.winner())


                

        