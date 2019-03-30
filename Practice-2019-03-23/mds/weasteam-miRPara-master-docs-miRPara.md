# INSTALL

* * *

miRPara was written in perl and developed under Linux. We suggest to run miRPara under linux. But it should be able to run under Mac OS and Windows if all third-party software packages were installed.

**Please Cite:**

MiRPara: a SVM-based software tool for prediction of most probable microRNA coding regions in genome scale sequences. Wu Y., Wei B., Liu H., Li T., Rayner S. BMC Bioinformatics. 2011 Apr 19; 12(1):107

**Required Packages**

_Version 6.0 or above_ 

* Getopt::Long (CPAN) 
* threads (CPAN) 
* threads::shared (CPAN)
* Cwd (CPAN) 
* File::chdir (CPAN) 
* UNAFold (http://mfold.rna.albany.edu/?q=DINAMelt/software'>download) 
* ct2out (http://code.google.com/p/mirpara/downloads/detail?name=ct2out.tar.gz&can=2&q='>download) 
* libsvm ([http://www.csie.ntu.edu.tw/~cjlin/libsvm/](http://www.csie.ntu.edu.tw/~cjlin/libsvm/))

Copy UNAFold.pl, ct2out, svm-predict to $PATH

```
# Install the packages from CPAN

# See the instruction at [http://perl.about.com/od/packagesmodules/qt/perlcpan.htm](http://perl.about.com/od/packagesmodules/qt/perlcpan.htm)

# Open a terminal under linux, type the following to install CPAN packages. (Ignore the "$")

$ perl -MCPAN -e shell

# for ubuntu root, type

$ sudo perl -MCPAN -e shell

# install CPAN packages

cpan> install Getopt::Long cpan> install threads cpan> install threads::shared cpan> install Cwd cpan> install File::chdir

# Install UNAFold

# See the INSTALL in the UNAFold package

# Check the success of installation by typing

$ UNAFold.pl

# if returns "UNAFold.pl: command not found", do the following under the UNAFold.pl folder and test again, you might need to be root to do so.

$ sudo cp UNAFold.pl /use/bin/

# Install ct2out

$ gfortran ct2out.f -o ct2out

# or

$g77 -o ct2out ct2out.f

# then copy ct2out to PATH, you might need to be root to do so

$ sudo cp ct2out /usr/bin/

# Test the ct2out by

$ ct2out

# Failed if returns "ct2out: command not found", success if returns nothing

# Install libsvm

# See the README in the libsvm package

# copy svm-predict to the path, you might need to be root to do so

$ sudo cp svm-predict /usr/bin/
```

_Version 5.3 or below_ 
* Getopt::Long 
* Algorithm::SVM (http://code.google.com/p/mirpara/downloads/detail?name=algorithm_SVM_install_fix.pdf&can=2&q='>click here if you have install problem) 
* Cwd 
* UNAFold (http://mfold.rna.albany.edu/?q=DINAMelt/software'>download) 
* ct2out (http://code.google.com/p/mirpara/downloads/detail?name=ct2out.tar.gz&can=2&q='>download)

Copy UNAFold.pl, ct2out to $PATH

* * *

# USAGE

* * *

**Before Run**

A folder called "models" should be created and placed in the same directory as miRPara.pl, all the models should be copied into this folder. Or just created a link to the models folder and rename the link as "models". (It is not required if the models was provided by "-s" tag, only for version 6.0 or above)

miRPara.pl does not required to be copied to $PATH. If you did so, do copy the model folder links into $PATH.

The _mature.fa_ and _organisms.txt_ was required for the miRPara.pl 6.0 or above. miRPara.pl will check the $PATH and automatically download the files if they were not exist.

The selection of miRPara_model_trainer.pl have to match the miRPara.pl version: 

|Model Trainer Version|miRPara Version|
|:--------------------|:--------------|
|3.0 or above |6.0 or above |
|2.3 or below |5.3 or below |

The previous models do not fit for miRPara.pl 6.0 or above!

**miRPara version 6.0 or above**

```
Usage: miRPara.pl [Options] file [File]

Options: -v, --version -h, --help -s, --species=species group name (defaults as overall) or species short name or path of a model file: /home/xxx/miRPara/model/hsa_10.model -c, --cutoff= (defaults to 0.8) -l, --levels=<1..20>(defaults to 1) -p, --prilengthlimit= (defaults to 60) -f, --foldlength= (defaults to 500) -o, --overlaplength= (defaults to 150) -t, --threads= (defaults to 1) --pmt, --Only calculate the parameters without further prediction

File (one of following): *.fasta, --Only fasta format sequences were allowed *.pmt, --Repredict from the parameter files

Report bugs to Yonggan Wu (weasteam@gmail.com) or Dr. Simon Rayner (raynere@wh.iov.cn)

Homepage: [http://www.whiov.ac.cn/bioinformatics/mirpara](http://www.whiov.ac.cn/bioinformatics/mirpara) Google Project: [http://code.google.com/p/mirpara/](http://code.google.com/p/mirpara/) Facebook: [https://www.facebook.com/mirpara2009](https://www.facebook.com/mirpara2009) ```

_Examples:_

1) check the version and help message: `perl miRPara.pl -v or perl miRPara.pl --version`

2) print the help message: `perl miRPara.pl -h or perl miRPara.pl --help`

3) Basic usage: `perl miRPara.pl test.fasta`

4) Advanced usage by providing species, cutoff, model level, prilengthlimit, overloplength `perl miRPara.pl -s animal -c 0.5 -l 12 -p 70 -o 100 test.fasta`

5) Advanced usage by using species group model `perl miRPara.pl -s animal test.fasta perl miRPara.pl -s Metazoa test.fasta`

6) Advanced usage by using specific species model `perl miRPara.pl -s hsa test.fasta`

7) Advanced usage by providing a model file Instead of providing species short names, a trained model can be provided directly from "-s" tag. The level tag "-l" will be ignored: `perl miRPara.pl -s /home/testuser/mirpara/models/hsa_12.model test.fasta`

