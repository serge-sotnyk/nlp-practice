## Evaluation Corpus for Named Entity Recognition using Europarl

This repository contains a gold-standard test set created from the [Europarl corpus](http://www.statmt.org/europarl/). The test set consists of 799 sentences manually annotated using four entity types and following the [CoNLL 2002 and 2003 guidelines](https://www.clips.uantwerpen.be/conll2003/ner/) for 4 languages: English, German, Italian and Spanish.

In order to obtain the final 799 annotated sentences for each language, the first 2000 sentence from the Europarl corpus were used for each of the languages. The word alignments were obtained via Giza++, which was trained on the rest of the Europarl corpus (e.g., Europarl minus the first 2000 sentences).

If you use this corpus for your research, **please cite the following publication**:

Rodrigo Agerri, Yiling Chung, Itziar Aldabe, Nora Aranberri, Gorka Labaka and German Rigau (2018). Building Named Entity Recognition Taggers via Parallel Corpora. In Proceedings of the 11th Language Resources and Evaluation Conference (LREC 2018), 7-12 May, 2018, Miyazaki, Japan.

You should also consider citing the original Europarl publication:

Europarl: A Parallel Corpus for Statistical Machine Translation, Philipp Koehn, MT Summit 2005.

This evaluation corpus was manually annotated by **Nora Aranberri**.

## Contents
One file per language in CoNLL 2002 format:

+ de-europarl.test.conll02
+ en-europarl.test.conll02
+ es-europarl.test.conll02
+ it-europarl.test.conll02

## License
We follow the original Europarl terms of use which states : "We are not aware of any copyright restrictions of the material." For more details, please visit [http://www.statmt.org/europarl/](http://www.statmt.org/europarl/)

