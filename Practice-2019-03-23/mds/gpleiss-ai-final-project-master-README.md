Rachel and Geoff's AI project, spring 2013.
===========================================

Given a movie review, finds the sentence which best summmarizes the review. Based on research by Zhuang et al., available [here](http://research.microsoft.com/en-us/um/people/leizhang/Paper/cikm06_movie.pdf).

Requires Stanford Parser, written in Java. We've got the python wrapper included, but you need to download the Java package separately, as described below. 

Examples
-------
The [NYTimes review for "Pain and Gain"](http://movies.nytimes.com/2013/04/26/movies/michael-bays-pain-gain-with-mark-wahlberg.html?_r=0) is summarized by the sentence:

> It all leaves you pondering whether you have just seen a monumentally stupid movie or a brilliant movie about the nature and consequences of stupidity

And, the [Roger Ebert's review of the estimable Mean Girls](http://www.rogerebert.com/reviews/mean-girls-2004) is summarized by
> Mean Girls dissects high school society with a lot of observant detail which seems surprisingly well-informed

Setup
-----
* ``git clone git@github.com:gpleiss/ai-final-project.git``
* Download the Java code from [MIT](http://projects.csail.mit.edu/spatial/Stanford_Parser), and copy the 3rdParty directory to this project. (We added it to the .gitignore, because it was huge)
* You'll need to install JPype for python. We found [these instructions](http://blog.y3xz.com/blog/2011/04/29/installing-jpype-on-mac-os-x/) helpful for installing JPype on our Macs
* There's a chance you'll have more debugging to do. It took us about 4 hours to get the Stanford Parser working.
* To see whether things are set up properly, open Python and...:

        >>> from stanford_parser import parser as sp
        >>> parser = sp.Parser()
            Loading parser from serialized file 3rdParty/stanford-parser/stanford-parser-2010-08-20/../englishPCFG.July-2010.ser ... done [0.9 sec].
        >>> print parser.parseToStanfordDependencies("this movie was utterly fantastic")
        sentence='this movie was utterly fantastic'
        det(movie, this)
        nsubj(fantastic, movie)
        cop(fantastic, was)
        advmod(fantastic, utterly)

* If the above code works, you're good to go

To Use
------
To summarize each review included in the NLTK movie_reviews corpus:
    
    $ python summarizer.py

To summarize movie review(s) not included in the NLTK:
    
    $ python summarizer.py filename1.txt filename2.txt ... etc.
(We include 2 extra movie reviews, review_painandgain.txt and review_meangirls.txt)

