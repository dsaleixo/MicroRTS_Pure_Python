
from Game.GameState import GameState
from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.evaluatorSP import EvaluatorSP
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.feature1 import Feature1
from synthesis.extent1DSL.TwoLevelSearch.search.naiveSampling import NaiveSampling
from synthesis.extent1DSL.TwoLevelSearch.search.sketchSearch import SketchSearch


class BehavioralCloning :


	

	

	
	
	
    def __init__(self, time0 : int, T0 : float,  alpha : float,  beta :float,  sa_act : bool) :
        self.SA_activation = sa_act # se colocar falso a busca vira HC
        print("Search CCB")
        self.limit_time=time0
        self.T0_initial = T0
        self.alpha_initial= alpha
        self.beta_initial = beta
        self.T0 = self.T0_initial
        self.alpha = self.alpha_initial
        self.beta = self.beta_initial


	
	
    def  run(self, gs : GameState,  max : int,  j :Node, feature : Feature1,  eval : EvaluatorSP, l1 : NaiveSampling) -> Node:
        self.resert()
        print("search "+feature.toString());
        se : SketchSearch =  SketchSearch(l1,True,j,self.T0,self.alpha,self.beta,False,feature,eval,self.limit_time,self.SA_activation);
        n : Node =se.run(gs, max, 0)
        return n
	
	

    def  resert(self) ->Node:
        self.T0 = self.T0_initial
        self.alpha = self.alpha_initial
        self.beta = self.beta_initial
	
	