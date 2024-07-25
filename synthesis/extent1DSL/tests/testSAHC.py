
import time
from Game.GameState import GameState
from Game.PhysicalGameState import PhysicalGameState
from Game.UnitTypeTable import UnitTypeTable
from selfPlay.selfPlayDefault import SelfPlayDefault
from synthesis.baseDSL.mainBase.node import Node
from synthesis.baseDSL.tests.scriptsToy import ScriptsToy
from synthesis.extent1DSL.LocalSearch.HC import HC
from synthesis.extent1DSL.LocalSearch.SA import SA
from synthesis.extent1DSL.LocalSearch.individuals.individual_Default import Individual_Default
from synthesis.extent1DSL.mutation.mutation2 import Mutation2
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class TestSAHC:
    
    
    @staticmethod
    def test():
        map = "maps/basesWorkers32x32A.xml"
        utt : UnitTypeTable= UnitTypeTable(2)
        
        pgs : PhysicalGameState = PhysicalGameState.load(map ,utt)
        gs : GameState= GameState(pgs,utt)
        sp = SelfPlayDefault(1)
        s_empty :Node = ScriptsToy.scriptEmpty()
        
        sp.update(s_empty)
        max_tick = 3000
        f = Factory_E1()
        #search = HC()
        search = SA(2000,0.9,0.5)
        ind = Individual_Default( Mutation2())
        time0 =800
        start_time = time.time()
        while True:
            
            prog = sp.getIndividual().clone(f)
            r1 = sp.evaluate(prog,gs,max_tick )
            prog_result, r0, log = search.run(prog,gs,sp,ind,5,time0,max_tick)
            
            if r0 > r1:
                time_eval = time.time() - start_time
                log ="Camp\t"+str(time_eval)+"\t"+str(sp.getN())+"\t"+prog_result.translate()#+"\n"
                print(log)
                sp.update(prog_result.clone(f))