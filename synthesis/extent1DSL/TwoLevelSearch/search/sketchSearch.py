



from math import exp
from random import random
import time
from Game.GameState import GameState
from synthesis.baseDSL.mainBase.node import Node
from synthesis.baseDSL.util.control import Control
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.behavioralFeature import BehavioralFeature
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.evaluatorSP import EvaluatorSP
from synthesis.extent1DSL.extent1Main.empty_E1 import Empty_E1
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1
from synthesis.extent1DSL.mutation.mutation2 import Mutation2
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class SketchSearch :
    '''
	Factory f;
	boolean use_cleanr;
	boolean SA_activation;
	boolean cego;
	
	double T0;
	double alpha;
	double beta;
	Random r =new Random();
	Node_LS best;
	Pair<Double,Double> best_v;
	long time_ini;

	int limit_cloning;
	
	Feature  oracle;
	
	Evaluation ava;

	Level1 l1;
	'''

    def __init__(self, l1 , clear : bool, jj :Node, T0 : float, alpha : float,
									 beta : float, cego : bool,  oraculo : BehavioralFeature, 
									ava : EvaluatorSP, limite_tempo : int,  sa_act : bool):
        self.SA_activation = sa_act
        self.l1=l1
        self.f =  Factory_E1()
        self.use_cleanr = clear #limpar o script de comandos qeu não foram usados
        self.limit_cloning = limite_tempo
        self.T0=T0
        self.alpha = alpha
        self.beta= beta
        self.best = jj
        self.ava : EvaluatorSP=ava
        self.cego = cego
        self.r = random
        self.oracle=oraculo
        self.time_ini = time.time()
        self.best_v : tuple[float,float] = (-1000.0,-1000.0)
        self.mutation = Mutation2()
		
    def  if_best(self,v1 :tuple[float,float],  v2 : tuple[float,float]) -> bool:
        if v2[0]>v1[0]:return True
        aux = abs(v2[0] - v1[0]) <0.1
        if aux and v2[1] > v1[1]: return True
        return False

	
    def  accept(self, v1 :tuple[float,float], v2 :tuple[float,float],  temperatura :float) ->bool:
        if v2[0]>v1[0]:return True
        aux = abs(v2[0] - v1[0]) <0.1
        if aux :
			#np.exp(self.beta * (next_score - current_score)/self.current_temperature)
            aux2 = exp(self.beta*(v2[1] - v1[1])/temperatura)
            aux2 = min(1,aux2)
            if self.r()<aux2:return True
        return False;

	
	
    def  if_best2(self, v1 :tuple[float,float], v2 :tuple[float,float]) ->bool:
        if v2[1] > v1[1]: return True
        return False
	
    def accept2(self, v1 :tuple[float,float], v2 :tuple[float,float],  temperatura :float) ->bool:
        aux2 = exp(self.beta*(v2[1] - v1[1])/temperatura)
        aux2 = min(1,aux2)
        if self.r()<aux2:return True
        return False
    
    def stop(self,v1 :tuple[float,float] )->bool:
        return False
	
	
    def SearchSketch(self, gs : GameState,  max_cicle : int)->Node :
        atual =  S_E1( Empty_E1())
        v  : tuple[float,float]= (-1.0,-1.0)
        Tini = time.time()
        paraou = time.time()-Tini
        cont=0
        while paraou <(self.limit_cloning*0.1):
            print(paraou ,(self.limit_cloning*0.1))
            T = self.T0/(1+cont*self.alpha)
            best_neighbor = None 
            v_neighbor : tuple[float,float]=  (-1111.0,-1111.0)
            progs = self.mutation.getMutations(atual,5)
            for p in progs:  
                
                v2 = self.ava.evaluation(gs,max_cicle,p,self.oracle,self.l1)
                #print("\t"+str(v2[0])+" "+str(v2[1])+" "+p.translate())
                if self.if_best2(v_neighbor,v2):
                    if self.use_cleanr or True :p.clear(None, self.f)
                    best_neighbor = p.clone(self.f)
                    v_neighbor=v2
                paraou = time.time()-Tini
                if (paraou*1.0)/1000.0 >(self.limit_cloning)*0.1:
                    break
			
		
            if (self.accept2(v,v_neighbor,T) and self.SA_activation )or self.if_best2(self.best_v,v_neighbor):
                atual= best_neighbor.clone(self.f)
                v = v_neighbor
				
		
			#//System.out.println(v_neighbor.m_b+"   t\t"+best_neighbor.translate());
            paraou = time.time()-Tini
			
			
            if self.if_best2(self.best_v,v_neighbor):
                self.best =  best_neighbor.clone(self.f)
                self.best_v = v_neighbor
                paraou2 = time.time()-self.time_ini
                print("atual2\t"+str(paraou2*1.0)+"\t"+str(self.best_v[0])+"\t"+str(self.best_v[1])+"\t"+
						Control.save(self.best)+"\t")
				
				
			
            if self.ava.stoppingCriterion(self.best_v[0]) and False:
                this.best = best_neighbor.Clone(f)
                this.best_v = v_neighbor
                paraou2 = time.time()-this.time_ini
                #System.out.println("atual2\t"+((paraou2*1.0)/1000.0)+"\t"+best_v.m_a+"\t"+best_v.m_b+"\t"+
			    #			Control.salve(best)+"\t");
                break
            cont+=1
        return self.best

    def  SearchBR(self, gs : GameState,  max_cicle : int,  aux2 :Node) -> Node:
        atual : Node =   aux2.clone(self.f)
        v : tuple[float,float] = self.best_v
        Tini = time.time()
        paraou = time.time()-Tini;
        cont=0;
        print("ww")
        while (paraou*1.0) <300 and not self.ava.stoppingCriterion(v[0]):
            print(paraou ,(300))
            T = self.T0/(1+cont*self.alpha)
            best_neighbor = None 
            v_neighbor  : tuple[float,float]=(-1.0,-1.0)
            progs = self.mutation.getMutations(atual,5)
            for p in progs:  
                v2:  tuple[float,float] = self.ava.evaluation(gs, max_cicle,p,self.oracle,self.l1);
				#//System.out.println("\t"+v2.m_a+" "+v2.m_b+" "+aux.translate());
                if self.if_best(v_neighbor,v2):
                    if self.use_cleanr:p.clear(None, self.f)
                    best_neighbor =  p.clone(self.f);
                    v_neighbor=v2
                paraou = time.time()-Tini;
                if (paraou*1.0) >(self.limit_cloning)*1.0 or self.ava.stoppingCriterion(v_neighbor[0]):break
            
            
            
            if (self.accept(v,v_neighbor,T) and self.SA_activation) or self.if_best(self.best_v,v_neighbor):
                atual=best_neighbor.clone(self.f)
                v = v_neighbor
			#System.out.println(v_neighbor.m_b+"   t2\t"+best_neighbor.translate());
            paraou = time.time()-Tini
            if self.if_best(self.best_v,v_neighbor):
                self.best =  best_neighbor.clone(self.f)
                self.best_v = v_neighbor
                paraou2 = time.time()-self.time_ini
                print("atual2\t"+str(paraou2*1.0)+"\t"+str(self.best_v[0])+"\t"+str(self.best_v[1])+"\t"+
						Control.save(self.best)+"\t")
            if self.ava.stoppingCriterion(self.best_v[0]):
                self.best =  best_neighbor.clone(self.f);
                self.best_v = v_neighbor
                paraou2 = time.time()-self.time_ini
                print("atual2\t"+str(paraou2*1.0)+"\t"+str(self.best_v[0])+"\t"+str(self.best_v[1])+"\t"+
						Control.save(self.best)+"\t")
                break
            cont+=1
        return self.best;

    def  run(self, gs : GameState,  max_cicle : int, location :int)->Node:
        #paraou = time.time()-self.time_ini
        self.best_v = self.ava.evaluation(gs, max_cicle, self.best,self.oracle,self.l1)
        print("atual2\t0.0"+"\t"+str(self.best_v[0])+"\t"+str(self.best_v[1])+"\t"+
						Control.save(self.best)+"\t")
        print("SearchSketch")#eu separarei em dois codigos para facilitar a manutenção, mas diferença é que não primera busca
        # não olhamos o numero de vitorias apenas o quando é similar ao vetor de caracteristas
        n : Node=	self.SearchSketch(gs, max_cicle)
        print("SearchBR")#olhamos o numero de vitorias e depois no numero de caracteristas 
        
		#//l1.update(null, this.oraculo, this.best_v.m_a);
        return self.SearchBR(gs, max_cicle,n)

		
