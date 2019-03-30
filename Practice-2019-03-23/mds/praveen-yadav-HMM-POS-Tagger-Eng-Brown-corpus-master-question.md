Assignment 4 : Part-of-Speech Tagging with HMMs
-----------------------------------------------

Task description : Part-of-Speech is a lexical property attributed to each word in a sentence. POS is generally the first layer of abstraction applied for any NLP task. This allows us to look at different words in a similar context because they have the same POS category.

The task involves this : 
    - You will be given a sentence (S)
    - Tokenise (S) into a word sequence (Ws) {Please use the tokeniser you have already developed}
    - For each word (w) use the HMM to produce a tag (t)
    - Finally output a tag sequence (T)
    
For learning the HMM parameters, you would need an annotated corpus. For that, please use the brown corpus from the nltk : http://www.nltk.org/howto/corpus.html#tagged-corpora
    - You would need to install nltk and then do nltk.download() (Then, go to corpora tab and install brown)
    - If your language of choice is not python, you need to convert this into plain text file and then use it.
    - Important !! : If you run out of ram on this big a data, then run it on a feasible part of this data (Mention it in the report)
    
Training and Testing
    - If you are working with say 1000 sentences, you have to divide them into training, and testing.
    - Training set is typically 60-80% of the whole dataset; so in this case it is 600-800 sentences.
    - Testing is the rest; 400-200 sentences
    - It is imperative that the Training and Testing sets are separate.
    - It is equally crucial that you DO NOT train on the testing set (It is cheating otherwise :P)




