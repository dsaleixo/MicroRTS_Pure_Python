
from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1
from synthesis.extent1DSL.extent1Main.s_s_E1 import S_S_E1
from synthesis.extent1DSL.mutation.mutation import Mutation
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class Mutation1(Mutation):
    #adiciona um mutação no inicio do script
    def __init__(self):
        self._f = Factory_E1()
    
    
    def getMutations(self, prog, n_mutation) -> list[Node]:
        l_progs = []
        for _ in range(n_mutation):
            mutation = prog.clone(self._f)
            s = S_E1()
            s.sample(5)
         
            l_progs.append(S_E1(S_S_E1(s,mutation)))
        return l_progs