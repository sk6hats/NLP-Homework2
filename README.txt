
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

Arc1: passed -> week        Arc2: referendum -> is
These two arks intersect each other. Also EXACTLY-ONE node
'referendum' of Ark2 falls within head ('passed') and tail ('week')
of Ark1. Thus this is non-projective.

===================================================================

2B:
UAS: 0.279305354559
LAS: 0.178726483357

===================================================================

3A:
For the starters, provided code only used top of stack (STK0) &
first word in buffer (BUF0) for features. The model received <.3 LAS
for English & Swedish. Danish LAS was .56 mostly due to 'feats'.
During n-gram exercise in previous Homework, we learnt that adding
more context ('n' adjacent words), increases accuracy in POS/grammar.
That principle should also work for arc-eager by looking beyond just
top of stack & second-third word in buffer.

Thus, it was found that by adding STK0_TAG, BUF0_TAG & BUF1_TAG was
had biggest impact on LAS (close to 0.7 for all languages).
Individually each of these features have .1 to .2 improvement to LAS
but as a combination, LAS improves significantly. These three features
add very small number of additional features (<100) that helps the
training speed and process memory. Thus, these seem to be most
efficient set of features for gain in accuracy Vs speed/memory cost.

STK0_TAG feature individually improved English & Swedish LAS by 15%
and Danish LAS by 9%. And thus simply guessing dependency based on
tag of the current word seems not too accurate just as humans can not
accurately predict such dependency without reading rest of sentence.
e.g. given current word is 'eating', rest of sentence could be
'eating pizza', 'eating with a fork' or 'eating with a friend'.

BUF0_TAG feature alone improved English LAS by .4 although Danish &
Swedish LAS improved by <.1. Intuitively, this means knowing tag of
next word, we can most often predict current word tag. e.g. if next
word is -ing verb, most often current word would be is/was.
Interestingly, the difference of impact on LAS of English versus on
that of Danish & Swedish can be attributed to rigid/predictive
word-ordering in English sentences than that of other languages.

BUF1_TAG feature alone only marginally (<.1) improved LAS for all
three languages. This also matches human intention that we almost
never can predict second-next word without knowing current or next
word. Yet, the relevance of this feature is to combine with above
two features to produce added context/tag-sequence for added accuracy
(similar to tri-grams Vs bi-grams/unigrams).

Other observations about features tried:
* STK0_FORM & BUF0_FORM also improve LAS close significantly for all
  languages but have downside of too-many additional features slowing
  training and could 'overfit' classifier in case of blind dataset.
* Arc-eager design of stack/buffer seem to predict all child/dependent
  dependencies before finding head of current STK0/BUF0. e.g. it will
  detect "with->fork" OR "with->friend" before "eat->with". That thought
  indicates knowing dependents of STK0/BUF0 will help predict STK0<->BUF0
  dependency as seen by sequence (STK0, BUF0, BUF1).
* Coarse tags CTAG seem to achieve same results as TAG but provided
  code from_sentence() ignores CTAG.
* Removing left-right dependent address functions had much lesser impact
  on LAS for all three language - indicating some relation, however small,
  on dependent arcs already discovered.
* Number of elements in Stack and remaining words in buffer had little
  positive impact on LAS.
===================================================================

3C:
English:
UAS: 0.79902200489
LAS: 0.756968215159

Swedish:
UAS: 0.796671490593
LAS: 0.700434153401

Danish:
UAS: 0.793149764943
LAS: 0.700470114171

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
