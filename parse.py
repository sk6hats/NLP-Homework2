from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition
#from providedcode.DependencyGraph import DependencyGraph
from providedcode.dependencygraph import DependencyGraph


import sys
if len(sys.argv) != 2:
    raise ValueError("Invalid arguments. Usage: python parse.py <modelfile>")

modelfile = sys.argv[1]
print modelfile
tp = TransitionParser.load(modelfile)


for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        continue

    sentence = DependencyGraph.from_sentence(line)
    parsed = tp.parse([sentence])
    print parsed[0].to_conll(10).encode('utf-8')


    #print ">>",line,"<<"