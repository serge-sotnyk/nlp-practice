Representing Kekule Cells in Stable Molecules
======


<b>1 Introduction</b>

Carbon is the 6th element of the periodic table and backbone of all organic molecules. It is tetravalent,
meaning it has 4 valence electrons available to form covalent chemical bonds. In such bonds,
atoms share electrons relatively equally between them. Each possible bonding partner of carbon
will contribute a single electron to the covalent bond, meaning carbon, in its full valency will have
8 electrons. This is considered a full octet, and the stable configuration of carbon. However, 4
bonding partners is not always needed in order to be stable. If Carbon was bonded to 3 other
atoms, but one of them was able to share 2 electrons (a double bond), carbon would still have a full
valency of 8 electrons.

According to the Valence Bond Theory, such single and double bonds have different electron
structures. Single bonds are named “sigma (s) bonds”, and are caused by the head-on overlapping
between atomic orbitals. Sigma Bonds are the strongest type of covalent bond. Double bonds are
named “pi (p) bonds”, and result from electron overlap in the nodal plane which passes through
both of the bonding atoms. Double bonds are weaker, but still resilient.

Many organic molecules display alternating paths of single and double bonds. In this configuration,
every atom is connected with precisely one double bond. This is named conjugation,
and can increase molecular stability. Conjugation implies the possibility of different resonance
structures, where every double bond shifts in one direction to obtain a different representation of
1
the same molecule. The amount of such resonance structures is a measure of stability. The actual
molecule results from the superposition of all resonance contributors.

Each of the nodal lobes involved in pi bond conjugation allow their electrons to delocalize
across the molecule. Since electrical current is the flow of electrons, such alternating paths are
postulated to be electrically conductive [1, 4]. When electricity (specifically a ‘soliton’) is ran
through a conjugated system, all single and double bonds are interchanged [4].

This allows some molecules to display a ‘switching’ property. A channel is defined as a path
through a molecule. A channel is open when the path is alternating, and closed otherwise. When
some alternating paths are toggled, other paths may be opened or closed. This resembles the
behavior of circuitry, and is proposed as a basis for molecular computation. This proposal is quite
speculative.

<b>2 Literature Review</b>

Hesselink et al. [1, 2] has previously shown that the switching behaviour can be completely described
using Kekule Theory. Graph theory is first used to model cyclic unsaturated hydrocarbons,
where atoms are abstracted as nodes, and edges represent chemical covalent bonds. These graphs
neglect all hydrogen atoms, as they do not contribute to conjugation.

Double bonds are represented using a pairwise disjoint subgraph, where every edge in the
subgraph represents a double bond. Pairwise because a double bond reaches two vertices, and
disjoint because double bonds are seen at every other position in an alternating path. It is possible
to give every carbon atom precisely one double bond if its graph has a ‘perfect matching’. Each
perfect matching corresponds to a single resonance structure.

Certain vertices are labelled ‘ports’ are are not required to contain a double bond. Therefore,
our matchings can contain imperfections at the ports. Ports are where the molecule connects to
the ‘outside world’. This could allow not only connectivity between molecules, but locations to
observe and influence molecular behaviour. Anything can be attached to a port, as it does not affect
the interchanging of bonds or the switching behaviour.

Each graph is associated with a Kekule cell, which consists of all the possible stable double
bond configurations of that molecule. This is recorded by naming the ports, and labelling each
configuration based on which ports contain double bonds. From this, Hesselink has classified all
possible Kekule cells with ports  5. He has also classified 210 out of 214 possible Kekule cells
with 6 ports.This means nearly any molecule with 6 or less ports has the exact same ‘switching
behavior’ as one of the structures found by Hesselink. However, results obtained by Hesselink are
graphs which only represent the Kekule cell, not graphs which also resemble molecules.

<b>3 Motivation and Proposed Work</b>

We derive our motivation from Prof. Hesselink’s work. Let us start with a quote. 

“For application
to carbon chemistry, it would be interesting to see whether all Kekule cells ... can be realized in
2
stable molecules” - Hesselink, 2013 [1].

This area of research is relatively new. To our knowledge, of the few studies that have been
done, none of them have made any attempt to obtain realistic graphs. For our contribution, we
would like to first, create our own software framework to confirm previous results. We would
then like to attempt to find alternate more realistic structures for each one given in Hesselinks
classification.

If we want a molecule with a certain switching behaviour, the search can be split into three
sections:

1. Search for cells K with the required switching behavior.

2. Search for graphs G which have cell K.

3. Search for suitably alternating hydrocarbon molecules that have such a graph. - Hesselink,
2013 [1].

Our research attempts to bridge the gap between step 2 and 3, now that Hesselink [1] has made
strong headway in step 2. We approach the problem first, by adding multiple restrictions to our
resulting graphs.

