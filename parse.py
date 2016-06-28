from providedcode.transitionparser import TransitionParser
from providedcode.dependencygraph import DependencyGraph
from nltk.tag import mapping
import sys

# check number of inputs
if len(sys.argv) != 2:
    raise ValueError("Invalid arguments. Usage: python parse.py <modelfile>")

# validate & load modelfile from commandline arg
modelfile = sys.argv[1]
tp = TransitionParser.load(modelfile)

# read each line as a sentence from stdin
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        continue

    # convert to DependencyGraph and replace CPOS features as they are not
    # originally part of from_sentence(). Piazza
    sentence = DependencyGraph.from_sentence(line)
    for node in sentence.nodes:
        tag = sentence.nodes[node]['tag']
        ctag = mapping.map_tag('wsj','universal',tag)
        sentence.nodes[node]['ctag'] = ctag


    parsed = tp.parse([sentence])
    print parsed[0].to_conll(10).encode('utf-8')


    #print ">>",line,"<<"