8) Advanced usage by using a custom trained models `perl miRPara.pl -s customModelName test.fasta perl miRPara.pl -s /home/testuser/mirpara/models/hocustomModelName_10.model test.fasta`

9) Run with multiple cores `perl miRPara.pl -t 12 test.fasta`

10) Only calculate the X.pmt files. skip the prediction process `perl miRPara.pl --pmt test.fasta`

11) Repredict the result by change the cutoff or model level. `perl miRPara.pl -c 1 -l 20 test.pmt`
```
**miRPara version 5.2 and 5.2 above**

```
Usage: miRPara.pl [Options ] file [File ]

Options: -v, --version -h, --help -n, --name= -s, --species=species group name (defaults as overall) or species short name or path of a model file: /home/xxx/miRPara/model/hsa_10.model -c, --cutoff= (defaults to 0.8) -l, --Levels=<1..20>(defaults to 1) -p, --prilengthlimit= (defaults to 60) -f, --foldlength= (defaults to 500) -o, --overlaplength= (defaults to 150) -t, --cores= (defaults to 1) --pmt, --Only calculate the parameters without further prediction

File (one of following): X.fasta, --Only fasta format sequences were allowed X.pmt, --Repredict from the parameter files

Homepage: [http://www.whiov.ac.cn/bioinformatics/mirpara](http://www.whiov.ac.cn/bioinformatics/mirpara) Google Project: [http://code.google.com/p/mirpara/](http://code.google.com/p/mirpara/) Facebook: [https://www.facebook.com/mirpara2009](https://www.facebook.com/mirpara2009) ```

_Examples:_

1) check the version and help message: `perl miRPara.pl -v or perl miRPara.pl --version`

2) print the help message: `perl miRPara.pl -h or perl miRPara.pl --help`

3) Basic usage: `perl miRPara.pl test.fasta`

4) Advanced usage by providing the name, species, cutoff, model level, prilengthlimit, overloplength `perl miRPara.pl -n test -s animal -c 0.5 -l 12 -p 70 -o 100 test.fasta`

5) Advanced usage by using species group model `perl miRPara.pl -s animal test.fasta`

6) Advanced usage by using specific species model `perl miRPara.pl -s hsa test.fasta`

7) Advanced usage by providing a model file directly Note: If you have the miRPara model in a directory different to miRPara.pl program, you can redirect the models folder to miRPara.pl by giving trained models at any level. -l option will be ignored if full path of a model provided `perl miRPara.pl -s /home/testuser/mirpara/models/hsa_12.model test.fasta`

8) Advanced usage by using a custom trained models `perl miRPara.pl -s customModelName test.fasta perl miRPara.pl -s /home/testuser/mirpara/models/hocustomModelName_10.model test.fasta`

9) Run with multiple cores Note: need BIG RAM (>16G, depend on the input data size), if your computer do not have big RAM, you can split the input fasta files into small files and run each of them in one core. This function is still in beta and can be buggy. `perl miRPara.pl -t 12 test.fasta`

10) Only calculate the X.pmt files. skip the prediction process  

    perl miRPara.pl --pmt test.fasta

11) Repredict the result by change the cutoff or model level.  

    perl miRPara.pl -c 1 -l 20 test.pmt
```
**miRPara version 5.2 or below**
```
    Usage: miRPara.pl [Options ] file [File ]

    Options:
    -v, --version
    -h, --help
    -n, --name=<abbreviated name of the species>
    -s, --species=<overall, animal, plant or virus> (defaults as overall)
    -c, --cutoff=<the cutoff to svm prediction probabilities> (defaults to 0.8)
    -l, --Levels=<1..20>(defaults to 1)
    -p, --prilengthlimit=<limit to the pri-miRNA length> (defaults to 60)
    -f, --foldlength=<The length to be split for folding> (defaults to 500)
    -o, --overlaplength=<The overlap length of two nearby splited fragments> (defaults to 150)
    -t, --cores=<No. of cores> (defaults to 1)
    --pmt, --Only calculate the parameters without further prediction

    File (one of following):
    X.fasta, --Only fasta format sequences were allowed
    X.pmt, --Repredict from the parameter files

_Examples:_

