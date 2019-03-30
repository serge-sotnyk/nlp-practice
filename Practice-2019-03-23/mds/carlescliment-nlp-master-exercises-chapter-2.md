## Chapter 2

2)
> Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?

```
>>> import nltk
>>> words = nltk.corpus.gutenberg.words('austen-emma.txt')
>>> len(words)
192427
>>> len(set(words))
7811
```

So it contains 192,427 word tokens and 7,811 word types.

3)
> Use the Brown Corpus reader nltk.corpus.brown.words() or the Web Text Corpus reader nltk.corpus.webtext.words() to access some sample text in two different genres.

```
>>> nltk.corpus.brown.sents(categories=['adventure'])[1]
[u'He', u'was', u'well', u'rid', u'of', u'her', u'.']
>>> nltk.corpus.brown.sents(categories=['science_fiction'])[1]
[u"Self's", u'integrity', u'was', u'and', u'is', u'and', u'ever', u'had', u'been', u'.']
```

4)
> Read in the texts of the *State of the Union* addresses, using the state_union corpus reader. Count occurrences of men, women and people in each document. What has hapened to the usages of these words over time?

```
import nltk

cfd = nltk.ConditionalFreqDist(
  (target, fileid[:4])
  for fileid in nltk.corpus.state_union.fileids()
  for w in nltk.corpus.state_union.words(fileid)
  for target in ['men', 'women', 'people']
  if w.lower().startswith(target))

cfd.plot()
```

The text suggests that before 1970 the term *women* was almost unused, but since then it has been used more or less like the term *men*. *People* is the preferred term, specially in the last decades.

5)
> Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(), part_holonyms(), and substance_holonyms().

```
>>> lava = wn.synsets('lava')[0]
>>> ice = wn.synsets('ice')[0]
>>> lava.common_hypernyms(ice)
[Synset('matter.n.03'), Synset('physical_entity.n.01'), Synset('entity.n.01')]
>>> ice.substance_holonyms()
[Synset('glacier.n.01'), Synset('ice_cube.n.01')]
>>> ice.substance_meronyms()
[Synset('water.n.01')]
```


6)
> In the discussion of comparative wordlists, we created an object called translate, which you could look up using words in both German and Italian in order to get corresponding words in English. What problem might arise with this approach? Can you suggest a way to avoid this problem?

If a word exists in both languages, but with different meanings, we don't know what language are we going to translate from. A way to avoid the problem is to maintain two different dicts and pass the language toguether with the word to translate as method arguments.


7)
> According to Strunk and White’s Elements of Style, the word however, used at the start of a sentence, means “in whatever way” or “to whatever extent,” and not “nevertheless.” They give this example of correct usage: However you advise him, he will probably do as he thinks best. (http://www.bartleby.com/141/strunk3.html). Use the concordance tool to study actual usage of this word in the various texts we have been considering. See also the LanguageLog posting “Fossilized prejudices about ‘however’” at http://itre.cis.upenn.edu/~myl/languagelog/archives/001913.html.

```
nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')).concordance('however', lines=1000)
```

By analyzing a few documents, we find out that *However* is very rarely used properly.


8)
> Define a conditional frequency distribution over the Names Corpus that allows you to see which initial letters are more frequent for males versus females

```
>>> distribution = nltk.ConditionalFreqDist([(file, word[0]) for file in ['female.txt', 'male.txt'] for word in nltk.corpus.names.words(file)])
>>> distribution.tabulate()                                              
              A    B    C    D    E    F    G    H    I    J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z 
female.txt  443  246  469  308  251  144  213  124   83  293  276  332  484  158   66  121    9  247  309  198   14  105   54    5   18   31 
  male.txt  213  173  166  146  119   87  156  163   45  144   70  113  200   77   52  101   15  200  238  188   22   50  151    7   16   31 
```

