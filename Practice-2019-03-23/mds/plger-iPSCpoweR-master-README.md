# The iPSCpoweR package

This package provides resources for exploring large transcriptomics datasets from human induced pluripotent stem cell (iPSC) lines, run large numbers of differential expression analyses across random groups of individuals, in order to approximate power and guide experimental design. This vignette will guide you through its main usage.

<br/><br/><br/>
      
        
# Installing the package

To install the package, download it and install it using the following R command:
```
install.packages("path/to/iPSCpoweR.tar.gz", repos=NULL)
```

Alternatively, if you have `devtools` installed you can install the package directly from the git repository using:
```
library(devtools)
install_git("https://github.com/plger/iPSCpoweR", build_vignettes=TRUE)
```

Building the vignette might take a couple of minutes. Once the package is installed, you can load it and access this vignette:
```
library(iPSCpoweR)
vignette("iPSCpoweR")
```

<br/><br/><br/>


# Data included in the package

The main dataset included in this package was released by the Human Induced Pluripotent Stem Cell Initiative (HipSci), quantified with Salmon v6.1, using FMD indexes and the Refseq transcript annotation. You can use the `getSamplesInfo()` function to have an overview of the samples, and `data("hipsci_annotation")` to access the samples' annotation.

The package's functions take care of loading and handling the data. If you wish to access the data for other purposes, see the `getTxExpr` and `getGeneExpr` functions. To aggregate technical replicates, see the `aggByClone` function.

### Using the GSE79636 dataset

The data from Carcamo-Orive et al. (Cell Stem Cell 2016) is also included in the package to allow its usage in the permutation DEA analyses. To do so, you must first load the GSE79636 object, which contains both the expression and annotation matrices:
```
data("GSE79636")
summary(GSE79636)

##            Length Class      Mode
## annotation  20    data.frame list
## dat        317    data.frame list
```

Then you can pass this object to any of the DEA permutation functions through the `res` argument:
```
DEA.permutateIndividuals(nbIndividuals = 3, res=GSE79636)
```

### Using a custom dataset

A custom dataset could be used in a similar fashion. You must simply pass to the `res` argument a list containing two slots:

- `dat` : the expression matrix, with samples as columns and features as row names.
- `annotation` : the annotation matrix, with each row corresponding to a column in `dat`, and with at least the columns `sex` and `individual`.


<br/><br/><br/>
      

# Permutation DEA analysis across the HipSci open dataset

The package runs differential expression analyses (DEA) on random groups of samples using two functions, related to types of grouping:

<p style="text-align: center;"><img src="vignettes/permu_schemes.png" alt="Permutation schemes" width=75%/></p>

By default, the permutation functions are multithreaded, using `detetedCores()-1` threads. This can be adjusted through the `ncores` arguments, and multithreading can be disabled using `ncores=1`.

## DEA.permutateIndividuals

The `DEA.permutateIndividuals` function constitutes, for each permutation, random groups of sex-balanced individuals. By default, the function will run up to 300 DEA (depending on how many different permutations are possible), each on random but sex-balanced groups of 2 individuals, using 2 iPSC clones per individual.

The (maximum) number of permutations can be changed with the `maxTests` argument; the number of individual per group can be changed using the `nbIndividuals` argument, and the number of clones (either 1 or 2) can be changed using the `nbClone` argument.

The default function does not add true/known differential expression (necessary for estimates of sensitivity), and the results can accordingly only be used for specificity analysis. To include differential expression and assess the proportion of it detected, set `addDE=TRUE` (see `?DEA.permutateIndividuals` for more details). We'll run this example single-threaded (`ncores=1`):

```
DEA.permutateIndividuals(nbIndividuals = 3, maxTests = 10, nbClone = 2, addDE=TRUE, ncores = 1)

## Aggregating transcript counts to gene-level...
## Running 10 differential expression analyses
## Results saved in 3indiv.vs.3indiv.2.RData
```

By default, the results (both a R object and summary figures) will be saved in the current working directory, although this behavior can be changed by setting `doSave=FALSE, returnResults=TRUE`.

A number of other parameters can be altered; see `?DEA.permutateIndividuals` for more information.

