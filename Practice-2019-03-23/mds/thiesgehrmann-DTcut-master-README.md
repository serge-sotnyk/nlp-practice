DT-cut
======

Dynamic Test Cut: A general purpose tool to dynamically cut a tree based on a statistical test with dynamic testing correction at each node.

It is, in essence, a general purpose implementation of the dynamic tree cutting algorithm in [Proteny](https://github.com/thiesgehrmann/proteny#proteny).

![An example output from DT-cut](https://raw.githubusercontent.com/thiesgehrmann/DTcut/master/example_data/example_output/GO:0008152.tsv.dtcut.png)

## Dependencies

For the core library functionality, you must have installed:
* Numpy: http://www.numpy.org/
* Scipy: http://www.scipy.org/

If you want to use the provided execution wrapper 'cluster_test.py', then you must also install:
* Fastcluster: https://pypi.python.org/pypi/fastcluster
* IBIDAS: https://pypi.python.org/pypi/Ibidas
* Matplotlib: http://matplotlib.org/

## Example usage

```python
  # Given:
  #  X: An (NxM) numpy matrix of feature vectors for N objects, each of length M.
  #  L: An (Nx1) numpy array of boolean values describing labels for each object.
  #  IDS: A list of length N containing identifiers for each object.
  #  D: a linkage from scipy.linkage(X) or Fastcluster.linkage(X)

import dtcut as dtcut;
from EnrichmentTest import TEST;

  # Prepare the DTcut algorithm
T    = dtcut.prepare_tree(D);
tree = dtcut.DTCUT(T);

  # Prepare the statistical test
stat_test = TEST.Test(tree, IDS, X, L);
stat_func = lambda i_node: stat_test.test(i_node);

  # Set your parameters
pvalue_thresh = 0.05;
min_set_size  = 20;

  # Test the tree, getting significant node IDS
S = tree.test_tree(stat_func, pvalue_thresh, min_set_size);

  # For each leaf, get a cluster label
  # C[i] = cluster_id.
  # if C[i] = j < 0, the leaf is not in a significant cluster.
  # if C[i] = j > 0, the leaf is in significant cluster j.
C = tree.get_clusters(S);

  # Get information for each cluster
  # Returns
  # * Height of node in dendrogram
  # * p-value of node
  # * leaf members
I = tree.get_clusters_info(S, IDS);
```

### Example 
Example data in /example_data is prepared from:

* [Gasch et al. (2000) Mol. Biol. Cell. 11(12) 4241-4257](http://genome-www.stanford.edu/yeast_stress/gasch.pdf) [RAW](http://genome-www.stanford.edu/yeast_stress/data/rawdata/complete_dataset.txt)
* [Cherry JM, et al. (2012) Nucl. Acids 40(D)  700-705](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3245034/pdf/gkr1029.pdf) [RAW](http://downloads.yeastgenome.org/curation/literature/gene_association.sgd.gz)

The example can be run with the following command:
```
./cluster_test.py example_data/gene_ids.tsv example_data/expression_matrix.tsv correlation complete EnrichmentTest.py 0.05 20 80 ./ True example_data/GO\:0008152.tsv
```

It produces output like that seen in file [/example_data/example_output/GO:0008152.tsv.dtcut.tsv](https://raw.githubusercontent.com/https://github.com/thiesgehrmann/DTcut/blob/master/example_data/example_output/GO:0008152.tsv.dtcut.tsv).


