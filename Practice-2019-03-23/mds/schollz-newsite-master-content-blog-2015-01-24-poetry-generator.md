+++
slug = "/2015/01/24/turing-test-passed-using-computer-generated-poetry/"
title = "How my Poetry generator passed the Turing test"
date = "2015-04-25"
+++

![Cover of the Archive](/img/the_archive_cover.jpg)


This is how I developed another kind of
artificial intelligence (AI). This AI can create poetry indistinguishable
from real poets.

The real Turing Test of this AI was to get it accepted to a literary
journal, which was accomplished - this poetry was successfully accepted
into a literary journal at a prestigious university. The story is below
and the code is at the bottom for those who want to make their own!

What do you think of the following poem?
========================================

<div id="poem">
<blockquote><p><strong><em>Orange Light</em></strong></p>
<p><em>I conduct myself in a windy manner because I am</em><br />
<em> drunk and enchanted in this field.</em><br />
<em> The oxygen around my head is rabid</em><br />
<em> and filled with orange light</em><br />
<em> like a equinoctial tiger to its flesh.</em><br />
<em> My heart moves violently</em><br />
<em> on this neon ship.</em></p>
<p><em>I promise as I were a rotting ghost</em><br />
<em> forced half-open in love</em><br />
<em> in front of the gray agony of the darkness</em><br />
<em> and decaying droplets of acidulous gold.</em></p>
<p><em>I reply, only fear and geology are the</em><br />
<em> leaves of belligerence.</em></p>
<p><em>I&#8217;d do it for the geology</em><br />
<em> and I&#8217;d do it for the fear of your response.</em></p></blockquote>
</div>
If you answered anything other than *“That’s not a poem!”* to that
question, then you probably believe more or less that it *is* a poem,
and by some standards then the artificial intelligence that generated
this poem once again passed the Turing Test.

Turing test, what’s that?
=========================

The Turing test is a test of the ability of a machine to exhibit
intelligence that is indistinguishable from a human. It can exist in
many varieties - chat bots, intelligence bots, artist bots. This poetry
generator is a very simple type of artificial intelligence, yet it is
indistinguishable from any sort of poetry you may encounter from other
humans.

There have been generators among the years that are capable of passing
Turing tests. In 2005, [students wrote a generator for academic CS
papers](http://pdos.csail.mit.edu/scigen/). One of the generated papers
was accepted to a conference before conference organizers realized it
was a joke. There is also [a great post-modernism
generator](http://www.elsewhere.org/pomo/) developed by Andrew Bulhak
and Josh Larios, which demonstrates the ability to generate cohesive but
incoherent post-modernist literature academic papers.

How does the poetry generator work?
===================================

This Poetry generator uses a [Context-free
grammar](https://en.wikipedia.org/wiki/Context-free_grammar) using the
notation of [Backus-Naur
Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form).
Context-free grammar systems are a generalized system of formal grammar
defined by production rules which allow sentences to be recursively
built from smaller phrases. The formalism was developed by [Noam
Chomskey](https://en.wikipedia.org/wiki/Noam_Chomsky) in the 1950’s.

Essentially this poetry generator works by having the poem dissected
into smaller components: stanzas, lines, phrases, then verbs,
adjectives, and nouns. When a call to create a poem is made, then it
randomly selects components of the poem and recursively generates each
of those. For example, a generated title may look something like this:

    *title*=A *fruit*
    *fruit*=grape|apple|orange|banana|cherry|mango|kiwi|tomato|lemon|fruit

In that case the title is generated as “A ” and then it looks up and
selects one of the possible “” words to finish it before it returns “A
grape” or something similar.

Does this computer-generated poetry pass the Turing test?
=========================================================

I began by submitting my poetry to
[your-poetry.com](http://www.your-poetry.com/index.php) which was a
popular poetry website of the time (in 2010). I never conferred that
these poems were computer-generated. I published under the name
[Antikythera](http://www.your-poetry.com/modules.php?name=Your_Account&op=userinfo&username=antikythera).
The responses I received were, for the most part, quite flattering. Here
are some of the responses I got:

> *“Many layers to this piece, it demands a second and even third
> reading. I like the challenge you’ve set out here, well done.”*
>
> *"I like this!* *Its like it is straight from the pages of a mystical
> story,filled with delightful colours and wonderful landscapes."*
>
> *“I like you style of just giving the reader a small taste of what you
> are expressing. It opens up the thought process and gives us something
> to ponder without fully knowing the subject. Nice!”*
>
> *“What a wonderful piece of writing. you paint a vivid picture and I
> love the picture you have painted here. well done.”*
>
> *“Its like you just sang a beautiful song…”*
>
> *“you certainly know how to make words jump off the page, well
> written, well done.”*

The negative criticism I received typically found that my poems were
incomprehensible or nonsensical, such as the following:

> *“Sorry to say you have a very strange way of expressing yourself and
> this poem I have really not understood.”*

The overwhelming positive responses compelled me to use a more stringent
test of authenticity - seeing whether this computer-generated poetry
could get published in a poetry or literary journal.

Final test: Getting computer-generated poetry published
=======================================================

As many poets often do, I tried submitting my poetry to several places.
When I submitted these poems to publications I never specified that they
were computer generated. I submitted to the Memoir Journal (now defunct)
and First Writer Poetry contest but both rejected the poetry without
comment. I then turned to local sources and submitted to The Archive,
one of the oldest continuously published literary magazines in the
United States and the oldest student publication at [Duke
University](https://dukearchive.wordpress.com/).

The Archive agreed to publish one of my poems! The email chain is below.
I actually submitted 26 poems (one for each letter of the alphabet) and
selected a good one to publish.

<br>
<div class="row">
<div class="col-md-3"></div>
<div class="col-md-6"><img src="/img/the_archive_email.jpg" alt="Poetry generator correspondence" class="img-responsive center-block"></div>
<div class="col-md-3"></div>
</div>
<br> 
           
The Archive published a great poem and selected an image of a bulldozer
to be accompanied with it. The bulldozer is interesting, I think that
they implied that the poem's central theme is something about the
destruction of the environment? The poem and art is shown below:

<br>
<div class="row">
<div class="col-md-3"></div>
<div class="col-md-6"><img src="/img/the_archive_pg31.jpg" alt="Page 31 of The Archive - The poem I entered into a literary journal" class="img-responsive center-block"></div>
<div class="col-md-3"></div>
</div>
<br>             
<br>
<div class="row">
<div class="col-md-3"></div>
<div class="col-md-6"><img src="/img/the_archive_pg32.jpg" alt="Page 32 of the Archive, photograph accompanying the poem" class="img-responsive center-block"></div>
<div class="col-md-3"></div>
</div>
<br>
**In conclusion** it seems very possible to create an artificial
intelligence to do specialized tasks, like writing poetry, that can
sufficiently pass as a human being. Perhaps in the future we will need
to question the source of creative materials to determine whether they
are indeed human or machine made.

**Interested in making your own poem?**
=======================================

The source code for my poetry generator (now implemented in Python
instead of Java) is open-source and available. Click the button below to
generate your own poem, or check out the source code on
[Github](https://github.com/schollz/poetry-generator).

Click [here](http://www.poetrygenerator.ninja) to try generating your own poem!
===============================================================================

Acknowledgements
================

My thanks to the editor for considering the poetry for The Archive.

