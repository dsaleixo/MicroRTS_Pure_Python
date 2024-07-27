

from synthesis.baseDSL.tests.scriptsToy import ScriptsToy
from synthesis.extent1DSL.mutation.mutation4 import Mutation4


if __name__ == "__main__":
    s = ScriptsToy.script3()
    m = Mutation4()
    print(s.translate())
    m.getMutations(s._childS,1)