PATH = "/your/path/to/ner-uk/"

# Read tokens and positions of tokens from a file

def read_tokens(filename):
    tokens = []
    pos = 0
    with open(filename, "r") as f:
        text = f.read().split("\n")
        for line in text:
            if len(line) == 0:
                pos += 1
            else:
                tokens.append(("<S>", pos, pos))
                for token in line.split(" "):
                    tokens.append((token, pos, pos + len(token)))
                    pos += len(token) + 1
                tokens.append(("</S>", pos, pos))
    return tokens

# Read annotations and positions of annotations from a file

def read_annotations(filename):
    anno = []
    with open(filename, "r") as f:
        for line in f.readlines():
            annotations = line.split()
            anno.append((annotations[1], int(annotations[2]), int(annotations[3])))
    return anno

# Using positions of tokens and annotations, extract a list of token labels

def extract_labels(anno, tokens):
    labels = []
    ann_id = 0
    for token in tokens:
        if ann_id < len(anno):
            label, beg, end = anno[ann_id]
            if token[0] in ["<S>", "</S>"]:
                labels.append("--")
            elif token[1] < beg:
                labels.append("--")
            else:
                if token[1] == beg:
                    labels.append("B-" + label)
                else:
                    labels.append("I-" + label)
                if token[2] == end:
                    ann_id += 1
        else:
            labels.append("--")    
    return labels

# tokens = read_tokens(PATH + "data/A_alumni.krok.edu.ua_Prokopenko_Vidrodzhennia_velotreku(5).tok.txt")
# anno = read_annotations(PATH + "data/A_alumni.krok.edu.ua_Prokopenko_Vidrodzhennia_velotreku(5).tok.ann")
# labels = extract_labels(anno, tokens)

# for i, j in zip(tokens, labels):
#     print(i[0], j)

# Extract list of files for training and testing

dev_test = {"dev": [], "test": []}
category = ""
with open(PATH + "doc/dev-test-split.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line in ["DEV", "TEST"]:
            category = line.lower()
        elif len(line) == 0:
            continue
        else:
            dev_test[category].append(line)

print(len(dev_test["dev"]), len(dev_test["test"]))

# Get train and test data and labels

train_tokens, test_tokens, train_labels, test_labels = [], [], [], []

for filename in dev_test["dev"]:
    try:
        tokens = read_tokens(PATH + "data/" + filename + ".txt")
        train_tokens += [token[0] for token in tokens]
        train_labels += extract_labels(read_annotations(PATH + "data/" + filename + ".ann"), tokens)
    except:
        pass

for filename in dev_test["test"]:
    try:
        tokens = read_tokens(PATH + "data/" + filename + ".txt")
        test_tokens += [token[0] for token in tokens]
        test_labels += extract_labels(read_annotations(PATH + "data/" + filename + ".ann"), tokens)
    except:
        pass

