
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

===================================================================
