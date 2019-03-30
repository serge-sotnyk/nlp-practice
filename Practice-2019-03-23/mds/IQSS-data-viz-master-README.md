# Dataverse Visualizations

This is a tool for visualizing data from the Dataverse project. It is intended to augment TwoRavens, a data analysis tool for Dataverse, to give it visualization capability. 

##Setup 
1. Download from Github

1. Software Prerequisites:
  * [Python](https://www.python.org/downloads/)
  * Python package index [(pip)] (https://pip.pypa.io/en/latest/installing.html)
  * [R](https://www.r-project.org/)
     + Make sure you have the libraries 'rjson' and 'DescTools' loaded into R. To download them, open R, and run the following    commands: 
    
    ``` R
        install.packages('rjson')
        install.packages('DescTools')
 ```
 

2. (Recommended)
  * Before downloading the necessary packages for this application, it is recommended to set up a python virtualenv with a virtualenvwrapper. Please see the [virtualenv documentation](https://virtualenv.pypa.io/en/latest/) and then the [virtualenvwrapper documentation.](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) Note: if you are running windows, download [virtualenvwrapper-win-1.1.5] (https://pypi.python.org/pypi/virtualenvwrapper-win) or [cygwin] (https://www.cygwin.com/) instead of virutalenvwrapper.
 
3. Package Download
 * In your terminal, change directories to the path of the application (data-viz). Then enter the 'DataVisualiations' directory. if you decided to set up an virtualenvwrapper, activate it with the command: ```$ workon your_environment_name```. Then, change directories to the project directory ```data-viz```, then enter the ```DataVisualizations``` folder. To download the contents of the "requirements.txt" file, type the following command into the terminal: ```$ pip install -r /path/to/requirements.txt```
 
4. Starting the App
 * To begin visualizing, make sure you are in the ```DataVisualizations``` directory and run the following command: ```python viz_tool.py```. You will see the following line: ``` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)```. Go to the listed URL in a browser (preferably Chrome), and you will be ready to visualise. 
 
## User Guide
* To see how to use this tool to visualize your data, please see [this 4 minute demonstration](https://youtu.be/OzrECzPf95g).
 

