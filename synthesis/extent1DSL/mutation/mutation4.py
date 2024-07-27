from synthesis.baseDSL.mainBase.S import S
from synthesis.baseDSL.mainBase.c import C
from synthesis.baseDSL.mainBase.for_S import For_S
from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.extent1Main.c_E1 import C_E1
from synthesis.extent1DSL.extent1Main.for_S_E1 import For_S_E1
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1
from synthesis.extent1DSL.extent1Main.s_s_E1 import S_S_E1
from synthesis.extent1DSL.mutation.mutation import Mutation

from synthesis.extent1DSL.util.Factory_E1 import Factory_E1
import random

class Mutation4(Mutation):
    # seleciona um simbolo aleatoriamente e modificar ele
    def __init__(self):
        self._f = Factory_E1()
    
    def getC(self):
        c = C_E1()
        c.sample(6)
        s = S_E1(c)
        if random.random()<0.3:
            return S_E1(For_S_E1(s))
        else:
            return s
    def getMutations(self, prog, n_mutation) -> list[Node]:
       
        l_progs = []
        for _ in range(n_mutation):
            mutation = prog.clone(self._f)
            l= []
            mutation.countNode(l)
            newProg=[]
            for i in range(len(l)-1,-1,-1):
                
               if isinstance(l[i],S):
                    if isinstance(l[i]._childS,C) :
                        newProg.append(l[i])
            
            
            if len(newProg) == 0:
                l_progs.append(self.getC())
            else:
                no = newProg[random.randint(0, len(newProg)-1)]
            
            
                s_s = S_S_E1(S_E1(no._childS),self.getC())
                no._childS = s_s
                l_progs.append(mutation)
        return l_progs