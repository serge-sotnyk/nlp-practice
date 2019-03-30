# Dynamic Models of Choice with Better Graphic Tools and Quicker Computations 

_ggdmc_, evolving from dynamic model of choice (_DMC_, Heathcote et al., 2018),
is a generic tool for hierarchical Bayesian Computations. 

1. Instead of using Gibbs or HMC, _ggdmc_ uses population-based MCMC (pMCMC) 
samplers. A notable Gibbs example is the Python-based 
HDDM (Wiecki, Sofer & Frank, 2013), which does not allow the user to 
conveniently set the variabilities of DDM parameters. 

2. _ggdmc_ uses a different variant of _migration_ operator, which safeguards
the detailed balance. It is not imperative to turn off the _migration_ 
operator.  For some complex models, it is preferalbe to use a mixture of 
differernt genetic operators to prevent premature convergence. Further, pMCMC 
is more efficient when a combination of operators is used. 

3. _ggdmc_ uses two parallel methods. First is via the _parallel_ package in R.
This facilitates the computations for fitting many participants, namely 
fixed-effects models.  The second is via OpenMP at C++ level. This facilitates 
the computations for fitting hierarchical models. For an advanced parallel 
computation technique / algorithm, please see my R package, 
[_ppda_](https://github.com/yxlin/ppda), which implements CUDA C language for 
massive parallel computations.

## Getting Started
Below is an example using the LBA Model (Brown & Heathcote, 2008). 
Please see my [tutorials site](https://yxlin.github.io/) for more details. 
The names of _R_ functions in _ggdmc_ mostly informs what they are doing, such
as _BuildModel_. The syntax differs from DMC; Nevertheless, although _ggdmc_
seemingly similar with DMC, its core of Bayesian sampling is a new 
implementation, because the different method of parallelism and pMCMC 
algorithms. Please use with your own risk. 

Note the sequence of parameters in a parameter vector (i.e., p.vector) must 
strictly follow the sequence in the _p.vector_ reported by _BuildModel_. 
Otherwise, _run_ function will throw an error message to _stop_  you from 
fitting a model.

```
require(ggdmc) 
model <- BuildModel(p.map = list(A = "1", B = "R", t0 = "1",
                            mean_v = c("F", "M"), sd_v = "M", st0 = "1"),
          match.map = list(M = list(s1 = 1, s2 = 2)),
          factors   = list(S = c("s1", "s2"), F = c("f1", "f2")),
          constants = c(sd_v.false = 1, st0 = 0), 
          responses = c("r1", "r2"),
          type      = "norm")

## Population distribution, rate effect on F
pop.mean <- c(A = .4, B.r1 = 1.2, B.r2 = 2.8, t0 = .2,
              mean_v.f1.true = 2.5, mean_v.f2.true = 1.5, mean_v.f1.false = .35,
              mean_v.f2.false = .25, sd_v.true = .25)
pop.scale <- c(A = .1, B.r1 = .1, B.r2 = .1, t0 = .05,
               mean_v.f1.true = .2, mean_v.f2.true = .2, mean_v.f1.false = .2,
               mean_v.f2.false = .2, sd_v.true = .1)
pop.prior <- BuildPrior(
  dists = rep("tnorm", 9),
  p1    = pop.mean,
  p2    = pop.scale,
  lower = c(0,   0,  0, .1, NA, NA, NA,  0,  0),
  upper = c(NA, NA, NA,  1, NA, NA, NA, NA, NA))

## Draw parameter prior distributions to visually check
plot(pop.prior)
print(pop.prior)

## Simulate 20 participants, each condition has 30 responses.
## The true parameter vectors are drawn from parameter prior distribution
## specified in 'pop.prior' 
dat <- simulate(model, nsim = 30, nsub = 20, prior = pop.prior)
dmi <- BuildDMI(dat, model)    ## dmi = data model instance 

## Extract the mean and variabilities of parameters across the 40 participants
## ps <- attr(dat, "parameters")
##
## Please use matrixStats package, which is even faster than the C functions 
## in base package
##
## round(matrixStats::colMeans2(ps), 2)
## round(matrixStats::colSds(ps), 2)
##    A  B.r1  B.r2  mean_v.f1.true  mean_v.f2.true mean_v.f1.false 
## 0.43  1.22  1.00            0.21            2.48            1.45 
## 0.10  0.10  0.01            0.04            0.17            0.19 
## mean_v.f2.false  sd_v.true     t0
##            0.34       0.36   0.23
##            0.16       0.18   0.10
           
## FIT hierarchical model
p.prior <- BuildPrior(
  dists = rep("tnorm", 9),
  p1    = pop.mean,
  p2    = pop.scale,
  lower = c(0,   0, 0, .1, NA, NA, NA,  0,  0),
  upper = c(NA, NA, 1, NA, NA, NA, NA, NA, NA))

## Specify prior distributions at the hyper level
mu.prior <- BuildPrior(
  dists = rep("tnorm", 9),
  p1    = pop.mean,                           
  p2    = c(1,   1,  1,  2,   2,  2,  2,  1, 1),
  lower = c(0,   0,  0, .1,  NA, NA, NA, NA, 0),
  upper = c(NA, NA, NA, NA,  NA, NA, NA, NA, NA))

## lower and upper are taken care of by defaults.
sigma.prior <- BuildPrior(
  dists = rep("beta", 9),
  p1    = c(A=1, B.r1=1, B.r2=1, t0 = 1, mean_v.f1.true=1, mean_v.f2.true=1,
            mean_v.f1.false=1, mean_v.f2.false=1, sd_v.true = 1),
  p2    = rep(1, 9))

pp.prior <- list(mu.prior, sigma.prior)

## Visually check mu priors and sigma priors
plot(pp.prior[[1]])
plot(pp.prior[[2]])

## Initialise a small sample 
## Get the number of parameters
npar <- length(GetPNames(model)); npar
thin <- 2

## Initiate 100 new hierarchical samples and specify (randomly) only the first 
## iteration.  Others are NA or -Inf. 
hsam <- StartNewHypersamples(1e2, dmi, p.prior, pp.prior)
hsam <- run(hsam, report = 20, pm = .3, hpm = .3)

```

## How to pipe DMC samples to _ggdmc_ samplers 
Diffusion decision model (Ratcliff & McKoon, 2008) is one of the most popular 
cognitive models to fit RT data in cognitive psychology.  Here we 
show two examples, one fitting the LBA model and the other fitting DDM.  


```
###################
##   LBA model   ##
###################
## DMC could be downloaded at "osf.io/pbwx8".
setwd("~/Documents/DMCpaper/")
source ("dmc/dmc.R")
load_model ("LBA","lba_B.R")
setwd("~/Documents/ggdmc_paper/")
## load("data/dmc_pipe_LBA.rda")

model <- model.dmc(p.map = list( A = "1", B = "R", t0 = "1",
                                mean_v = c("F", "M"), sd_v = "M", st0 = "1"),
          match.map = list(M = list(s1 = 1, s2 = 2)),
          factors = list(S = c("s1", "s2"), F = c("f1", "f2")),
          constants = c(sd_v.false = 1, st0 = 0),
          responses = c("r1", "r2"),
          type = "norm")
pop.mean <- c(A=.4, B.r1=.6, B.r2=.8, t0=.3, mean_v.f1.true=1.5, 
              mean_v.f2.true=1, mean_v.f1.false=0, mean_v.f2.false=0,
              sd_v.true = .25)
pop.scale <-c(A=.1, B.r1=.1, B.r2=.1, t0=.05, mean_v.f1.true=.2, 
              mean_v.f2.true=.2, mean_v.f1.false=.2, mean_v.f2.false=.2,
              sd_v.true = .1)
pop.prior <- prior.p.dmc(
  dists = rep("tnorm",9),
  p1    = pop.mean,
  p2    = pop.scale,
  lower = c(0,0,0,NA,NA,NA,NA,0,.1),
  upper = c(NA,NA,NA,NA,NA,NA,NA,NA,1))
raw.data <- h.simulate.dmc(model, p.prior = pop.prior, n = 30, ns = 20)
data.model <- data.model.dmc(raw.data, model)

ps <- attr(raw.data, "parameters")

p.prior <- prior.p.dmc(
  dists = rep("tnorm",9),
  p1    = pop.mean,
  p2    = pop.scale*5,
  lower = c(0,0,0,NA,NA,NA,NA,0,.1),
  upper = c(NA,NA,NA,NA,NA,NA,NA,NA,NA))
mu.prior <- prior.p.dmc(
  dists = rep("tnorm",9),
  p1    = pop.mean,
  p2    = c(1,1,1,2,2,2,2,1,1),
  lower = c(0,0,0,NA,NA,NA,NA,0,.1),
  upper = c(NA,NA,NA,NA,NA,NA,NA,NA,NA))
sigma.prior <- prior.p.dmc(
  dists = rep("beta", 9),
  p1    = c(A=1, B.r1=1, B.r2=1, t0=1, mean_v.f1.true=1, mean_v.f2.true=1, 
            mean_v.f1.false=1, mean_v.f2.false=1, sd_v.true = 1),
  p2    = rep(1,9))
pp.prior <- list(mu.prior, sigma.prior)

hsamples <- h.samples.dmc(nmc = 50, p.prior, data.model, pp.prior = pp.prior,
  thin = 1)

## Piping 
hsam0 <- ggdmc::run(hsamples, pm = .05, report = 10)


## Turn off migration. Default pm = 0
hsam1 <- ggdmc::run(h.samples.dmc(nmc = 50, p.prior, samples = hsam0, 
  pp.prior = pp.prior, thin = 1))
hsam2 <- ggdmc::run(h.samples.dmc(nmc = 50, p.prior, samples = hsam1,
   pp.prior = pp.prior, thin = 1))
hsam3 <- ggdmc::run(h.samples.dmc(nmc = 50, p.prior, samples = hsam2,
  pp.prior = pp.prior, thin = 1))

## Check whether MCMC converge
plot(hsam3, pll = TRUE)
plot(hsam3)


hest1 <- summary(hsam3, hyper = TRUE, recovery = TRUE, ps = pop.mean)
hest2 <- summary(hsam3, hyper = TRUE, recovery = TRUE, ps = pop.scale, type = 2)
est <- summary(hsam3)


###################
##   DDM         ##
###################
rm(list = ls())
setwd("~/Documents/DMCpaper")
source ("dmc/dmc.R")
load_model ("DDM", "ddm.R")
setwd("~/Documents/ggdmc_paper/")
## load("data/hierarchical/dmc_pipe_DDM.rda")
model <- model.dmc(
    p.map     = list(a = "1", v = "F", z = "1", d = "1", sz = "1", sv = "1",
                     t0 = "1", st0 = "1"),
  match.map = list(M = list(s1 = "r1", s2 = "r2")),
  factors   = list(S = c("s1", "s2"), F = c("f1", "f2")),
  constants = c(st0 = 0, d = 0),
  responses = c("r1", "r2"),
  type      = "rd")
  
## Population distribution
pop.mean <- c(a=2,  v.f1=4, v.f2=3, z=0.5, sz=0.3, sv=1, t0=0.3)
pop.scale <-c(a=0.5,v.f1=.5,v.f2=.5,z=0.1, sz=0.1, sv=.3,t0=0.05)
pop.prior <- prior.p.dmc(
   dists = rep("tnorm", 7),
   p1    = pop.mean,
   p2    = pop.scale,
   lower = c(0,-5, -5, 0, 0, 0, 0),
   upper = c(5, 7,  7, 1, 2, 1, 1) )

raw.data   <- h.simulate.dmc(model, p.prior = pop.prior, n = 32, ns = 8)
data.model <- data.model.dmc(raw.data, model)
ps <- attr(raw.data, "parameters")

p.prior <- prior.p.dmc(
  dists = c("tnorm","tnorm","tnorm","tnorm","tnorm","tnorm","tnorm"),
  p1=pop.mean,
  p2=pop.scale*5,
  lower=c(0,-5, -5, 0, 0, 0, 0),
  upper=c(5, 7,  7, 1, 2, 1, 1)
)

mu.prior <- prior.p.dmc(
  dists = c("tnorm","tnorm","tnorm","tnorm","tnorm","tnorm","tnorm"),
  p1=pop.mean,
  p2=pop.scale*5,
  lower=c(0,-5, -5, 0, 0, 0, 0),
  upper=c(5, 7,  7, 1, 2, 1, 1)
)
sigma.prior <- prior.p.dmc(
  dists = rep("beta", length(p.prior)),
  p1=c(a=1, v.f1=1,v.f2 = 1, z=1, sz=1, sv=1, t0=1),
  p2=c(1,1,1,1,1,1,1),
  upper=c(2,2,2,2,2,2,2)
)

pp.prior <- list(mu.prior, sigma.prior)
  
## Sampling  
hsam0 <- ggdmc::run(h.samples.dmc(nmc = 512, p.prior = p.prior, 
      pp.prior = pp.prior, data = data.model, thin = 2), pm = .1)

hsam1 <- ggdmc::run(h.samples.dmc(nmc = 512, p.prior = p.prior, 
      pp.prior = pp.prior, samples = hsam0, thin = 32), pm = .1)

hsam2 <- ggdmc::run(h.samples.dmc(nmc = 512, p.prior = p.prior, 
      pp.prior = pp.prior, samples = hsam1, thin = 128), pm = .3)

hsam3 <- ggdmc::run(h.samples.dmc(nmc = 512, p.prior = p.prior, 
      pp.prior = pp.prior, samples = hsam2, thin = 2))

```

## How to fit fixed-effect model with multiple participants

```
require(ggdmc)
## Model Setup----------
model <- BuildModel(p.map = list( A = "1", B = "R", t0 = "1",
   mean_v = c("F", "M"), sd_v = "M", st0 = "1"),
   match.map = list(M = list(s1 = 1, s2 = 2)),
   factors = list(S = c("s1", "s2"), F = c("f1", "f2")),
   constants = c(sd_v.false = 1, st0 = 0),
   responses = c("r1", "r2"),
   type = "norm")
   
npar <- length(model)

## Population distribution, rate effect on F
pop.mean <- c(A = .4, B.r1 = .6, B.r2 = .8, t0 = .3, mean_v.f1.true = 1.5,
  mean_v.f2.true = 1, mean_v.f1.false = 0, mean_v.f2.false = 0, sd_v.true = .25)
pop.scale <-c(A = .1, B.r1 = .1, B.r2 = .1, t0 = .05, mean_v.f1.true = .2,
  mean_v.f2.true = .2, mean_v.f1.false = .2, mean_v.f2.false = .2, sd_v.true = .1)
pop.prior <- BuildPrior(
  dists = rep("tnorm", npar),
  p1    = pop.mean,
  p2    = pop.scale,
  lower = c(0,   0,  0, NA, NA, NA, NA, 0, .1),
  upper = c(NA, NA, NA, NA, NA, NA, NA, NA, 1))

## Simulate some data
nsubject <- 8
ntrial <- 1e2
dat <- simulate(model, nsim = ntrial, nsub = nsubject, prior = pop.prior)
dmi <- BuildDMI(dat, model)
ps  <- attr(dat, "parameters")

# round( matrixStats::colMeans2(ps), 2)
# round( matrixStats::colSds(ps), 2)

## FIT FIXED-EFFECT MODEL----------
## Use all truncated normal priors for locations
p.prior <- BuildPrior(
  dists = rep("tnorm", npar),
  p1    = pop.mean,
  p2    = pop.scale * 5,
  lower = c(0,   0,  0, NA, NA, NA, NA,  0, .1),
  upper = c(NA, NA, NA, NA, NA, NA, NA, NA, NA))

thin <- 8
nchain <- npar * 3
migrationRate <- .2
sam <- run(StartManynewsamples(512, dmi, p.prior, thin, nchain),
  pm = migrationRate, ncore = 8)
sam <- run(RestartManysamples(512, sam), pm = migrationRate, ncore = 8)
sam <- run(RestartManysamples(512, sam, thin = 16), pm = migrationRate, ncore = 8)
sam <- run(RestartManysamples(512, sam, thin = 64), pm = migrationRate, ncore = 8)
sam <- run(RestartManysamples(512, sam, thin = 16), pm = migrationRate, ncore = 8)

plot(sam[[6]])
plot(sam)  ## This will take a while, because ploting many participants

```

## How to conduct automatic convergence checks 
One challenge in Bayesian modeling is to make sure posterior samples are from 
target distribuitons.  When using the DE-MCMC sampler to fit very complex models, 
some regions in parameter spaces might be difficult to handle.  Here we provide 
one method to conduct automatic sampling by repeatedly fitting models until 
posterior samples are proper.

First, we convert the first stage samples (i.e., hsam0) to a generic object, 
_hsam_. Then, we use the _repeat_ function to iterate model fits. Meanwhile,
we use _hgelman_ to check whether both the PSRFs at the hyper- and data-level
are smaller than 1.1, suggesting that chains are well mixed. 

```
thin <- 2
hsam <- hsam0
counter <- 1
repeat {
  hsam <- run(RestartHypersamples(5e2, hsam, thin = thin),
    pm = .3, hpm = .3)
  save(hsam, file = "data/tmp_posterior_samples.rda")
  rhats <- hgelman(hsam)
  counter <- counter + 1
  thin <- thin * 2
  if (all(rhats < 1.1) || counter > 1e2) break
}


```

## List of models currently hard-wired in _ggdmc_
1. The LBA model, type = "norm",
2. The DDM, type = "rd",
3. The Piecewise LBA model 0; CPU-based PDA likelihoods; type = "plba0",
4. The Piecewise LBA model 1; CPU-based PDA likelihoods; type = "plba1", 
5. The Piecewise LBA model 0; GPU-based PDA likelihoods; type = "plba0_gpu", 
6. The Piecewise LBA model 1; GPU-based PDA likelihoods; type = "plba1_gpu", 
7. The LBA model; GPU-based PDA likelihoods;, type = "norm_pda_gpu",
8. The correlated accumualtor model; type = "cnorm".

For the details regarding PLBA types, please see 
[Holmes, Trueblood, and Heathcote (2016)](http://dx.doi.org/10.1016/j.cogpsych.2015.11.002)

## Further information  
Please see my [tutorials site, Cognitive Model](https://yxlin.github.io/), for 
more details.

## Prerequisites
 - R (>= 3.4.0)
 - Rcpp (>= 0.12.10), RcppArmadillo (>= 0.7.700.3.0), ggplot2 (>= 2.1.0),
   rtdists (>= 0.6-6), ggmcmc (>= 0.7.3), 
   coda (>= 0.16-1) tmvtnorm, matrixStats, data.table
 - Windows users need Rtools (>= 3.3.0.1959) 
 - Mac OS users need to make clang understand OpenMP flag
 - Linux/Unix users may need to install Open MPI library, if it has not 
   been installed. 
 - [Armadillo](https://CRAN.R-project.org/package=RcppArmadillo)
   requires a recent compiler; for the g++ family at least version 4.6.*

## Installation

CRAN method is currently unavailable. The latest version of the package is still 
in the process of CRAN standard software checks.

~~From CRAN: ~~
~~> install.packages("ggdmc")~~

From source: 

> install.packages("ggdmc_0.2.5.2.tar.gz", repos = NULL, type="source")

From GitHub (you will need to install _devtools_:

> devtools::install_github(“yxlin/ggdmc”)

For Mac Users:

1. You will need to install [gfortran](https://gcc.gnu.org/wiki/GFortranBinaries#MacOS).
As to 27, Aug, 2018, please install gfortran 6.1, even you are using a mscOS 
High Sierra Version 10.13.4. gfortran 6.3 may not work.

2. Then install clang4-r. 
[James Balamuta](https://thecoatlessprofessor.com/programming/openmp-in-r-on-os-x/)
has created a convenient tool, [clang4-r](https://uofi.app.box.com/v/r-macos-clang-pkg).
Once you install clang4-r, your clang will then understand the OpenMP flag
in _ggdmc_. You may use other methods he suggests to allow Mac to understand
OpenMP flag, but they are usually less straightforward.

Please visit his site for detailed explanations about the clang-OpenMP issue. 

## Citation

If you use this package, please cite the software, for example:

Lin, Y.-S., & Heathcote, A. Population-based Monte Carlo is as Effective as 
Hamiltonian Monte Carlo in Fitting High Dimension Cognitive Model. Manuscript 
in preparation.  Manuscript in preparation. 
Retrieved from https://github.com/yxlin/ggdmc

Lin, Y.-S., Heathcote, A., & Holmes, W. R (submitted). Parallel Probability 
Density Approximation. Behavior Research Methods.

Lin, Y.-S., Strickland, L., Reynold, A., & Heathcote, A. 
(manuscript in preparation). Tutorial on Bayesian cognitive modeling.


## Contributors

The R documentation, tutorials, C++ codes, R helper functions and pacakging are 
developed by Yi-Shin Lin. DMC is developed by Andrew Heathcote 
(Heathcote et al., 2018). Please report bugs to [me](mailto:yishin.lin@utas.edu.au). 

## License

GPL-2 

## Acknowledgments

* Early version of density.cpp is based on Voss & Voss's (2012) density.c in 
fast-dm 30.2. 
* Early version of the truncated normal distributions is  based on Jonathan 
Olmsted's <jpolmsted@gmail.com> RcppTN 0.1-8 (https://github.com/olmjo/RcppTN) 
and Christopher Jackson's <chris.jackson@mrc-bsu.cam.ac.uk> R codes in msm package. 
* Armadillo is a collection of C++ library for performing linear
algebra <http://arma.sourceforge.net/>, authored by Conrad Sanderson. 
* Thanks to Matthew Gretton's consulation about rtdists. 
* Thanks to Andrew Heathcote for lending MacBook Air for facilitating tests of
ggdmc on OS X (mscOS High Sierra Version 10.13.4) 