“In view of the application to conjugation in carbon chemistry, we could restrict attention to
graphs where all nodes degrees  4” - Hesselink et al., 2007 [2].

Hesselink himself has said that graphs could be restricted so nodes have degrees of 4 or less.
However, we feel this is not strict enough. Every atom in such conjugated systems is involved
in a double bond (or else the structure wouldnt be stable). Since double bonds are seen only in
subgraphs, a node should be at maximum allowed to connect to 3 distinct vertices.

What about ports? Ports aren’t required to have a double bond in order for the structure to
be stable. However, in most molecules, at least one configuration involves a double bond at any
given port. Additionally, ports are defined as atoms which “other chemical groups can be attached
to observe and influence behavior” [1]. This means ports must have: (1) The capacity to form
a double bond, and (2) One bond reserved to connect to outside chemical groups. Therefore we
restrict ports to at maximum, be allowed to connect to 2 distinct vertices. Other than the degree of
vertices, there are other inconsistencies with some of Hesselinks results [1]. Graphs are permitted
to be disjoint. An unconnected graph really represents two molecules, not one, with no feasible
means of conjugation between them. Therefore, results must also be limited to connected graphs.
Other unstable structures such as 3 membered rings of carbon (which appear in some graphs) are
sterically unfavourable and should be avoided.

<b>4 Challenges</b>

There are many challenges with such an approach. How do we find a graph for a given cell? The
current approach involves searching for a smaller graph whose cell is a subset of the required cell.
3
We then add edges to our graph, slowly approximating our final cell. It is not currently known
whether it is possible to make an algorithm which determines whether a given cell is Kekule.
Hesselink’s [1] program is capable of enumerating all graphs, and testing each of them to see if
their cell matches the input. However, if a cell was not Kekule, Hesselink’s program would search
forever. Therefore the class of Kekule cells is currently semi-decidable.

Additionally, the time complexity of the current approach is quite large. It takes many hours
just to classify all cells of order 6. For this reason, Hesselink has used a finite set of verticies and
edges. This also means his algorithm will always terminate, although it will not always give a
solution when it does. When searching for cells of order 6, Hesselink was not able to find graphs
for 4 of them because of the limited vertex/edge set. However, allowing more components in the
graph is computationally prohibitive due to the large growth rate. Considering we intend to search
for graphs with much more restrictions than Hesselink, it is likely some graphs will be unfindable.

This suggests the possibility of rather than searching for restricted structures, to simply edit
Hesselink’s structures. The editing of a graph without changing its Kekule cell has been studied in
[1, 2, 3]. Hesselink et al. [2] shows a way to split a node of high degree into two nodes of lower
degree, and even shift edges across verticies. M.H. van der Veen [3] outlines eight topological
operations used algorithmically to create omniconjugated systems (alternating path between all
ports). Perhaps its possible to create a similar algorithm which edits graphs towards our restrictions
rather than omniconjugation.

<b>5 Work Plan</b>

First we intend to completely familiarize ourselves with Hesselink’s work. This will involve studying
his C program at the theoretical level, as well as being comfortable with its execution. We will
then begin to create our own software framework in Java. We will confirm Hesselink’s results and
attempt to add restrictions of our own such as limited degrees and connectedness. Based on our
results, we will begin to edit our new graphs to remove steric hinderance and other inconsistencies
between our graphs and organic molecules. In order for us to state our graphs represent realistic
molecules, we will likely need to search for existing organic molecules which resemble our
generated structures.

<b>6 More Details</b>

For a much more thorough review see the document here:
https://github.com/germuth/Kekule/blob/master/Documents/Comprehensive%20Everything%20Document.pdf

Or see the published article at:
NANOARCH 2015, “From Kekule Cells to Molecular Switches”

In programming there are many directories:
Kekule -> Original program by Hesselink in C (with some minor modifications)
Kekule Java -> Translated program in java with many additions

Main is located here:
https://github.com/germuth/Kekule/blob/master/Programming/Kekule%20Java/Kekule/src/all/Main.java

Finally, for an idea of some future directions:
https://github.com/germuth/Kekule/blob/master/Aaron%2C%20when%20you%20work%20on%20this%20again.txt

<b>References</b>

[1] W. H. Hesselink, Graph Theory for alternating hydrocarbons with attached ports. Indagationes
Mathematicae, Elsevier, 24:115141, 2013.

[2] W.H. Hesselink, J.C. Hummelen, H.T. Jonkman, H.G. Reker, G.R. Renardel de Lavalette,
M.H. van der Veen, Kekule Cells for Molecular Computation. Cornell University Library
Online, 2013.

[3] M.H. van der Veen. p-Logic. PhD thesis, University of Groningen, May 2006.
4

[4] A.J. Heeger, S. Kivelson, J.R. Schrieffer, and W.-P Su. Solitons in conducting polymers,
Rev. Mod. Phys.,60:781, 1988.
5

