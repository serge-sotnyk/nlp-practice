from sklearn.metrics import classification_report

from scripts.baseline_logisticregression import readInData
from typing import NamedTuple, List
#from scripts.bert_utils import calc_entailment_prob
from sklearn.ensemble import RandomForestClassifier
from bpemb import BPEmb


_emb = BPEmb(lang='en', dim=300)


class RawInput(NamedTuple):
    twit0: str
    twit1: str


def load_data(fn: str)->(List[RawInput],List[bool]):
    print(f"Start to read '{fn}'")
    data, trends = readInData(fn)
    print("Total records:", len(data))
    print("True samples:", sum([1 for r in data if r[1]]))
    print("False samples:", sum([1 for r in data if not r[1]]))
    return [RawInput(r[2], r[2]) for r in data], [r[1] for r in data]


def featurize(x_raw: List[RawInput])->List[List[float]]:
    res = []
    for r in x_raw:
        p = calc_entailment_prob(r.twit0, r.twit1)
        pb = calc_entailment_prob(r.twit1, r.twit0)
        res.append([p[0], p[1], pb[0], pb[1]])
    return res


def main():
    x_train_raw, y_train = load_data('../data/train.data')
    x_dev_raw, y_dev = load_data('../data/dev.data')
    x_test_raw, y_test = load_data('../data/test.data')

    print("Start featurizing...")
    x_train_features = featurize(x_train_raw)
    x_dev_features = featurize(x_dev_raw)
    x_test_features = featurize(x_test_raw)
    print("Done!")

    print("Start learning classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=1974, verbose=True)
    print("Done!")
    clf.fit(x_test_features, y_train)
    y_pred = clf.predict(x_test_features)
    print(classification_report(y_test, y_pred))

    #model = train_model(x_dev_raw, y_train)


if __name__=="__main__":
    main()