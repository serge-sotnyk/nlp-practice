from sklearn.metrics import classification_report

from scripts.baseline_logisticregression import readInData
from typing import NamedTuple, List
#from scripts.bert_utils import calc_entailment_prob
from sklearn.ensemble import RandomForestClassifier
from  sklearn.linear_model import LogisticRegression
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


def featurize(x_raw: List[RawInput]) -> List[List[float]]:
    res = []
    for r in x_raw:
        res.append([len(r.twit0)/len(r.twit1), len(r.twit0)/100, len(r.twit1)/100])
    return res


def report(y_true, y_pred):
    y_true_cleaned, y_pred_cleaned = [], []
    for t, p in zip(y_true, y_pred):
        if t is not None:
            y_true_cleaned.append(t)
            y_pred_cleaned.append(p)
    print(classification_report(y_true_cleaned, y_pred_cleaned))


class FakeClassifier():
    def fit(self, x, y):
        return self

    def predict(self, x):
        res = []
        for i, _ in enumerate(x):
            res.append(i % 2 == 0)
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
    #clf = RandomForestClassifier(n_estimators=100, random_state=1974, verbose=True)
    clf = LogisticRegression(random_state=1974, verbose=True, solver='saga', max_iter=2000, class_weight='balanced')
    #clf = FakeClassifier()
    print("Done!")
    clf.fit(x_train_features, y_train)
    y_pred = clf.predict(x_test_features)
    report(y_test, y_pred)

    #model = train_model(x_dev_raw, y_train)


if __name__=="__main__":
    main()