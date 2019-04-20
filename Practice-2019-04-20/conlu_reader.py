from collections import OrderedDict
from conllu import parse
import itertools

PATH = "d:/git-nlp/UD_Ukrainian-IU"


def read_trees(path: str = PATH):
    with open(PATH + "/uk_iu-ud-train.conllu", "r", encoding='utf-8') as f:
        data = f.read()
    trees = parse(data)
    return trees


if __name__=="__main__":
    # debug mode
    trees = read_trees()
    node_printed = False
    for tree in itertools.islice(trees, 1):
        for node in tree:
            if not node_printed:
                print(node)
                node_printed = True
            head = node["head"]
            print("{} <-- {}".format(node["form"],
                                     tree[head - 1]["form"]
                                     if head > 0 else "root"))
            # print(node)
