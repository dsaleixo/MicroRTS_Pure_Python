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
        self.ava=EvaluatorSP(3,FeatureFactory1()); # 1 = BestREsponde inf = FictionPlay, recomento usar 2 ou 3, mas para ser rapido mellhor deixar 1
        self.l1 = NaiveSampling(0.3,0.3,0.6,3) # para o level 1 da busca CMAB, ele gera um vetor de caracteristas
        #os paramentos são a probablidade de exploitar ou explorar
        self.l2 =  BehavioralCloning(1000,2000,0.9,0.5,True);#paramentos do SA,T0,alpha e beta

	
	
	    
    def run(self, gs : GameState, max :int) ->None:
        while(True):
            seed : tuple[Feature1, Node] = self.l1.getSeed(); #pega um vetor de caracteristisca
            print("Selecionado: "+seed[0].toString())
            oraculo = Feature1(BehavioralFeature(2,7,7,7,0,1,10))
            seed = (oraculo, self.l1.getScript(seed[0]))
            print("xxxxxxxxxxxxxxx")
            print(self.l1.imprimir())
            print("Selecionado: "+seed[0].toString())
            print("Script inicial "+seed[1].translate())# usando a memoria do NS iniciamos a busca com um script proximo
            c0 :Node = self.l2.run(gs, max, seed[1],seed[0], self.ava,self.l1); #realiza a busca para o vetor de caracterista
            self.ava.update(gs, max, c0)#tentamos atualizar o vetor de inimigos do SelfPlay usando o script encontrado
            print(self.l1.imprimir())
            #self.l1.toString2()
         
			