## DEA.permutateClones

The `DEA.permutateClones` function selects random individuals for each permutation, and puts one iPSC clone of each individual in each of two groups, so that each group contains different clones from the same set of individuals. By default, the function will run up to 300 DEA (can be changed with the `maxTests` argument), using groups based on 2 individuals (can be changed using the `nbIndividuals` argument).

The output, as well as most of the options (including the addition of differential expression) are as in the `DEA.permutateIndividuals` function. The function however has an additional feature, controlled by the `paired` argument: if set to TRUE, the differential expression will not be performed using the classical method (edgeR with exact test), but using GLM in order to pair the clones of the same individuals, i.e. using the model `~individual+group`. By default, pairing is disabled.

For more information, see `?DEA.permutateClones`.

## Output files

if `doSave=TRUE` (default), 3 or 4 output files are produced, each with either of the following prefix:

* `[x]indiv.vs.[x]indiv.[y]` for results of the `DEA.permutateIndividuals` function, where x is the number of individuals per group and y the number of clones (e.g. 2indiv.vs.2indiv.1).
* `clones.[x]indiv.[paired]` for results of the `DEA.permutateClones` function, where x is the number of individuals and [paired] indicates if a paired analysis was performed.

The output files are:

1. *.RData : a R object containing all the results as well as the call.
2. *Nsig.svg : a histogram of the number of `spurious` differentially-expressed genes for each permutation.
3. *logFC.svg : a histogram of the foldchange of the `spurious` differentially-expressed genes.
4. *sensitivity.svg : (only if `addDE=TRUE`) a heatmap of the sensitivity at different foldchanges and expression levels, as produced by the `getSensitivityMatrix()` function.

### Extracting true and false positives from the results

The simplest way of extracting the distributions of true positives (TP) and false positives (FP) from the results of permutation DEA is through the 
`readPermResults` function:
```
pm <- readPermResults("3indiv.vs.3indiv.2.RData")
```

The function returns a list, with each element being the results of one set of permuations. In other words, multiple filenames could be passed to the `readPermResults` function, but right now we have only one:
```
lapply(pm[[1]],FUN=head)
## $nbComps
## [1] 10
## 
## $FP
##  V1  V2  V3  V4  V5  V6 
##  31 286 126  37  41  38 
## 
## $TP
## V1 V2 V3 V4 V5 V6 
## 51 55 47 50 42 48 
## 
## $DEGs
##              FDR.below.05 absLog2FC logMeanCount
## SPDYE3                 10  2.321928     2.744059
## CYP46A1                10  2.321928     2.722561
## LOC100101478           10  2.321928     3.816600
## RNF212                 10  2.321928     3.864638
## C19orf40               10  2.321928     4.805020
## NEIL1                  10  1.584963     4.816916
```

Each such object is itself a list containing:

* `nbComps: number of comparisons.
* `FP: number of false (or spurious) positives for each comparison.
* `TP: (only if the permutations were generated with addDE=TRUE) The number of true positives for each comparison.
* `DEGs: (only if the permutations were generated with addDE=TRUE) a data.frame containing, for each gene, the number of times it was found with a FDR below 0.05, the absLog2FC introduced in the input, and the mean fragment count.

The object(s) in this list can then be used to plot sensitivity matrices (assuming that `addDE` was enabled) using `getSensitivityMatrix`, or to plot the distribution of false positives across permutations:
```
getSensitivityMatrix(pm[[1]])
```

<p style="text-align: center;"><img src="vignettes/sensMat.png" alt="sensitivity matrix"/></p>

```
hist(pm[[1]]$FP, xlab="False positives", ylab="Number of permutations",breaks=20)
```

<p style="text-align: center;"><img src="vignettes/hist.png" alt="false positives"/></p>


