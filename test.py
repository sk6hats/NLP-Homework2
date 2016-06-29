from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition
import time


if __name__ == '__main__':

    # flags
    F_TEST_BADMODEL = True
    F_TRAIN_SWEDISH = True
    F_TRAIN_ENGLISH = True
    F_TRAIN_DANISH  = True
    F_TRAIN_KOREAN  = False

    #traindata = dataset.get_swedish_train_corpus().parsed_sents()


    try:
        if F_TEST_BADMODEL == True:
            print time.ctime(), "START BADMODEL"
            traindata = dataset.get_swedish_train_corpus().parsed_sents()
            labeleddata = dataset.get_swedish_dev_corpus().parsed_sents()
            blinddata = dataset.get_swedish_dev_blind_corpus().parsed_sents()

            modelfile = 'badfeatures.model'
            tp = TransitionParser.load(modelfile)
            parsed = tp.parse(blinddata)

            ev = DependencyEvaluator(labeleddata, parsed)
            print "UAS: {} \nLAS: {}".format(*ev.eval())

            conllfile = 'test.conll'
            with open(conllfile, 'w') as f:
                for p in parsed:
                    f.write(p.to_conll(10).encode('utf-8'))
                    f.write('\n')

            print time.ctime(), "-------DONE----- BADMODEL", modelfile, conllfile

        if F_TRAIN_SWEDISH == True:
            print time.ctime(), "START TRAIN SWEDISH"
            traindata = dataset.get_swedish_train_corpus().parsed_sents()
            labeleddata = dataset.get_swedish_dev_corpus().parsed_sents()
            blinddata = dataset.get_swedish_dev_blind_corpus().parsed_sents()

            modelfile = 'swedish.model'
            conllfile = 'swedish.conll'

            tp = TransitionParser(Transition, FeatureExtractor)
            tp.train(traindata)
            tp.save(modelfile)

            # load model for testing
            tp = TransitionParser.load(modelfile)
            parsed = tp.parse(blinddata)

            ev = DependencyEvaluator(labeleddata, parsed)
            print "UAS: {} \nLAS: {}".format(*ev.eval())

            with open(conllfile, 'w') as f:
                for p in parsed:
                    f.write(p.to_conll(10).encode('utf-8'))
                    f.write('\n')
            print time.ctime(), "-------DONE----- TESTING SWEDISH ", modelfile, conllfile

        if F_TRAIN_ENGLISH == True:
            print time.ctime(), "START TRAIN english"
            traindata = dataset.get_english_train_corpus().parsed_sents()
            labeleddata = dataset.get_english_dev_corpus().parsed_sents()
            blinddata = dataset.get_english_dev_blind_corpus().parsed_sents()

            modelfile = 'english.model'
            conllfile = 'english.conll'

            tp = TransitionParser(Transition, FeatureExtractor)
            tp.train(traindata)
            tp.save(modelfile)

            # load model for testing
            tp = TransitionParser.load(modelfile)
            parsed = tp.parse(blinddata)

            ev = DependencyEvaluator(labeleddata, parsed)
            print "UAS: {} \nLAS: {}".format(*ev.eval())

            with open(conllfile, 'w') as f:
                for p in parsed:
                    f.write(p.to_conll(10).encode('utf-8'))
                    f.write('\n')
            print time.ctime(), "-------DONE----- TESTING english ", modelfile, conllfile

        if F_TRAIN_DANISH == True:
            print time.ctime(), "START TRAIN danish"
            traindata = dataset.get_danish_train_corpus().parsed_sents()
            labeleddata = dataset.get_danish_dev_corpus().parsed_sents()
            blinddata = dataset.get_danish_dev_blind_corpus().parsed_sents()

            modelfile = 'danish.model'
            conllfile = 'danish.conll'

            tp = TransitionParser(Transition, FeatureExtractor)
            tp.train(traindata)
            tp.save(modelfile)

            # load model for testing
            tp = TransitionParser.load(modelfile)
            parsed = tp.parse(blinddata)

            ev = DependencyEvaluator(labeleddata, parsed)
            print "UAS: {} \nLAS: {}".format(*ev.eval())

            with open(conllfile, 'w') as f:
                for p in parsed:
                    f.write(p.to_conll(10).encode('utf-8'))
                    f.write('\n')
            print time.ctime(), "-------DONE----- TESTING danish ", modelfile, conllfile


        if F_TRAIN_KOREAN == True:
            print time.ctime(), "START TRAIN korean"
            traindata = dataset.get_korean_train_corpus().parsed_sents()
            labeleddata = dataset.get_korean_dev_corpus().parsed_sents()
            blinddata = dataset.get_korean_dev_blind_corpus().parsed_sents()

            modelfile = 'korean.model'
            conllfile = 'korean.conll'

            tp = TransitionParser(Transition, FeatureExtractor)
            tp.train(traindata)
            tp.save(modelfile)

            # load model for testing
            tp = TransitionParser.load(modelfile)
            parsed = tp.parse(blinddata)

            ev = DependencyEvaluator(labeleddata, parsed)
            print "UAS: {} \nLAS: {}".format(*ev.eval())

            with open(conllfile, 'w') as f:
                for p in parsed:
                    f.write(p.to_conll(10).encode('utf-8'))
                    f.write('\n')
            print time.ctime(), "-------DONE----- TESTING korean ", modelfile, conllfile



        # tp = TransitionParser(Transition, FeatureExtractor)
        # tp.train(traindata)
        # tp.save('swedish.model')

#        labeleddata = dataset.get_swedish_dev_corpus().parsed_sents()
#        blinddata = dataset.get_swedish_dev_blind_corpus().parsed_sents()
#        tp = TransitionParser.load('badfeatures.model')

        #parsed = tp.parse(blinddata)
        # with open('test.conll', 'w') as f:
        #     for p in parsed:
        #         f.write(p.to_conll(10).encode('utf-8'))
        #         f.write('\n')
        #
        # ev = DependencyEvaluator(labeleddata, parsed)
        # print "UAS: {} \nLAS: {}".format(*ev.eval())

        # parsing arbitrary sentences (english):
        # sentence = DependencyGraph.from_sentence('Hi, this is a test')

        # tp = TransitionParser.load('english.model')
        # parsed = tp.parse([sentence])
        # print parsed[0].to_conll(10).encode('utf-8')
    except NotImplementedError:
        print """
        This file is currently broken! We removed the implementation of Transition
        (in transition.py), which tells the transitionparser how to go from one
        Configuration to another Configuration. This is an essential part of the
        arc-eager dependency parsing algorithm, so you should probably fix that :)

        The algorithm is described in great detail here:
            http://aclweb.org/anthology//C/C12/C12-1059.pdf

        We also haven't actually implemented most of the features for for the
        support vector machine (in featureextractor.py), so as you might expect the
        evaluator is going to give you somewhat bad results...

        Your output should look something like this:

            UAS: 0.23023302131
            LAS: 0.125273849831

        Not this:

            Traceback (most recent call last):
                File "test.py", line 41, in <module>
                    ...
                    NotImplementedError: Please implement shift!


        """