1) check the version and help message:  

    perl miRPara.pl -v or perl miRPara.pl --version

2) print the help message:  

    perl miRPara.pl -h or perl miRPara.pl --help

3) Basic usage:  

    perl miRPara.pl test.fasta

4) Advanced usage by providing the name, species, cutoff, model level, prilengthlimit, overloplength  

    perl miRPara.pl -n test -s animal -c 0.5 -l 12 -p 70 -o 100 test.fasta

5) Run with multiple cores  
Note: need BIG RAM (>16G, depend on the input data size), if your computer do not have big RAM, you can split the input fasta files into small files and run each of them in one core.  

    perl miRPara.pl -t 12 test.fasta

6) Only calculate the X.pmt files. skip the prediction process  

    perl miRPara.pl --pmt test.fasta

7) Repredict the result by change the cutoff or model level.  

    perl miRPara.pl -c 1 -l 20 test.pmt
```
* * *

# Result

* * *

The predicted result named as "＊.out". It is a tab-delimited text file with following columns:  

|Column Name | Example 1 | Example 2 | Description |
|------------|-----------|-----------|-------------|
| priid | lin:1-94 | lin:1-94 | |
| priseq | augcuuccggcCUGUUCCCUGAGACCUCAAGUgugaguguacuauugaugcuucacaccugggcucuccggguaccaggacgguuugagcagau | augcuuccggccuguUCCCUGAGACCUCAAGUGUGaguguacuauugaugcuucacaccugggcucuccggguaccaggacgguuugagcagau | Upper case indicated the mature miRNA sequences |
| miid | lin:1-94:12_21 | lin:1-94:16_20 | underline 
| miseq | CUGUUCCCUGAGACCUCAAGUU | CCCUGAGACCUCAAGUGUG |
| miRNA sequence strand | 5P | 5P | location of the miRNA |
| SVM_probability | 0.823885 | 0.984632 | SVM Probability, the higher the better miRBase NA lin-4-5p Hit in miRBase |

* * *

# Release

* * *

**2013-03-13 miRPara 6.3**

*   fixed a bug in reading the fasta files in ./ folder  

*   fixed a bug in outputing wrong format of pmt file when using multicore  

*   added a feature to display how much time left to finish

2013-03-13 miRPara 6.2  

*   fix a bug in using the tag "-s animal", thanks to Anurag Chaturvedi for reporting the bug.

2012-11-24 miRPara 6.1  

*   optimize the multicore running, force to wait for unfinished cores.

2012-11-23 miRPara 6.0  

*   replace Algorithm::SVM with libsvm  

*   remove "-n" tag  

*   multi-core support  

*   optimize the known miRNA data hash  

*   the specific species support

2012-10-24 miRPara 5.3  

*   fix the bug to extract model level from a full path model file

2012-10-24 miRPara 5.2  

*   add support for custom models

2012-10-02 miRPara 5.1  

*   add facebook and google code page links

2012-09-10 miRPara 5.0  

*   multicore support (beta2)

2012-08-09 miRPara 4.2  

*   fix bug of uninitialized value $loop in lc at miRPara.pl line 813.
*   optimize the UNAFold.pl & ct2out check  

*   multicore support (beta1)

2011-06-02 miRPara 4.1  

*   Correct share path problem

2010-11-15 miRPara 4.0  

*   return probability  

*   Optimize the codes  

*   Change the output format

2010-04-06 miRPara 3.0  

*   Changed the predicted models, replace species (animal, plant, virus) with miRNA families  

*   new algorithm to calculate parameters  

*   three different models (numerical, arphabetic and bulge)

2009-11-28 miRPara 2.0  

*   Retrain all the models  

*   Different models been added, the miRNA could been predicted with specific models  

*   Changed the SVM parameters for different models  

*   Optimize the scripts

2009-9-16 miRPara 1.7  

*   Update the sub script of callunafold

2009-9-2 miRPara 1.6  

*   Retrained all the data with UNAFold.pl predicted structures.  

*   Change the output alignment form, more easy to read the output results  

*   Increse the level of models to 20  

*   Added the enviroment, more easy to install

2009-5-12 miRPara 1.5  

*   Replaced the Bio::Seq and Bio::SeqIO module, again increased the speed  

*   Change the input data read policy, allow multiple input sequences

2009-4-18 miRPara 1.4  

*   Retrain the models files, exclude the bad format files  

*   Reorganize all miRNA parameters  

*   Optimize output format

2009-4-17 miRPara 1.3  

*   Replace the XML module, increase the analysis speed.  

*   Update the file output format of XXX.pmt

2009-3-9 miRPara 1.1  

*   Update the algorithm to extract UNAFold.pl exported data  

*   Correct the candidates extraction algorithms

2009-2-19 miRPara 1.0 Beta  

*   All the script were rewrite with perl, and could be run under Linux

2008-9 miRPara 0.5  

*   miRPara Windows application software, write in Visual Basic

2007-12 miRPara 0.1  

*   Based on Microsoft Excel, the first miRPara version released  
    *   It calculate the parameters and filter based on artificial cutoffs  
    *   Write in VBA

