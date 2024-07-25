

from Game.UnitTypeTable import UnitTypeTable
from Game.GameState import GameState
from Game.PhysicalGameState import PhysicalGameState
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.behavioralFeature import BehavioralFeature
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.evaluatorSP import EvaluatorSP
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.feature1 import Feature1
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.featureFactory1 import FeatureFactory1
from synthesis.extent1DSL.TwoLevelSearch.search.BehavioralCloning import BehavioralCloning
from synthesis.extent1DSL.TwoLevelSearch.search.TwoLevelsearch import TwoLevelsearch
from synthesis.extent1DSL.TwoLevelSearch.search.naiveSampling import NaiveSampling
from synthesis.extent1DSL.TwoLevelSearch.search.sketchSearch import SketchSearch
from synthesis.extent1DSL.extent1Main.empty_E1 import Empty_E1
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1


class TestSketchSearch:
    
    @staticmethod
    def test():
        l1 = NaiveSampling(0.3,0.3,0.6,3)
        clear =True
        jj  = S_E1( Empty_E1())
        T0 =2000 
        alpha = 0.9
        beta = 0.5
        cego = False,
        oraculo = Feature1(BehavioralFeature(1,5,0,0,0,1,0))
        ava = EvaluatorSP(1,FeatureFactory1())
        limite_tempo = 1200
        sa_act = True
        print(oraculo.toString())
        ss =SketchSearch(l1,clear,jj,T0,alpha,beta,cego,oraculo,ava,limite_tempo,sa_act)
        map = "./maps/basesWorkers32x32A.xml"
        utt = UnitTypeTable(2)
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        ss.run(gs,3000,0)
        

    @staticmethod
    def test0():
        l1 = NaiveSampling(0.3,0.3,0.6,3)
        clear =True
        jj  = S_E1( Empty_E1())
        T0 =2000 
        alpha = 0.9
        beta = 0.5
        cego = False,
        oraculo = Feature1(BehavioralFeature(1,5,0,0,0,1,0))
        ava = EvaluatorSP(1,FeatureFactory1())
        limite_tempo = 1200
        sa_act = True
        print(oraculo.toString())
        bc = BehavioralCloning(limite_tempo,T0,alpha,beta,True)
        #ss =SketchSearch(l1,clear,jj,T0,alpha,beta,cego,oraculo,ava,limite_tempo,sa_act)
        map = "./maps/basesWorkers32x32A.xml"
        utt = UnitTypeTable(2)
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        bc.run(gs,3000,jj,oraculo,ava,l1)
        #ss.run(gs,3000,0)
    @staticmethod
    def test1():
        map = "./maps/basesWorkers32x32A.xml"
        utt = UnitTypeTable(2)
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        tl = TwoLevelsearch()
        tl.run(gs,3500)
        
        