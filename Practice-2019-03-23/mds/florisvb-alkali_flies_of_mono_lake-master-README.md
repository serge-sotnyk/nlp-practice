# Alkali Flies of Mono Lake
This repository contains the software associated with the paper "Super-hydrophobic diving flies (Ephydra hians) and the hypersaline waters of Mono Lake". Some of the data is included in this repository as well (e.g. GCMS results and SEM images). For force trace data see our [OSF data repository](https://osf.io/43yhs/ "OSF data repository").

This readme assumes working knowledge of Ubuntu and python. This code is not actively maintained. It worked on 2017-10-4 using up-to-date versions of the required software below.

Code and data are licensed under a [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/ "CC BY-NC-SA 4.0"). See subfolders for full text license.

## What you need to run our analysis
* Ubuntu (we used Ubuntu 12-16)
* Python (2.7)
* ROS (Robot Operating System, Kinetic): http://wiki.ros.org/kinetic/Installation/Ubuntu
* apt-get repositories: git python-pip python-scipy python-h5py python-progressbar python-sympy python-networkx
* Manual downloads: 
  * https://github.com/taynaud/python-louvain/
  * http://www.pyqtgraph.org/
* pip installs: pandas (0.19), statsmodels, word_cloud (https://github.com/amueller/word_cloud)
* My packages:
  * FigureFirst: https://github.com/FlyRanch/figurefirst
  * FlyPlotLib: https://github.com/florisvb/FlyPlotLib
  * DataFit: https://github.com/florisvb/DataFit
  * FlyStat: https://github.com/florisvb/FlyStat
* Inkscape

You may wish to do all of this in a virtual environment.

## Downloading the data

Data for force traces is available from our [OSF data repository](https://osf.io/43yhs/ "OSF data repository"). The OSF repo contains a collection of tar.gz compressed folders. Inside each folder are .bag, .hdf5, and .pickle files. Raw data is saved as .bag files, which contain raw force measurements, lvdt, and movie images, all time-synced. See http://wiki.ros.org/ROS/Tutorials/Recording%20and%20playing%20back%20data. The quantitative information from the bag is converted to the hdf5 format. The pickle files are used by the analysis to parse the data (see processing raw data below). 

In order to properly run our code, you will need to download and un-tar all of the data files, and then you will need to follow the instructions for making the data accessible (below).

## Making the data automatically accessible to the analysis
We ran our analysis on several different computers, so to keep track of everything, we created a python package that points to the data and figure template locations. In order to run our analysis, you will need to add your machine and local paths to this repository. 

In `mono_paper_locations/mono_paper_locations`, create a duplicate of `data_locations_analysiscavetech_organized.py`, e.g. `data_locations_yourname.py`. Edit the file so that the paths correspond to the data locations on your machine. Next, you will need to create an environmental variable called `mono_paper_locations` (e.g. type `export mono_paper_locations mono_paper_yourname` in any terminal window in which you plan to run our code, or add that to your .bashrc). Add an `elif` statement to the `__init__.py` file in `mono_paper_locations` that matches, for example, `mono_paper_yourname` to  `data_locations_yourname.py` as in the other if and elif statements.

In `mono_paper_locations/mono_paper_locations`, edit the file `figure_template_locations.py`, so that the paths match your system.

Install the package (from `mono_paper_locations` type `python setup.py install`). 

## Installing our analysis

In addition to mono_paper_locations, you need to install the following python packages inside analysis:
* mono_analysis
* gcms_analysis

## Processing raw data
Raw data is saved as .bag files, which contain raw force measurements, lvdt, and movie images, all time-synced. See http://wiki.ros.org/ROS/Tutorials/Recording%20and%20playing%20back%20data

Our first step was to manually segment the data into the portions where the fly is entering the water, stable and submerged, or exiting the water. We did this using a pyqtgraph gui. You can view our segments for data (and change them!) as follows:

* Directory: raw_analysis
* Command: `python align_force_data.py --file=FILENAME.bag`

To change the selection, drag the vertical lines, and click save. These time segments are saved (along with mean and std values) in a pickle file associated with each filename.

Calibration data was preprocessed in a similar way; we selected stable segments of before, during, and after calibration weight placement and used the mean values of these segments to determine the calibration for each fly, which is also saved as a separate pickle file. 

* Directory: raw_analysis
* Command: `python extract_calibration_data.py --file=FILENAME.bag`

## Running the analysis

In each "figure" folder (except figure1) there is a make_figureX.py file. Run this file (`python ./make_figureX.py`) to rerun the analysis and update the associated svg figure files in that directory. You can use this to trace backwards our analysis, most of which can be found in mono_analysis/plot_raw_traces.py

## Species and colloquial names

In our analysis and data we refer to the species by the following alternative names:

* Fucelia rufitibia: blue kelp fly
* Coelopa vanduzeei: black kelp fly
* Ephydra hians: alkali fly / mono lake fly
* Ephydra sp: santa ana fly
* Helaeomyia petrolei: oil fly / petroleum fly
* Drosophila melanogaster: melanogaster
* Drosophila virilis: virilis

## Hairyness calculations

For our hairnyess calculations (e.g. used in Fig. 4), see `SEM_images/20161118/Hairyness.ipynb`

