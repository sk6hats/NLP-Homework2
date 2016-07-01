
                           UNI: spk2136
                      Name: Swapnil Khedekar

===================================================================

1B:
Simple way to find if a given dependency graph is to compare each
ark with every other ark in the graph. If we find an ark with
EXACTLY-ONE node (either head or tail but not none/both), that
falls within head & tail of another ark, then its a Non-Projective.
Otherwise the graph is projective.

Intuitively, if only one node of another ark falls within head-tail
span of current ark, then other node of that ark must be outside the
head-tail span of current ark. The only way that ark can connect is
by intersecting current ark, hence graph must be non-projective.

===================================================================

1C:
Projective:
British voters passed the Brexit referendum last week.

Non-Projective:
British voters passed the Brexit referendum last week which is
a non-binding motion.

Ark1: passed -> week        Ark2: referendum -> is
These two arks intersect each other. Also EXACTLY-ONE node
'referendum' of Ark2 falls within head ('passed') and tail ('week')
of Ark1. Thus this is non-projective.

===================================================================

2B:
UAS: 0.279305354559
LAS: 0.178726483357

===================================================================

3A:

===================================================================

3C:
English:
UAS: 0.791687041565
LAS: 0.750611246944

Swedish:
UAS: 0.798842257598
LAS: 0.706222865412

Danish:
UAS: 0.795836131632
LAS: 0.701141705843

===================================================================

3D:
Regular shift-reduce type parser needs to compare all possible POS
combinations against some rule-based grammar to make dependency
decision between two words. This easily turns into polynomial
O(n^3) or O(n^4) time complexity.

Arc-Eager makes "eager" or greedy decision to choose next action
(shift, reduce, left-arc, right-arc) at a given state of parser
configuration. It relies on pre-trained probability-based classifier
which could be considered a constant O(1) operation.
Additionally, each word is pushed/popped from stack exactly once &
arcs are added only between top-of-stack word & first buffer word.
Thus total number of actions are LINEAR O(n) complexity and
practically almost close to 'n'.

On the downside, arc-eager's greedy approach might result in less
optimal dependency decision especially for long phrases and in
languages where word order matters less. Also classifier picks
only one action & arc-eager never revisits/reconsider it in future
iterations, thus there is a chance certain combinations/rules may
never be considered by arc-eager.

Being probabilistic and pre-trained classifier, it can handle unseen
or blind datasets as well as does not need to explicitely elicit
each grammar rule or probable dependency ordering. Practically, its
performs reasonably well on unseen data as long as its from similar
dataset that classifier was trained on.

In short, Arc-eager tradeoffs accuracy VERSUS speed and reduction in
manual effort of eliciting each grammar rules. Practically, the loss
of accuracy is minimal compared to gains in speed & versatility.
===================================================================
