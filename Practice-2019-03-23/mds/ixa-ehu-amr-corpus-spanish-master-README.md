# Abstract Meaning Representations in Spanish

This repository contains the Spanish AMR annotations for 50 sentences from the [Little Prince Corpus](https://amr.isi.edu/download/amr-bank-v1.6.txt). For details about AMR annotations in Spanish please see the following publication:

Noelia Migueles Abraira. A Study Towards Spanish Abstract Meaning Representation. Master Thesis, University of the Basque Country UPV/EHU. June 2017.(https://addi.ehu.es/handle/10810/22056)

## Spanish AMR annotations

The file **es-Little-Prince-Corpus-50-AMR.txt** contains the 50 Spanish sentences that were manually annotated. Futhermore, it includes the following metadata:

+ ::id → llp_es.N, where "es" indicates that it is a Spanish sentence and "N" its ID number. The ID number corresponds to the ID number of their corresponding English sentence in the original English corpus (https://amr.isi.edu/download/amr-bank-v1.6.txt).
+ ::annotator → The nickname of the annotator.
+ ::tok → The sentence to be annotated.

## English AMR annotations

For convenience, we also include the 50 English sentences used to create the Spanish AMR annotations. These sentences and annotations taken without any modification to facilitate researchers any mapping between the English and the Spanish AMRs.

Thus, the file **en-Little-Prince-Corpus-50-AMR.txt** contains the 50 original English sentences and AMRs that were translated and annotated in Spanish. Furthermore, it includes the following metadata:

+ ::id → llp_en.N, where "en" indicates that it is an English sentence and "N" its ID number. The ID number corresponds to the ID number of their corresponding Spanish sentence.
+ ::annotator → lpp_1943.N, where "N" indicates its ID number within The Little Prince Corpus.
+ ::tok → The sentence to be annotated.

## License
The Spanish AMR corpus is licensed by a cc-by-sa-4.0 license:

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

