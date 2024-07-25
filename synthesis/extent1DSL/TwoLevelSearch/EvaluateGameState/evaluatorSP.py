

import time
from Game.GameState import GameState
from ai.ai import AI
from synthesis.ai.Interpreter import Interpreter
from synthesis.baseDSL.mainBase.node import Node
from synthesis.baseDSL.util.control import Control
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.playoutBF import PlayoutBF
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.behavioralFeature import BehavioralFeature
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.feature1 import Feature1
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.featureFactory1 import FeatureFactory1
from synthesis.extent1DSL.TwoLevelSearch.search.naiveSampling import NaiveSampling
from synthesis.extent1DSL.extent1Main.empty_E1 import Empty_E1
from synthesis.extent1DSL.extent1Main.for_S_E1 import For_S_E1
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class EvaluatorSP:
	

    def __init__(self, n : int,  fabicaDeNovidade : FeatureFactory1):
        self.fn : FeatureFactory1 = fabicaDeNovidade
        print("N = "+str(n))
        self.playout =  PlayoutBF()
        self.f =  Factory_E1()
        self.n :int = n
        self.js : list[Node]= []
        self.best :float =0.5
        self.js.append( S_E1( Empty_E1()))
        print("Camp\t0.0"+"\t0"+"\t"+Control.save(self.js[0]) )
        self.budget : int =0
        self.time_ini=time.time()
        

    def evaluation(self, gs : GameState,  max : int,  j : Node,  oraculo :Feature1 = None, l1 : NaiveSampling=None) ->tuple[float,float]:
        utt = gs.getUnitTypeTable()
        pgs = gs.getPhysicalGameState()
        ai : AI =  Interpreter(pgs,utt,For_S_E1(j))
        r : tuple[float,float] = [0.0,0.0]
        nov : tuple[Feature1,Feature1]=[self.fn.create(),self.fn.create()]
        for adv in self.js:
            ai2 : AI =  Interpreter(pgs,utt,For_S_E1(adv))
            aux0 : tuple[float,BehavioralFeature] = self.playout.run(gs,utt, 0, max, ai, ai2, False);
            aux1 : tuple[float,BehavioralFeature] = self.playout.run(gs,utt, 1, max, ai, ai2, False);
          
            if aux0[0]+aux1[0]:
                self.budget+=1;
            if self.budget%50==0:
                paraou = time.time()-self.time_ini;
                print("Camp\t"+str(paraou)+"\t"+str(self.budget)+"\t"+
						Control.save(self.getBest()) )
            r[0]+=aux0[0] + aux1[0]
            if oraculo!=None:
                nov = (self.fn.create(aux0[1]),self.fn.create(aux1[1]))
        if r[0]>=0 and oraculo!=None :
            l1.update(j, nov[0], r[0]/(2*len(self.js)))
            l1.update(j, nov[0], r[0]/(2*len(self.js)))
        copia = -11
        if oraculo!=None:
            copia = oraculo.semelhaca(nov[0])+oraculo.semelhaca(nov[1]);
        
        return (r[0]/2,copia/2)

	

    def update(self, gs : GameState,  max:int,  j:Node) ->Node:
        paraou = time.time()-self.time_ini;
        camp=  j.clone(self.f)
        r =self.evaluation(gs,max,camp)[0]
        print("result "+str(paraou*1.0)+"     "+str(r)+ ">" + str(self.best)+" individuals = "+str(len(self.js)));
        if r> self.best:
            if len(self.js)>=self.n: self.js.pop(0);
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" )
            print("upgrade "+str(r)+ ">" + str(self.best)+" individuals = "+str(len(self.js)) )
            camp.clear(None, self.f);
            self.js.append( camp);
            self.best= self.evaluation(gs,max,camp)[0]
            print("Camp\t"+str(paraou)+"\t"+str(self.budget)+"\t"+
						Control.save(self.getBest()) )
	

    def getIndividuo(self) ->Node:
        return self.js(len(self.js)-1).Clone(self.f)

    def stoppingCriterion(self, d:float) ->bool:
        return d>len(self.js)-0.1
    

    def getBest(self)->None:
        return self.js[len(self.js)-1].clone(self.f)