<div id="plotting-a-roc-curve" class="section level3">
<h3>Plotting a ROC curve</h3>
<p>The packages includes a function to plot a Receiver Operating Characteristic (ROC) curve representing the results of a permutation DEA analysis (assuming that <code>addDE</code> was enabled). The function must <i>not</i> be called on the results of the <code>readPermResults</code> function, which do not include individual p-values, but directly on the results of the permuation analysis, e.g.:</p>
<pre class="r"><code>getPermROC(&quot;3indiv.vs.3indiv.2.RData&quot;)</code></pre>
<p><img src="vignettes/ROC.png"/></p>
<p>By default, the function will plot the median sensitivity and specificity at sliding p-values (the line and points), as well as the 0.05 and 0.95 quantiles across the different permutations (the shaded area). You can disable the shaded area with <code>qprobs=NA</code>. See <code>?getPermROC</code> for more options.</p>

<br/><br/><br/>
      

## Using a different DEA method in the permutations

By default, permutations are done using edgeR, and without any pre-filtering of the tested genes. The functions however give the user the possibility of changing this in two ways.

### Filtering genes before testing

In both functions, you can use the `filter` argument to set a pre-testing filtering rule. The argument should be passed a function which will be applied to each row of the expression matrix, and should return TRUE if the row is to be kept (tested), and false otherwise. For instance, `filter=function(x){ sum(x>10)>2}` would only include genes that have more than 10 fragments in more than 2 samples.

### Using a custom DEA function

The permutation analysis calls the `edgeRwrapper` function to perform the DEA. This function can be replaced by a custom function, or by some of the other functions already implemented (see below), using the `DEAfunc` argument of either `DEA.permutateIndividuals` or `DEA.permutateClones`. For custom functions, the output should be a data.frame with genes as row.names (in the same order in which they were initially given), and the following columns: `logFC`, `PValue`, `FDR`. The best way to get started writing your own function is too look at `edgeRwrapper` or `voomWrapper`.

#### Using the duplicateCorrelation approach for multiple clones

To enable the use of `limma::duplicateCorrelation` (and treat individuals as random effects) in `DEA.permutateIndividuals`, make sure you set `DEAfunc=voomWrapper` and `nested=TRUE`. This feature is not available for edgeR and requires more than one clone per individual.

For example:
```
DEA.permutateIndividuals(nbIndividuals = 3, nbClone = 2, addDE = T, 
    filter = function(x) {
        sum(x > 10) > 2
    }, nested = T, DEAfunc = voomWrapper)
```

Of note, this approach was the best performing in our study.

#### Summing clones' read counts before DEA

You can use the function `voomWrapperSumReps`, which does the same thing as the normal `voomWrapper` function, except that it sums the read counts of clones of the same individual before running the analysis.

#### Using mixed models

Three functions are available to use `lme4`-based mixed models, considering the individual as a random effect:

* `vstLmerWrapper` runs `DESeq2`'s variance-stabilizing transformation (VST), fits the mixed model ~1+(1|individual)+group (assuming that it is called with `nested=TRUE`), and uses the `drop1` test to assess statistical significance.
* `voomLmerWrapper` performs similarly, except that it passes the counts through voom instead of DESeq2's VST,
* `glmmWrapper` fits the mixed moded ~1+(1|individual)+group using `MASS::glmmPLQ` with a quasipoisson dispersion model.

All these methods should be used with the `nested` argument, e.g.:
```
DEA.permutateIndividuals( nbIndividuals = 3, 
	nbClone = 2,
	addDE = T, 
	filter = function(x) { sum(x > 10) > 2 }, 
	nested = T, 
	DEAfunc = vstLmerWrapper )
```

If `nested=F`, the corresponding model without random effect will be used.

Of note, all three methods are very slow, and according to our study less accurate than the approach based on `limma::duplicateCorrelation` (as discussed above).




<br/><br/><br/>
      


# Reproducing the analysis of variance


The analysis of the proportion of transcriptional variance explained by difference between individuals can be reproduced using the `transcriptionalVarianceExplained` function. By default, mixed models are used, treating the individual as a random effect variable. For more detail, see `?transcriptionalVarianceExplained`.

To reproduce the analysis of variance in cellular morphology, see `?cellphenoVarianceExplained`.


<br/><br/><br/>
    
# Reporting issues

Please report issues on the <a href="https://github.com/plger/iPSCpoweR">github repository</a>.

  
<br/><br/><br/>

