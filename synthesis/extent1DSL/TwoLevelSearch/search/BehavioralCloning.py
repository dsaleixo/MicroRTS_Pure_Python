
from Game.GameState import GameState
from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.evaluatorSP import EvaluatorSP
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.feature1 import Feature1
from synthesis.extent1DSL.TwoLevelSearch.search.naiveSampling import NaiveSampling
from synthesis.extent1DSL.TwoLevelSearch.search.sketchSearch import SketchSearch


class BehavioralCloning :


	

	

	
	
	
    def __init__(self, tempo : int, T0 : float,  alpha : float,  beta :float,  sa_act : bool) :
        self.SA_activation = sa_act
        print("Busca CCB")
        self.tempo_limite=tempo
        self.T0_inicial = T0
        self.alpha_inicial= alpha
        self.beta_inicial = beta
        self.T0 = self.T0_inicial
        self.alpha = self.alpha_inicial
        self.beta = self.beta_inicial


	
	
    def  run(self, gs : GameState,  max : int,  j :Node, nov : Feature1,  ava : EvaluatorSP, l1 : NaiveSampling) -> Node:
        self.resert()
        print("busca "+nov.toString());
        se : SketchSearch =  SketchSearch(l1,True,j,self.T0,self.alpha,self.beta,False,nov,ava,self.tempo_limite,self.SA_activation);
        n : Node =se.run(gs, max, 0)
        return n
	
	

    def  resert(self) ->Node:
        self.T0 = self.T0_inicial
        self.alpha = self.alpha_inicial
        self.beta = self.beta_inicial
	
	