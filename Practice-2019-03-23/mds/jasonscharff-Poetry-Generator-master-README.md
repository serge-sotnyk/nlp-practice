#Poetry Generator: Building Shakesparean Sonnets

###Summary
This program employs a combination of algorithims to generate a Shakesparean Sonnet: a 14 line poem written in iambic pentameter with a rhyming scheme of A, B, A, B, C, D, C, D, E, F, E, F, G, G. The fundamental principal behind the stategy employed in this program is the Markov chain. In other words, given a seed, the program finds all words used in the training text (all of Shakespeare's sonnets) after the seed and using a weighted probability randomly chooses the next word. The probability is weighted by how often a paritcular word appears after the initial word. For example if the seed was thou and 50% of the time after the word "thou" the word "art" is used then there is a 50% chance that art will be the next word in the poem. The process is repeated for every single word until the line is complete (all ten syllables). The first word of each line is taken exclusively from the collection of words used to start a line in Shakespeare. If the user does not enter a theme then from the collection of "start" words one is just chosen for each line. However, if the user decides to enter a theme then all synonyms and related words of the theme word that are in the collection of starting words are used to start lines. For example, if the user was to enter preceeding as the theme, the word above would be used to start a line because Shakespare started one of his lines with "Above" and it is related to "Preceding". By  just using words from Shakespearean texts all words are guaranteed to be in iambic pentameter and in the voice of Shakespeare.

The only exception to using words from Shakespeare's sonnets is for rhyming. Because lines are built from the front (while it could be done from the back, it would then be harder to use a Shakespeare word to start a line which helps the entire poem make more sense), sometimes a rhyming word used by Shakespare is not available to finish a line. In that case a rhyming dictionary finds a word that starts with the correct stress, fits the syllable count, and then uses that word to finish the line. While this will occasionally make the poem make less sense and rarely make it not perfect iambic pentameter, a rhyme is ensured.

If nothing fits that line, the poem is just thrown out and a new one is generated. This is fairly rare, however.

###User Experience
After building the database (which takes a few seconds), the user is prompted for a theme. If they choose to not enter a theme, the computer will just build a poem using a completely random words. If, however, they choose to enter a theme all synonyms and related words that Shakespeare also has used to start a line are used to start lines in the computer's poem. Some themes simply do not work with the training set in which case the user is informed the theme is invalid and the computer just writes their own poem. The computer will continue to create poems as prompted to the user unless the enters "done" instead of a theme in which case the program terminates. This allows the databse to not be built multiple times.

###Tools and Libraries
The program was written entirely in Python Version 2.7.6 with the use of external libraries.
The external libraries are as follows:
* [PyTrie](http://pythonhosted.org//PyTrie/)
    * PyTrie implements a Trie. It is used instead of a Dictionary to store the syllable mappings (a pronunciation guide) and the syllable count of each word. Due to the large volume of words in the English language it is more efficient than a Dictionary due to the amount of RAM that would be necessary for a simple dictionary.   
  
* [Big Huge Thesaurus](https://words.bighugelabs.com/) 
    * Big Huge Thesaurus is used as an API to get related words to the theme. If the user enters a theme, all synonyms are found using their API to maximize the occurence of words related to that theme. 
* [Rhyme Brain](http://rhymebrain.com/api.html)
    * If the end of a line is occuring without the Markov chain leading to a potential rhyme then a rhyming word is found using the Rhyme Brain API that can be inserted to finish a line while preserving rhyme. 
* [Requests](http://docs.python-requests.org/en/latest/)
    * The Rhyme Brain API uses a simple HTTP GET request for it's API. To make this process cleaner, the requests HTTP library for Python is used.
    
In addition to technical libraries, external documents are used as resources to assist in the development process. Namely, a [pronounciation and stressed syllable dictionary from CMU](http://www.speech.cs.cmu.edu/cgi-bin/cmudic) and the training text of all of [Shakespeare's sonnets](http://www.shakespeares-sonnets.com/all.php).

###Known Issues and Areas For Improvement
One of the bugs commonly seen early on is the disparity between the CMU dictionary and the words used in Shakespeare's work. To accomodate words not common to both are just thrown out. However, some words are in the dictionary, but Shakespeare adds a "st" to them (such as in bestow'st). To do this the program accomodates by throwing out the " 'st " to access the modern dictionary and just adding a syllable. However, this can mess up rhyming. A fix is possible as it is just a special case, but unfortunately I didn't have enough time to add this fix and therefore sometimes rhyming is slightly off.

As well, sometimes pathways lead nowhere causing an error in the program. Currently, the poem is just thrown out and a new one is produced (this is fairly rare), but if I had more time a more sustainable solution using foresight would be included instead.

The biggest area for improvement would actually be in the general strategy. Instead of just building from the front (or choosing to build from the back to ensure rhyming) the best would be to build from both and "meet in the middle". This would ensure a pure Shakesparean vocabulary, but once again could not be implemented due to time concerns.

As well, to further the quality of the words used if I had more time I would add in the training text of every single Shakespearean play. The reason this isn't that simple is I would need to write a script to scrape the text off of the web and then remove character names. This isn't necessarily complex, but I chose to allocate my time to the actual development of the program.







