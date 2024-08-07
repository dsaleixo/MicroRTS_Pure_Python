
from random import random
from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.mutation.mutation import Mutation
from synthesis.extent1DSL.mutation.mutation0 import Mutation0
from synthesis.extent1DSL.mutation.mutation1 import Mutation1
from synthesis.extent1DSL.mutation.mutation3 import Mutation3
from synthesis.extent1DSL.mutation.mutation4 import Mutation4
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class Mutation2(Mutation):
    #combina as outras mutações
    def __init__(self):
        self._f = Factory_E1()
        self.m0 = Mutation0()
        self.m1 = Mutation1()
        self.m3 = Mutation3()
        self.m4 = Mutation4()
        self.r = random
    
    
    def getMutations(self, prog, n_mutation) -> list[Node]:
        aux = self.r()
        #if aux <0.33: return self.m0.getMutations(prog, n_mutation)
        #elif aux < 0.66 :return self.m1.getMutations(prog, n_mutation)
        #else : return self.m3.getMutations(prog, n_mutation)
        aux = self.r()
        if aux <0.5: return self.m0.getMutations(prog, n_mutation)
        else :return self.m4.getMutations(prog, n_mutation)