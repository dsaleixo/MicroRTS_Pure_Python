from Tests.Test4 import Test4
from Tests.test6 import Test6
from synthesis.baseDSL.tests.scriptsTests import ScriptsTests
from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.playoutBF import PlayoutBF
from synthesis.extent1DSL.tests.sampleMutation import SampleMutation
from synthesis.extent1DSL.tests.testSketchSearch import TestSketchSearch

if __name__ == "__main__":
    #map = "./maps/basesWorkers32x32A.xml"
    #map = "./maps/mapadavid2.xml"
    map = "./maps/basesWorkers32x32A.xml"
    TestSketchSearch.test1()
