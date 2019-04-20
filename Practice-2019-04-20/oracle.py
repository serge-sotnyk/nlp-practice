from collections import OrderedDict
from enum import Enum
from itertools import zip_longest
from typing import List

from conllu import TokenList

from conlu_reader import read_trees


class Actions(Enum):
    SHIFT = "SHIFT"
    REDUCE = "REDUCE"
    RIGHT = "RIGHT"
    LEFT = "LEFT"


class Oracle:
    ROOT = OrderedDict([('id', 0), ('form', 'ROOT'), ('lemma', 'ROOT'), ('upostag', 'ROOT'),
                        ('xpostag', None), ('feats', None), ('head', None), ('deprel', None),
                        ('deps', None), ('misc', None)])

    def __init__(self):
        ...

    @staticmethod
    def _oracle(stack, top_queue, relations):
        """
        Make a decision on the right action to do.
        """
        top_stack = stack[-1]
        # check if both stack and queue are non-empty
        if top_stack and not top_queue:
            return Actions.REDUCE
        # check if there are any clear dependencies
        elif top_queue["head"] == top_stack["id"]:
            return Actions.RIGHT
        elif top_stack["head"] == top_queue["id"]:
            return Actions.LEFT
        # check if we can reduce the top of the stack
        elif top_stack["id"] in [i[0] for i in relations] and \
                (top_queue["head"] < top_stack["id"] or
                 [s for s in stack if s["head"] == top_queue["id"]]):
            return Actions.REDUCE
        # default option
        else:
            return Actions.SHIFT

    def restore_operations(self, tokens: TokenList) -> List[Actions]:
        stack, queue, relations = [self.ROOT], tokens[:], []
        operations = []

        while len(queue) > 0:
            action = self._oracle(stack, queue[0], relations)
            operations.append(action)
            if action == Actions.SHIFT:
                stack.append(queue.pop())
            elif action == Actions.REDUCE:
                stack.pop()
            elif action == Actions.LEFT:
                stack.pop()
            elif action == Actions.RIGHT:
                ...
        return operations

    @staticmethod
    def trace_actions(tree, log=True)->bool:
        """
        Try out the oracle to verify it's returning the right actions.
        """
        stack, queue, relations = [Oracle.ROOT], tree[:], []
        while queue or stack:
            action = Oracle._oracle(stack if len(stack) > 0 else None,
                                    queue[0] if len(queue) > 0 else None,
                                    relations)
            if log:
                print("Stack:", [i["form"] + "_" + str(i["id"]) for i in stack])
                print("Queue:", [i["form"] + "_" + str(i["id"]) for i in queue])
                print("Relations:", relations)
                print(action)
                print("========================")
            if action == Actions.SHIFT:
                stack.append(queue.pop(0))
            elif action == Actions.REDUCE:
                stack.pop()
            elif action == Actions.LEFT:
                relations.append((stack[-1]["id"], queue[0]["id"]))
                stack.pop()
            elif action == Actions.RIGHT:
                relations.append((queue[0]["id"], stack[-1]["id"]))
                stack.append(queue.pop(0))
            else:
                print("Unknown action.")
        g_relations = [(node["id"], node["head"]) for node in tree]
        are_equal = all(t1==t2 for t1, t2 in zip_longest(sorted(g_relations), sorted(relations)))
        if log and not are_equal:
            print("Not equal!")
            print("Gold relations:")
            print(g_relations)
            print("Retrieved relations:")
            print(sorted(relations))

        # trace_actions(tree)
        return are_equal


if __name__ == "__main__":
    trees = read_trees()
    total, unequal = 0, 0
    for i, tree in enumerate(trees):
        if any(not isinstance(t["id"], int) for t in tree):
            continue
        total += 1
        if not Oracle.trace_actions(tree, False):
            unequal += 1
            print(f"Sentence '{i}' is not oracled correctly.")
    print(f"Total: {total}, unequal: {unequal}")
    #Oracle.trace_actions(trees[0])
