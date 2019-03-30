# Annotating-Non-Restrictive
Code, models, and corpus of non-restrictive noun phrase modifications.  
Published in "[Annotating and Predicting Non-Restrictive Noun Phrase Modifications](https://gabrielstanovsky.github.io/assets/papers/acl16a/paper.pdf)" (Stanovsky and Dagan, ACL 2016)

Generating the corpus
---------------------

To get the annotated corpus, you'll first need to obtain the [CoNLL 2009 corpus from LDC](https://catalog.ldc.upenn.edu/LDC2012T04) (specifically, we'll use CoNLL2009-ST-English-train.txt).

Once you get it, run:
```bash
./generateCorpora.sh CoNLL2009-ST-English-train.txt
```

This will generate the corpus (train, dev and test splits) in the "corpus" directory.

Corpus format
-------------
The corpus will be generated in the corpus directory.
Each CoNLL token will contain these additional two fields:   

1. Restrictiveness, which has the following possible values:
       * **RSTR** -- Marking a restrictive modifier.
       * **NON-RESTR** -- Marking a non-restrictive modifier.
       * **_** -- Marks an un-annoated token.

2. Modifier Type, marking the type of this modifier. Has the following possible values (see paper for example and evaluation):
      * **_** -- This token is not a modifier.
      * **APPOS-MOD** -- Appositional modifier.
      * **INF-MOD** -- Infinitival modifier.
      * **POSTADJ-MOD** -- Postfix adjectival modifier.
      * **PP-MOD** -- Prepositional modifier.
      * **PREADJ-MOD** -- Prefix adjectival modifier.
      * **PREVERB-MOD** -- Prefix verbal modifier.
      * **RC-MOD** -- Relative Clause modifier.




Other files in this repo
------------------------

- **classifiers** -- Contains the code for the classifiers described in the paper.

- **diffs** -- The diff files which, in conjunction with the CoNLL data, generate our annotated corpus.

- **features** -- The CRF features for each of the training instances, used to train both CRF models.

- **models** -- Pre-trained models, acheiving the results described in the paper.


