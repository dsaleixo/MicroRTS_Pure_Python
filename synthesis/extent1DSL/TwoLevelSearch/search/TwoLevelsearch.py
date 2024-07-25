from Game.GameState import GameState
from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.behavioralFeature import BehavioralFeature
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.evaluatorSP import EvaluatorSP
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.feature1 import Feature1
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.featureFactory1 import FeatureFactory1
from synthesis.extent1DSL.TwoLevelSearch.search.BehavioralCloning import BehavioralCloning
from synthesis.extent1DSL.TwoLevelSearch.search.naiveSampling import NaiveSampling


class TwoLevelsearch:

	
    def __init__(self) :
        self.ava=EvaluatorSP(1,FeatureFactory1());
        self.l1 = NaiveSampling(0.3,0.3,0.6,3)
        self.l2 =  BehavioralCloning(1000,2000,0.9,0.5,True);

	
	
	    
    def run(self, gs : GameState, max :int) ->None:
        while(True):
            seed : tuple[Feature1, Node] = self.l1.getSeed();
            #oraculo = Feature1(BehavioralFeature(1,5,0,0,0,1,20))
            #seed = (oraculo, self.ava.getBest())
            print("xxxxxxxxxxxxxxx")
            print(self.l1.imprimir())
            print("Selecionado: "+seed[0].toString())
            print("Script inicial "+seed[1].translate())
            c0 :Node = self.l2.run(gs, max, seed[1],seed[0], self.ava,self.l1);
            self.ava.update(gs, max, c0)
            print(self.l1.imprimir())
            #self.l1.toString2()
         
			
