

from random import random
from random import randint
import time

from synthesis.baseDSL.mainBase.node import Node
from synthesis.baseDSL.util.control import Control
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.behavioralFeature import BehavioralFeature
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.feature1 import Feature1
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.featureFactory1 import FeatureFactory1
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class NaiveSampling :
    '''
	int change_NS ;
	boolean salvar=true;
	Random r;
	double e0;
	double el;
	double eg;
	int n_arms=7;
	double desc= 0.95;
	int opt=13;
	long T_inicial;
	int[] v_opt = {0,1,2,3,4,5,7,10,15,20,25,35,50};
	String[] name_arm= {"W  ","L  ","R  ","H  ","Ba ","Br ","Re "};
	Map<Integer,Integer> map;
	
	Integer[][] TiVik;

	Double[][] MiVik;
	TreeMap<Feature,Integer> T;
	TreeMap<Feature,Double> M;
	TreeMap<Feature,String> Backup;
	FeatureFactory fn;
    '''
    def __init__(self,e0 : float,  el : float,  eg : float ,  troca :int) :
        self.n_arms : int=7
        self.desc : float= 0.95
        self.opt : int =13
     
        self.v_opt : list[int]= [0,1,2,3,4,5,7,10,15,20,25,35,50]
        self.name_arm  : list[str]= ["W  ","L  ","R  ","H  ","Ba ","Br ","Re "]
        self.change_NS = troca
        self.map : dict[int,int]= {}
        for i in range(self.opt):
            self.map[self.v_opt[i]]=i
        self.T_inicial = time.time()
   
        self.e0 = e0
        self.el = el
        self.eg = eg
        self.TiVik : list[list[int]]= []   #new Integer[this.n_arms][this.opt];
        self.MiVik : list[list[float]]= [] #= new Double[this.n_arms][this.opt];
        self.fn =  FeatureFactory1()
        for i in range(self.n_arms):
            self.TiVik.append([])
            self.MiVik.append([])
            for j in range(self.opt):
                self.TiVik[i].append(0)
                self.MiVik[i].append(None)
        self.T : dict[Feature1, int]=  {}
        self.M : dict[Feature1, int] = {}
        self.Backup : dict[Feature1, str] = {}
	
	



    def imprimir(self) -> str:
        s=""
        for i in range(self.n_arms):
            s += self.name_arm[i]
            for j in range(self.opt):
                s+=str(self.v_opt[j])+"("+str(self.MiVik[i][j])+","+str(self.TiVik[i][j])+")   "
            s+="\n"  
        s+="\n"
        best = self.exploitSA()
      
        if not best == None:
            s+="Mellhor: "+best.toString()+"\n"
        return s

    def toString2(self):
        for m in self.Backup.items():
            print(m[0].toString(),m[1])
        

    def  exploreX(self, i:int) ->int:
        aux :int  = randint(0,self.opt-1)
       
        return self.v_opt[aux]

    def  exploitX(self, i: int)->int :
        maior : float =-1111
        index : int=-1
        for j in range(self.opt):
            if self.TiVik[i][j]==0:continue
            if self.MiVik[i][j]>maior:
                maior= self.MiVik[i][j]
                index = j
        if index==-1:return self.exploreX(i)
        return self.v_opt[index];

    def  explore(self)->Feature1:
        l : list[int]=[]
        for i in range(self.n_arms):
            if(random()<self.el) :
                l.append(self.exploitX(i))
            else :
                l.append(self.exploreX(i))
        return self.fn.create( BehavioralFeature(l[0],l[1],l[2],l[3],l[4],l[5],l[6]))

	
    def  exploit(self) ->Feature1:
        if random()<self.eg and len(self.M)!=0:
            return self.exploitSA()
        else :
            return self.exploreSA();

    def  exploreSA(self)->Feature1: 
        aux : int = randint(len(self.M)-1)
        for nov in self.M.keys():
            if aux==0 :return nov
            aux-=1
        return None

    def  exploitSA(self) ->Feature1:
        nov : Feature1=None
        maior=-1111111
        for m in self.M.items():
            if m[1]>maior :
                nov = m[0]
                maior = m[1]
        return nov

    def  getScript(self, nov : Feature1) ->Node:
        maior =-1
        melhor="S;Empty";
        seed : Feature1= self.fn.create();
        print("guia "+nov.toString())
        for m in self.Backup.items():
	
			#//System.out.println("\t "+nov.semelhaca(m.getKey())+" "+m.getKey()+" "+ m.getValue());
            if nov.semelhaca(m[0])>maior :
                maior = nov.semelhaca(m[0])
                melhor = m[1]
                seed =m[0]
        print("Mais Proximo "+seed.toString(),melhor)
        return Control.load(melhor, Factory_E1())

	
    def getSeed(self)->tuple[Feature1, Node] :
        paraou = time.time()-self.T_inicial;
        if paraou*1.0 >self.change_NS*3600:
            self.e0 = 0.9
            self.el = 0.7
            self.eg = 0.9

        nov = None;
        if random() <self.e0 and len(self.T)!=0:
            nov= self.exploit()
        else:
            nov= self.explore()
        if len(self.T)!=0:self.desconto()
        return (nov,self.getScript(nov))


	
    def update(self, j : Node,  nov : Feature1,  reward : float) ->Node:
        l = self.converte(nov).v

        for i in range(self.n_arms):
            aux = self.map[l[i]];
            if self.TiVik[i][aux]==0:
                self.TiVik[i][aux]=1
                self.MiVik[i][aux]=reward
            else:
                self.MiVik[i][aux]=(self.MiVik[i][aux]*self.TiVik[i][aux]+reward)/(self.TiVik[i][aux]+1)
                self.TiVik[i][aux]+=1;
        if nov in self.T:
            T_aux=self.T[nov]
            M_aux= self.M[nov];
            aux = (M_aux*T_aux+reward)/(T_aux+1);
            self.T[nov] = 1+T_aux
            self.M[nov] = aux
        else :
            self.T[nov] = 1
            self.M[nov] = reward
        self.Backup[nov] =  Control.save(j)



    def getFN(self) ->FeatureFactory1:
        return self.fn
    def closestArm(self, i: int)->int:
        maior =10000;
        index=-1;
        for j in range(self.opt):
            aux = abs(i-self.v_opt[j])
            if aux<maior :
                maior=aux;
                index=j
        return self.v_opt[index];


    def  converte(self, nov : Feature1) ->Feature1:
        w = self.closestArm(nov.v[0])
        l = self.closestArm(nov.v[1])
        r =self.closestArm(nov.v[2])
        h =self.closestArm(nov.v[3])
        ba =self.closestArm(nov.v[4])
        br =self.closestArm(nov.v[5])
        re= self.closestArm(nov.v[6])
        return self.fn.create( BehavioralFeature(w,l,r,h,ba,br,re));
	
    def  desconto(self)->None: 
        for m in self.M.keys():
            self.M[m]=self.M[m]*self.desc
        for i in range(self.n_arms):
            for j in range(self.opt):
                if self.MiVik[i][j]!=None:
                    self.MiVik[i][j]=self.MiVik[i][j]*self.desc;
				


