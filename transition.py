class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # i=top of stack, j=first word in buffer
        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer[0]

        # preconditions - no root & no arc exists with tail 'i'
        if idx_wi == 0:
            return -1
        for arc in conf.arcs:
            if arc[2] == idx_wi:
                return -1

        # pop 'i' from stack & add reverse-ark
        conf.stack.pop()
        conf.arcs.append((idx_wj, relation, idx_wi))

    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # You get this one for free! Use it as an example.

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.stack:
            return -1

        # i: top of stack
        idx_wi = conf.stack[-1]

        # preconditions: atleast one ark where tail is 'i'
        found = False
        for arc in conf.arcs:
            if arc[2] == idx_wi:
                found = True
        if found == False:
            return -1

        # remove 'i' from stack
        conf.stack.pop()


    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # i: first word in buffer, remove if from buffer & push on top of stack
        idx_wi = conf.buffer.pop(0)
        conf.stack.append(idx_wi)

