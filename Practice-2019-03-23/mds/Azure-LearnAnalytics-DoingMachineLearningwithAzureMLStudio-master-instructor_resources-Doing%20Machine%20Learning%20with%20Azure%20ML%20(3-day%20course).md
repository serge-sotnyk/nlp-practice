<link rel="stylesheet" href="./styles.css">

<!-- $theme: default -->
<!-- $size: 16:9 -->
<!-- page_number: true -->

<!--

Notes: This will replace the current "Azure Machine Learning - Deep Dive" course in the catalog. It was redesigned to make it more modular, add more background and concepts, and make the labs more integrated and interconnected.

This should be a three-day course.

There are some topics I would like to cover but don't, such as the bias-variance trade-off and cross-validation.

-->

<!-- 

Some examples of things:

- putting and image of the left and text on the right side:
<div style="float:left"><img src="./images/imagename.jpg" height="650" border="50"></div>
<div style="margin-left:45%"><p style="font-size:150%">Text on the right.</p>
</div>

- centering an image in the slide:
<div style="text-align:center"><img src ="./images/imagename.jpg" width="500"/></div>

- putting two images side-by-side:
<img src ="./images/imagename1.jpg" width="500"/>
<img src ="./images/imagename2.jpg" width="500"/>


- image that can be downloaded:
Click on the image to download.
<div style="text-align:center"><a href="URL"><img src ="./images/imagename.jpg" width="800"/></a></div>

- link to image in another slide so clicking on image would take you back to the top
<a name="backtotop"> </a>
link [click here to go to image](#imageid)
… many slides later …
<a href="#backtotop" name="imageid">
<div style="text-align:center"><img src ="./images/imagename.jpg" width="700"/></div>
</a>

Use the following regex to capture comments: <!-[^*]+?->

-->

<div style="text-align:center"><img src ="./images/elephant.jpg" width="700"/></div>

<!-- If I show you this picture it would probably take you next to no time to identify it as an elephant. Now imagine you showed this picture to someone who'd never seen an elephant before but had read descriptions of elephants (or to be more precise, a set of instructions for how to recognize an elephant). Even if the instructions were really thorough, and I wouldn't want to be the one tasked with writing them, they will probably find it harder to identify an elephant than someone who'd seen elephants before. 

https://www.thinglink.com/scene/865640765441703937# -->

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/elephant-sketch.jpg" width="700"/></div>

<!-- They might find it even harder to identify an abstract picture of an elephant like this beautiful one I just drew. Especially since I took some artistic liberty of giving it earings and roller skates. Computers are the same way. We can try to write a computer program that "describes" what an elephant looks like to a computer, but writing such a program is not a trivial task, and even then it might fail to work well especially when presented with more abstract representations of elephants. At some point we might throw our hands in the air and say but if I only "show" you enough pictures of elephants you'll eventually recognize this as an elephant. Well, basically that's what machine learning is all about. -->

--------------------------------------------------------------------------------

# Doing Machine Learning with Azure ML
## Seth Mottaghinejad
### Data Scientist
sethmott@microsoft.com
www.linkedin.com/in/sethmott/
<div style="text-align:right"><img src ="./images/microsoft-logo-white-small.jpg" width="200"/></div>

<!-- Hello, welcome to Doing Machine Learning with Azure ML. I'm Seth Mottaghinejad. I'm a data scientist at Microsoft and have the pleasure to be teaching this course.

Machine learning is at its core a set of algorithms that computers can use to "learn" from data. These algorithms look at data (and believe it or not almost anything including pictures can be expressed as data) and come up with "rules" that "describe" the relationships in the data, so that we (the lazy people that we are) don't have to figure out what the relationships are. This saves me the trouble of writing explicit instructions for deciding for example if something is an elephant or not. Instead, we let the data speak for itself. Depending on how complex the data is, some algorithms may work better than others, so machine learning is not just plug-and-play and there's quite a bit of trial-and-error involved, which we'll cover in more detail thoroughout the course.

Let's also talk about what the course is NOT about. This is not a specialized course on particular machine learning problems (such as image recognition, natural language processing, or anomaly detection), or on particular algorithms such as support vector machines. Instead, we try to keep the discussion around machine learning in general and data science as a practice. With that said, we provide some examples of particular ML algorithms mostly to help you build a strong intuition.

The last thing I'll say before we start is that this course is very lab-heavy, and we'll be using the Azure ML Studio for the exercises. You can get a guest account and get set up very easily. I strongly recommend that you take the time to do the labs, because they are an essential part of the course and sometimes new concepts are not introduced until we get to the labs.

So thanks for joining in and let's get started. -->

--------------------------------------------------------------------------------

<div style="float:left"><img src="./images/satya.jpg" height="650" border="50"></div>
<div style="margin-left:45%"><p style="font-size:150%">I believe over the next decade computing will become even more ubiquitous and intelligence will become ambient… This will be made possible by an ever-growing network of connected devices, incredible <mark>computing capacity from the cloud, insights from big data, and intelligence from machine learning.</mark></p>
</div>

<!-- We're going to begin with a quote from Satya Nadella which for me sums up what data science nowadays is concerned with. He says "I believe over the next decade computing will become even more ubiquitous and intelligence will become ambient. This will be made possible by an ever-growing network of connected devices, incredible computing capacity from the cloud, insights from big data, and intelligence from machine learning." You can see in the highlighted section a sort of bird's-eye view of data science: that is to say the prevalence data, combined with the ability to collect and store that data on the cloud and churn through and process it using the computing-capacity of the cloud. Throw machine learning into the mix and now we can extract fast insights (non-obvious or hidden trends) from the data and build intelligent applications. -->

--------------------------------------------------------------------------------

# Chapter 1
## Basic overview

<!-- Chapter 1 is a high-level overview of the data. It's really important for us to set the stage before we get down and dirty because data science is very much an iterative process, as we'll later in more detail, and so we need to know where we are at each stage and understand the feedback loops that feed in and out of each stage. -->

--------------------------------------------------------------------------------

### Here is what we are going to cover:

- statistics and data visualization
- machine learning concepts and examples
- Azure ML Studio
- data science process and workflow

There will be vocabulary and concepts, with **quizzes** for review and lots **hands-on labs** in the AzureML Studio.

<!-- So this is what we're going to spend our time on. We get our feet wet by going over some statistics and visualization, enough to know how to use the stuff to understand our data. We then jump right into machine learning, starting with what ML is and going over some examples, and then looking at some concepts and best practices that apply to most machine learning problems. All the while, we're going to do a lot of exercises that will really drive some of the concepts home. We finish the course by talking about data science as a process and putting machine learning in perpective. As we'll see, machine learning models are not the end-all-be-all, so instead we should think of them as part of a larger system which also includes data collection or model consumption. -->

--------------------------------------------------------------------------------

# Three essential skills of data scientists

<div style="text-align:center"><img src ="./images/three-skills.jpg" width="500"/></div>

Drew Conway
www.dataists.com/2010/09/the-data-science-venn-diagram/

<!-- Nowadays, people who are practitioners of machine learning are often called data scientist. It probably doesn't go the other way around, because not every data scientist is doing machine learning, but every machine learning practitioner can safely be called a data scientist. So what then is a data scientist? I think this Venn diagram by Drew Conway does a nice job of summing it up. Data science is the convergence of three particular skill sets: foundational knowledge in math and stats, some domain knowledge in your area of expertise and especially around what sorts of interesting questions we can ask and what sorts of data we can get our hands on, and finally, the ability to put these skills to use using programming, which nowadays is mostly R and Python, although it wouldn't hurt to be familiar with some strongly-typed language like C++. In addition to programming, it's also becoming increasingly important for data scientists to know about the production environment that ultimately deploys and serves some of the models they build. This means being better programmers, and also knowing about things like provisioning resources on the cloud, connectivity with other applications, and resource utilization and management. -->

--------------------------------------------------------------------------------

# What do data scientists do?

<!-- So the last slide gave a broad description of what sorts of skill sets make for a good data scientists, but now let's rephrase the question a little and get more specific: we want to know what data scientists do, or at least should do, on a day-to-day basis. Now this is a question that very much depends on the company or the team they work at, but we venture an answer which should more or less describe a data-scientist's workflow. -->

--------------------------------------------------------------------------------

### business understanding
- **ask**: identify key business variables
- **measure**: define success metrics

### data acquisition and understanding
- **data ingestion**: ingest the data into analytic environment
- **data exploration**: explore the data to check quality and adequacy

<!-- Even though data scientists are sometimes tempted to get their hands on data the first chance they get, data science actually begins with understanding the business we're in, that is to say what are some questions we want answered, are they the right questions to ask, and how can we use data to get a more-or-less satisfying answer? To answer the last question, we need to go and review the data we have, sometimes find ways to obtain more data or better data, and last-but-not-least, make sure that we have a correct understanding of the data. In most cases, data is maintained by DBAs or similar people who don't necessarily know or care much about how it's being used. They care more about data integrity, data governance, security, and other admin-like issues surrounding the data. It's up to us, data scientists, to make sure that we have a solid understanding of the fields in our data, and failure to do so can come back to kick us in later stages of the process. -->
 
--------------------------------------------------------------------------------

### modeling
- **pre-processing**: set up <mark>data pipeline</mark> to prepare data
- **feature engineering**: create <mark>features from raw data</mark>
- **model evaluation**: how well does <mark>the model fit?</mark>
- **model selection**: explore and find the "right" model

<!-- Once we have some questions in mind, and good data to match, it's time to have some fun. Not every machine learning problem involves modeling (which is what I refer to as a prediction problem). Sometimes you explore your data and find some interesting patters and take that to business and get feedback and so on. But most machine learning problem go one step further and attempt to make predictions. This is not necessarily predictions about the future (or what we refer to as forecasting), but prediction of the unknown. To that end, data scientists build models, and sometimes models force us to do some heavy-lifting with the data, which we call feature engineering. Once we have a model, we need to go how good it is, at predicting that is, and we refer to this as model evaluation. Even when we have a good model, it's probably not the only game in town. Now some industries have "standards" for which models they prefer and preferences for how to run feature engineering and such, but even then exploring some other candidate models can tell us a thing or two about the pros and cons of each. This can be helpful when we move on to model deployment. Before we move on, Let me reassure you that we do a better job of clarifying all of these terms in later sections, so don't worry if it's all sort of vague right now. -->

--------------------------------------------------------------------------------

### deployment
- **operationalization**: deploy model to production
- **model consumption**: use model to <mark>make predictions (scoring)</mark>
- **business validation**: are business requirements met?

<!-- This is home-run for data scientists: we have a model and it makes good predictions, but we need to find a way to surface those predictions so that interested parties can get to them, and do so on time. This is called operationalization if you can pronounce it, or deployment if like me you find the word operationalization to be a mouth-full. The end-user we have in mind here can be anyone from statisticians, management, or customers. They are the ones "consuming" our models. At this stage we can start collecting feedback to see if the model was able to accomplish what it set out to do. -->

--------------------------------------------------------------------------------

last but not least
## iterate, iterate, iterate...

<!-- We finished the last slide by asking "are business requirements met?", and if we're lucky the answer is yes, so you shake hands and hike the pacific crest trail for the next 6 months. But probably the answer is something like, "not really, the predictions are way off", "not really, that's not the questions we started with", "maybe, but we can't tell", "yes, but can we do better?", and all sorts of variations thereof. So we go back to the drawing board (and sometimes this means going right back to the data), and ask what can be done better, or differently. -->

--------------------------------------------------------------------------------

# What do data scientists do?

<div style="text-align:center"><img src ="./images/data-science-workflow.jpg" width="700"/></div>

<!-- So a picture is said to be worth a thousand words, which is what people tell you in order to spare you the long speech. In my case, I've already given you the long speech, but we can now look at the picture too so we can review what we just covered. We can see here how, starting with the business goal at the top, and moving clockwise, we get to collect and explore the data, build models and evaluate them (both statistically, and practically), and deploy them at last. But as you can see from the smaller arrows, every stage feeds forward into the next but also back into the prior stage. For example, we could have a perfectly good model in terms of predictive accuracy and move to the "Deploy model" stage only to find out that the model is slow in production or doesn't scale well with the amount of data coming its way. So we go back to the modeling phase and explore other models, which in turn can take us back to the data-processing or feature engineering phase because different models can have different requirements for how data needs to be "massaged" prior to modeling. -->

--------------------------------------------------------------------------------

# Azure Machine Learning

Our goal is to make machine learning **accessible** to every enterprise, data scientist, developer, information worker, consumer, and device anywhere in the world.

<div style="text-align:right"><img src ="./images/azureml-logo.jpg" width="200"/></div>

<!-- So we're about to jump right in, and we're going to use Azure Machine Learning Studio for the labs in this course. We refer to it as the ML Studio for short. The ML Studio is mostly a drag-and-drop interface, although you can also write your own R or Python modules. It's a good way to learn machine learning because we won't have to be bogged down by the quirks of the programming language. Since a lot of you are new to this, we don't assume that you are advanced R or Python programmers right off the bat, and if so, then a machine learning course is not the recommended place to start. Of course, eventually you want to pick up R or Python (or both) and learn to use them to solve machine learning problems, but we don't want that to get in the way of learning concepts. -->

--------------------------------------------------------------------------------

An Azure ML **experiment** is a blank canvas connecting **datasets to modules**, each module performing some action on the data.

You build a model in a <mark>training experiment</mark> and convert it to a <mark>predictive experiment</mark> to publish it as a web service so that your model can be consumed. An ML **project** is a collections of experiments, datasets, notebooks, and other resources.

<!-- In Azure ML Studio, we have what's called an experiment, which you can think of as an ML project. There are two kids of experiments: a training experiment and a predictive experiment. We are going to start with a training experiment, and what a predictive experiment is will become more clear in the last chapter. The goal of a training experiment is to start with data and build and evaluate one or many ML models. Every step of the process is represented by a module, which is a little box that we drag into our experiment canvas and it does something for us. It usually has arrows shooting into it from previous modules and arrows shooting out of it that feed into subsequent modules. So zooming out we can get a bird's-eye view of the whole experiment. Finally, multiple experiments and their associated datasets can be grouped together into what's called a project. -->

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/aml-interface.jpg" width="500"/></div>

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/aml-modules.jpg" width="300"/></div>

--------------------------------------------------------------------------------

# LAB 1
## Our first experiment

Expected lab duration: 15 minutes.

<!-- It's really easy to get familiar with the ML Studio environment and the goal of this lab is to force you to get your hands dirty. We're going to do a bunch of things, not knowing what exactly is going on, just so we can get more familiar with the mechanics of setting up and running and ML Studio experiment. We later go back and cover in detail the bits and pieces. -->

--------------------------------------------------------------------------------

# About the labs

To make it easier to understand the instructions
- Names of <button>modules</button> are in a grey box.
- `Column` names and code have a grey background and monospace font.
- <mark>A screenshot of the finished experiment is sometimes provided as a visual guide to see the final arrangement</mark>. You can click on the screenshot to go back to reading instructions.
- Instructions are not too detailed because the interface can sometimes change and because users can become more familiar with the interface by looking around.

<!-- Just a note about the labs in this course before we start with the first lab: we've formatted slides to make it easier to read and understand the instructions. So the module names are enclosed in a grey box to make it clear what we're talking about. Anything that is either code or a reference to column names in the data have a grey background and a monospace font so it's easier to recognize it. And because the experiments we're going to build are going to be increasingly complicated, we're providing screenshots of the final experiment so you can at least see what the final layout is once you drag in and connect all the modules. I highly recommended that you only look at this after you've given it a shot. Try not to cut too many corners in this class, because there're a lot you can learn by just tinkering with the environment. You should be able to recreate these experiments by just following the instructions, but the instructions are intentionally a little vague just to give you a chance to explore and figure things out on your own. This might seem a little frustrating right now but I promise it will pay off by the end of the course. -->

--------------------------------------------------------------------------------

<a name="backtolab1"> </a>

In this lab, we create and run the experiment shown in [this screenshot](#screenshotlab1).

1. Create a new experiment called **Automobile price prediction**.
2. Drag in <button>Automobile price data (Raw)</button> and visualize it.
3. Drag <button>Select Columns in Dataset</button> and remove `normalized-losses`.
4. Double-click on the module and entere text saying "column was removed due to too many NAs".
5. Drag <button>Clean Missing Data</button> and remove entire row if any column is missing.

--------------------------------------------------------------------------------

6. Drag <button>Select Columns in Dataset</button> and paste in the following columns: `make, body-style, wheel-base, engine-size, horsepower, peak-rpm, highway-mpg, price`
7. Run the <button>Split Data</button> to split the data 75% to 25%.
8. Connect <button>Split Data</button> to a <button>Train Model</button> and connect that to a <button>Linear Regression</button> module in turn.
9. Connect the second split to a <button>Score Model</button> module.
10. Drag <button>Evaluate Model</button> to evaluate the model.

--------------------------------------------------------------------------------

<a href="#backtolab1" name="screenshotlab1">
<div style="text-align:center"><img src ="./images/aml-lab1.jpg" width="500"/></div>
</a>

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

# Resources
- A listing of all the modules: https://msdn.microsoft.com/library/azure/dn906033.aspx
- Go to Cortana Intelligence Gallery and examine some pre-existing experiments: http://gallery.cortanaintelligence.com/
- Learn [this basic infographic](http://download.microsoft.com/download/0/5/A/05AE6B94-E688-403E-90A5-6035DBE9EEC5/machine-learning-basics-infographic-with-algorithm-examples.pdf)
- Azure Machine Learning Documentation Center: https://azure.microsoft.com/services/machine-learning/

<!-- So I hope you enjoyed working on the first lab. If you didn't, then don't worry, because as I said the first lab was really just meant to get you to learn the mechanics of building experiments. If you're new to swimming, then I just snuck up on you and pushed you into the pool. Well, hopefully it wasn't too bad. See you in the next chapter. -->

--------------------------------------------------------------------------------

# End of chapter

--------------------------------------------------------------------------------

# Chapter 2
## Just enough statistics

<!-- Welcome back. In this chapter, we want to learn some statistical tools that can help us explore our data. We said in the last chapter that a data scientist should start with a business problem and not jump immediately to the data, and that's true if we have some well-formulated business problems, but very often we don't. In fact, we as data scientists, might sometimes be tasked with finding out the kinds of questions that the data can take a stab at. So knowing what data we have and don't have, its quality, granularity or other limitations can help us set the right expectations. Knowing our data well is also very important to any future modeling task as we'll see. This open-ended process of data exploration is called exploratory data analysis, and statistics and data visualizations are our greatest tool in the toolkit. -->

--------------------------------------------------------------------------------

# What we will learn

- variables: dependent, response, independent, explanatory, numeric, categorical, nominal, ordinal
- features and target
- exploratory data analysis
- mean, median, standard deviation, range, percentiles or quantiles, univariate vs bivariate summaries and visualizations, histograms and density plots

<!-- By the end of these chapters, here are some terms you should be able to define and use. You may have heard of some of these terms before or learned in an introductory statistics course, and others might be brand new to you, but we're going to cover these extensively in this lecture. -->

--------------------------------------------------------------------------------

# Exploratory data analysis (EDA)

We have a new dataset, so we *slice and dice* the data to get a feel for it, for example we
 - use <mark>statistical summaries</mark> to see if the data makes sense or if <mark>outliers</mark> are present
 - examine <mark>missing values</mark>
 - visualize the data looking for any patterns
 - bivariate statistics and plots can hint at relationships between variables

<!-- Exploratory data analysis, or EDA for short, is basically all about "slicing and dicing" the data, looking for patterns, anomalitis such as outliers and missing data, and relationships between the columns in the data. Initially we're really looking for the obvious things, which we can get at using some basic statistics and visualizations. The goal is to quickly come to grasp with what's in the data. EDA is something that we get better and better at over time as data scientists, because it does require us to be a little forward-thinking with the analysis and know where we're going. But we cover the basics here. -->

--------------------------------------------------------------------------------

Visualize the **automobile price prediction** data from the lab

<div style="text-align:center"><img src ="./images/data-visualize.jpg" width="700"/></div>

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/data-snapshot.jpg" width="700"/></div>

--------------------------------------------------------------------------------

**Tabular data** is made up of rows and columns. Statisticians sometimes call them <mark>observations and variables</mark>.

Some variables are <mark>numeric</mark>. Numeric variables may be **discreet** or **continuous**.

Some variables are <mark>categorical</mark>. Categorical variables may be **nominal** when there is no order or **ordinal** when there is an order. Categorical data with only two categories is sometimes called **binary**.

<mark>A numeric variable can sometimes be treated (by us and our models) as if it's categorical.</mark>

<!-- Since we're going explore data, let's begin by what we mean by data. You hear data is everywhere these days and certainly the amount of data that is being collected these days has gone by through the roof, but so has the variety of data. For example, data is increasingly being stored in so-called no-SQL databases in addition to conventional relational databases. However, when it comes to doing machine learning, the great majority of ML algorithms only work with tabular data, that is data with rows and columns. Statisticians tend to use the word observations when talking about rows, and variables when talking about columns. Variables are broadly divided into numeric variables and categorical variables. Numeric variables can be discreet, which means they can be counted (think of an integer variable) or they can be continuous which is any variable with decimals. Categorical variables are called nominal when the categories are just names (like male vs female), and called ordinal when the categories have an inherent ordering to them (like low-income, middle-income and high-income). Lastly, a numeric variable can sometimes be treated as a categorical variable. And we see an example of that in the labs. -->

--------------------------------------------------------------------------------

Can you describe this dataset?

<div style="text-align:center"><img src ="./images/data-snapshot.jpg" width="700"/></div>

--------------------------------------------------------------------------------

You can describe each variable using **summary statistics** and **visualizations**.

--------------------------------------------------------------------------------

| statistic          | describes                                | useful because…                                          |
| ------------------ | ---------------------------------------- | ---------------------------------------------------------|
| mean               | average                                  | single-number representation of a column                 |
| median             | number in the middle                     | like mean, but <u>robust to outliers</u>                 |
| min                | lowest value                             | check for data quality issues                            |
| max                | highest value                            | check for data quality issues                            |
| standard deviation | average deviation from the mean          | measure of <u>spread or variability </u>                 |
| unique values      | number of distinct numbers or categories | find number of categories or distcreet numeric variables |
| missing values     | how much of the variable is missing      | check for data quality issues                            |

<!-- Let's take a look at some of the most important statistical summaries we should consider. I avoid using any math here because I don't want to distract you away from the interpretation by showing you ugly-looking formulas, but I encourage you to later find out how these numbers are computed and their derivation is frankly not that complex. We begin the mean and the median which can both be thought of as a single number representation of a bunch of numbers, in other words, an "average" for a bunch of numbers. The difference between the two is that outliers drag the mean toward them, but the median won't budge, this is because every numbers goes into the calculation of the mean. I'm using the word outlier here kind of loosly. What I mean by outlier here is really just extreme observations, high or low. So based on what I just said, if the mean of a variable is much higher than its median, that's an indication that there might be one or many really high observations. To confirm that, we can go look at the max. The standard deviation of a variable is the average spread of the variable, in other words it is an average of how much the data points deviate from the average. I hope that's not a mouth-full. A good way to think about it is that if we claim that the mean is the single number that best represents the data, then the standard deviation is a measure of how wrong we are in making this claim. Means, medians and standard deviations are useful for numeric variables with a high number of unique values (a fancy way to say that is a variable with high-cardinality), but they can be a little misleading with variables with just a few unique values. So it's always good to look at the number of unique values. Finally, the number of missing values is another thing that we should be aware of, and it's probably good to also ask why there might be missing values. For example, does it seem like the missing values are missing arbitrarily or are they more likely to be missing for some subset of the data. Missing values are a permanent thorn in the side when doing data analysis and modeling, and we talk more about them later. -->

--------------------------------------------------------------------------------

Another common statistic is the **percentile**: <mark>The $p$th percentile is the value such that $p$ *percent of the data falls below it* (or $1-p$ percent of the data is above it).</mark> We get percentiles by first sorting the data from small to large.

- the median is the 50th percentile, so 50% of the data is below the median (and 50% above it)
- the minimum is the 0th percentile and the maximum is the 100th percentile
- the 23rd precentile is the number that's bigger than 23% of the observations

<!-- The next statistic, or I should say set of statistics, we look at are percentiles. Percentiles seem to have a convoluted definition but they're actually pretty simple once you wrap your head around them, and as you'll see we've actually seen them before but called them by other names. If you pick some number p between 0 and 100, then the p-th percentile for a variable is just a cut-off point that splits the variable into p-percent on the left and 1-p-percent on the right. So for example, pick p = 23 and find the 23rd percentile of a variable, and let's just say that it comes out to be 34.1, then we can say that 23 percent of the variable's observations are less than and equal to 34.1, which means the other 77 percent are greater than 34.1. We picked p = 23 here but we could have picked any number between 0 and 100. The 0th-percentile is really just the minimum and the 100th-percentile is just the maximum, so unless you're trying to impress your date I would just call them min and max. After the min and max, the most common percentile is the median, which is the 50th percentile, or the 50% cut-off point. -->

--------------------------------------------------------------------------------

| statistic   | describes       | useful because…                                           |
| ----------- | --------------- | --------------------------------------------------------- |
| $q1$        | first quartile  | cut-off for bottom 25 percent of a variable               |
| $q3$        | third quartile  | cut-off for top 25 percent of a variable                  |
| $p1$        | 1st percentile  | numbers below may be outliers (compare it to the minimum) |
| $p5$        | 5th percentile  | cut-off for bottom 5 percent of a variable                |
| $p95$       | 95th percentile | cut-off for top 5 percent of a variable                   |
| $p99$       | 99th percentile | numbers above may be outliers (compare it to the maximum) |

<!-- After the median, the most common percentiles are the first and 99th, the fifth and 95th, and the 25th and 75th percentiles. The last two are also referred to as the first and third quartile. People just can't agree on one name for things, now can they? Anyway, let's take the first and 99th percentiles as an example: they represent the cut-off points for the bottom 1 percent and the top 1 percent of a variable, respectively. This is pretty useful because if the variable has outliers or extreme observations, which by definition represent a very small portion of data points, and let's say  then we should see a big difference between the say min and first percentile or the max and the 99th percentile, depending on whether we're talking about extremely low values, high values, or both. If we want to be more permissive in what we call an extreme observation, we can use the 5th and 95th percentiles instead. Of course, we're not suggesting that these data points are erroneous and should be thrown out, although they could be. We're only saying that we should probably take a closer look at these values, because they might exert undue influence on future models we build. I usually try to be careful when using this word because of the connotation it conveys, so you may hear me refer to extreme observations as potential outliers instead of just outliers. -->

--------------------------------------------------------------------------------

Visualizing data can reveal a lot of interesting trends. A <mark>histogram and boxplot</mark> are examples of univariate visualizations, because they involve only one variable and answer:

- is there a single peak or more than one peak?
- are the values tight or spread-out?
- is the data <mark>symmetric or heavy-tailed</mark>?
- are there any outliers (subjective)?

A **scatter plot** is an example of a bivariate visualization: it shows the relationship between two variables.

<!-- As we saw, to get a good feel for the variables in the data, we can't just rely on a single number. There are other statistics we could have looked at, but sometimes a picture is worth a thousand numbers, and so we now turn to our attention to visualizations. The most common visualizations we usually look at are histograms, box plots, and scatter plots. A histogram of a categorical data is more commonly referred to as a "bar plot", but we adopt the convention of calling it a histogram because they show the same kind of information. Histograms and box plots are examples of univariate visualizations, that is to say that they are a visual representation of a single variable, and they can be used to understand the "distribution" of the variable. The word "distribution" one of those words that statisticians can't go a day without using. In this context, the distribution of a variable refers to the way the data points are spread out. By looking at the histogram, we can see for example if the data points kind of spread out from the middle in a symmetric way, or if we have skewed data with a tail on the right or on the left. Tails can be an indication of outliers, especially if we see some heavy tails. A box plot overlaps to some extent with a histogram in the information it shows, as we'll see, it can do a better job of pointing out potential outliers. Scatter plots on the other hand are what we call a bivariate visualization, meaning that there are two variables involved and the scatter plots can help us divine any sort of relationship that exist between them. So let's now take a look at some examples. -->

--------------------------------------------------------------------------------

<img src ="./images/histogram-compensation.jpg" width="500"/>
<img src ="./images/boxplot-compensation.jpg" width="500"/>

--------------------------------------------------------------------------------

<img src ="./images/histogram-highwaympg.jpg" width="500"/>
<img src ="./images/boxplot-highwaympg.jpg" width="500"/>

--------------------------------------------------------------------------------

<img src ="./images/histogram-enginesize.jpg" width="500"/>
<img src ="./images/boxplot-enginesize.jpg" width="500"/>

--------------------------------------------------------------------------------

<img src ="./images/scatter-enginesize-highwaympg.jpg" width="500"/>
<img src ="./images/scatter-compression-highwaympg.jpg" width="500"/>

--------------------------------------------------------------------------------

| visualization | describes… | useful because… |
| - | - | - |
| histogram     | distribution of a variable | find the peaks and tails |
| density plot  | (continuous) fine-grained histogram | identify smaller peaks or tails the histogram missed |
| box plot      | simplified distribution of a numeric variable showing quantiles | identify outliers and range |
| scatter plot  | relationship between two numeric variables | look for trends (linear or non-linear) |

<mark>For numeric variables with a heavy-tailed distributions, it helps to apply a transformation like the log to resize the visualization and make trends more apparent.</mark>

<!-- Now that we've seen enough examples, we can review the kind of information that the visualizations we talked about convey. We saw that histograms are a good thing to look at if we want to find peaks and tails. There is a sort of fine-grained version of a histogram that we call a density plot. We can look at that too, especially if the histogram looks a little iffy, but usually histograms do a good job of showing what's there. We saw that box plots can be used to find potential outliers, the range of the data, and the range of the middle 50 percent of the data, which is spanned by the box itself. Finally, we saw that scatter plots show if there's a relationship between two variables. Of course it's rare to see an exact sort of relationship, linear or curved, but if something really stands out we should pay attention to that because strong patterns in the data that go unnoticed by us can mess up our models later down the road. -->

--------------------------------------------------------------------------------

# LAB 2
## More summary statistics

Expected lab duration: 30 minutes.

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/summarize-data-visualize.jpg" width="600"/></div>

--------------------------------------------------------------------------------

1. Find the summary statistics for the numeric column `price` and describe what you see. 
2. Do the same for the variable `make`. Why are there fewer summary statistics for `make` than `price`?
3. Look at a histogram (bar chart) for `make`. What are the most and least common values for `make`?
4. Look at the histogram for `price`. Describe the distribution of `price`.
5. In the "compare to" drop-down box, choose `horsepower` to see a scatter plot of `price` against `horsepower`. Describe what you see.

--------------------------------------------------------------------------------

6. In the "compare to" drop-down box, select "None" again to see the histogram for `price`. Since `price` is numeric, you can change the histogram to a boxplot by changing "view at" (next to where the number of rows and columns are reported).

<div style="text-align:center"><img src ="./images/view-as.jpg" width="400"/></div>

7. Describe the boxplot for `price`. What sort of information does the boxplot convey better than the histogram? And vice versa?

--------------------------------------------------------------------------------

8. In the "compare to" drop-down box, choose `make` to see a separate boxplot plot of `price` for each value of `make` (top 5 by default). Describe what you see.
9. Now drag in <button>Summarize Data</button>, run it and visualize it.
10. Interpret the 1st and 99th percentiles for `price` and compare them to the min and max. Does it seem like `price` has outliers? Does this confirm what we saw in the histogram for `price`?
11. Which columns in the data have a symmetric distribution and which ones have a skewed distribution?

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

# The importance of data visualization

<div style="text-align:center"><img src ="./images/anscombe-data.jpg" width="500"/></div>

https://en.wikipedia.org/wiki/Anscombe%27s_quartet

<!-- We're going to finish this chapter with a motivational example of why data visualization is important. It's kind of an extreme example, but it's meant to be a sort of poster child for the importance of visualizing your data as opposed to just relying on summary statistics. It's called "Anscombe's quartet", and it makes me think of "Asop's fables" every time I hear this name. First we're presented with four datasets, each consisting of a pair of variables X and Y. We're asked to speak to this dataset, and of course looking at numbers individually is kind of tedious, so we start by looking at some summary statistics. -->

--------------------------------------------------------------------------------

### The four datasets seem very similar
- The average x value is 9 for each dataset.
- The average y value is 7.50 for each dataset.
- The variance for x is 11 and the variance for y is 4.12.
- Are these 4 datasets similar? What does it look like if we plot this data?

<!-- As it turns out the four datasets have a lot in common: all the X variables have the same mean, as do all the Y variables. All the X's have the same standard deviation, or variance (which is just standard deviation squared), as do all the Y's. So same means and variances, and by now we might be tempted to think that the X's look very similar to each other, as do the Y's, and that whatever kind of relationship underlies X and Y in the four datasets is probably very similar too. Case closed, right? -->

--------------------------------------------------------------------------------

### Until you plot them, that is.
<div style="text-align:center"><img src ="./images/anscombe-plot.jpg" width="700"/></div>

<!-- It's only when you plot X and Y against each other that you notice how different the four datasets are. In the first one, X and Y seem to have a sort of linear relationship, and the nature of the relationship is statistical (or probabilistic) because there's a lot of uncertainty around it. In the second one X and Y appear to have curved relationship and it's a mathematical (or deterministic) relationship, in the sense that if you know how to mathematically describe the relationship (using an equation) then knowing X means you know Y, and vice versa. In the third dataset, X and Y have a linear relationship and it would be deterministic had it not been for the one data point that bucks the trend. If we try to fit a line through the data points, this one data point could exert undue influence on the slope of the line. Finally, in the last dataset, X appears to be a discreet numeric variable with only two values: 8 and 20. We can see that all the data points except for one have X = 8. This usually happens we have a numeric variable that should be thought of, and maybe even treated, as a categorical variable. So that was "Anscombe's quartet". A very coreographed example I admit, but it really does drive the point home about plotting our variables. In fact, notice that at least for the last dataset, even a univariate plot like a histogram would have indicated that something funny is going on with X. -->

--------------------------------------------------------------------------------

# Let's recap

- exploratory data analysis
- variable, column, row, observation
- numeric variables, categorical variables (including binary)
- nominal and ordinal variables
- mean, median, standard deviation, range, percentiles and quantiles
- univariate and bivariate summaries and visualizations
- histograms, boxplots, scatter plots

<!-- Take a look at what all you learned and see if you can point out a few important things about each of them. Then we take a small quiz and work on the lab.  -->

--------------------------------------------------------------------------------

# Quiz

True or false: a feature is a row in the data, a variable is a column in the data.

--------------------------------------------------------------------------------

# Answer

False.

> Features and variables usually refer to the same thing. Generally speaking we can think of a feature as a column in the data conveying some kind of information. Note that we usually have to do a lot of pre-processing to create useful features for modeling from the raw data.

--------------------------------------------------------------------------------

# Quiz

The average of a set of numbers is 200, but their median is 10. How can you explain this discrepancy?

--------------------------------------------------------------------------------

# Answer

> The data must be right-skewed (have some "outliers" in the positive direction). The mean (average) is dragged in the direction of outliers and therefore it's high. The median is not affected by outliers and remains low.

--------------------------------------------------------------------------------

# Quiz

What are some common reasons to perform EDA?

--------------------------------------------------------------------------------

# Answer

> Examine the distribution of each variable (skew, outliers, single peak, etc.).
> Examine correlations between variables.
> Find and try to account for missing values.
> Find more obvious trends and ask if they make sense.
> Know what kinds of pre-processing steps may be needed prior to any modeling.

--------------------------------------------------------------------------------

# LAB 3
## Creating a correlation matrix

Expected lab duration: 15 minutes.

--------------------------------------------------------------------------------

1. Connect the data to <button>Select Columns in Dataset</button>, launch the "column selector" and select all the numeric columns except `normalized-losses`.
2. Connect <button>Execute Python Script</button> to it and paste the python script (in the **next slide**) in the script box. Careful with tabs!
3. Run the experiment and right-click on <button>Execute Python Script</button>, select "Python Device" and then "Visualize".
4. Describe what you see. A high correlation implies a strong **linear** relationship between two variables. What does a low correlation imply?

--------------------------------------------------------------------------------

```python
def azureml_main(dataframe1 = None):
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("agg")
    import matplotlib.pyplot as plt
    cm=dataframe1.corr()
    fig=plt.figure()
    plt.imshow(cm,interpolation='nearest')
    plt.xticks(list(range(0,len(cm.columns))),
               list(cm.columns.values), rotation=45)
    plt.yticks(list(range(0,len(cm.columns))),
               list(cm.columns.values))
    plt.colorbar()
    fig.savefig("CorrelationPlot.png")
    return pd.DataFrame(cm)
```

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/correlation-matrix.jpg" width="800"/></div>

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

# End of chapter

<!-- So we're done with this chapter. I hope you enjoyed working on the lab. Something I mentioned at the start of the chapter is worth reiterating: EDA is part of parcel of the machine learning process, but because it's sort of open-ended it's something we get better at over time as we get better at noticing patterns and digging deeper. Ther are a lot of more advanced summaries and visualizations that can be used to facilitate the task, especially when dealing with very wide datasets, that is to say datasets with lots of columns (let's just say more than 100, although people usually have a much bigger number in mind). In such cases, it might be tedious to look at individual histograms, let alone all the possible pairs of scatter plots, but when you have so many variables there's bound to have relationships between some and we don't want to ignore those, and a correlation matrix like the one we saw in the lab can help. But we can also try to look at the data at a higher level than individual variables. Machine learning can be of help here too, and in fact in a later chapter we learn about principal component analysis as one approach. But more on that later. In the next chapter, we formally introduce machine learning and look at some important examples. See you then. -->

--------------------------------------------------------------------------------

# Chapter 3
## Machine learning through basic examples

<!-- Welcome to chapter 3. In this chapter we learn what exactly machine learning is, and what kinds of problems machine learning tries to solve. We then look extensively at some examples covering some fundamental ML algorithms and try to show you how they think by looking at the results they generate. -->

--------------------------------------------------------------------------------

# What we will learn

### supervised learning algorithms
- regression and classification
- prediction and scoring
- RMSE, MAE, R and R-squared
- accuracy, precision, recall
- training and test set

### unsupervised learning algorithms
- $k$-means clustering
- principal component analysis (PCA)

<!-- These are some of the terms we're going to learn in this chapter, so take a look at them and see if any of them ring a bell. If everything here is new to you then congratulations: you're about to add some pretty fancy words to your repertoire once this chapter is over. -->

--------------------------------------------------------------------------------

# What is machine learning?

An algorithm is a self-contained set of **rules** used to *solve problems* through data processing, math, or automated reasoning.

Machine learning is the field of study that gives computers the ability to learn <mark>without being explicitly programmed, using data (experience)</mark>.

The *problems* ML algorithms try to solve are usually (1) prediction and (2) finding structure in data, so the algorithms that do them are called <mark>supervised learning and unsupervised learning algorithms</mark> respectively.

<!-- We begin our discussion by trying to define machine learning more constructively. What we commonly refer to as machine learning is really just a set of algorithms, so let's start with what an algorithm is. For our purposes, we say that an algorithm is a a self-contained set of rules that solve a problem. A recipe is an algorithm, because it's a set of instructions for cooking a meal. So in that sense, a cookbook can be thought of as a set of algorithms, for cooking. So what makes machine learning algorithms so special is that their job is to learn from data. So without data, there's no machine learning. What we mean by "learning from data" is that an ML algorithm pores over data and try to find patterns or relationships and it describes them in a logical or mathematical way, that means through rules and equations. Sometimes those rules and equations are easy to comprehend and other times they make your head hurt. But the point I want to emphasize is that a machine learning algorithm is an algorithm that learns from data, and its output is also an algorithm with explicit rules that describe what we learned from the data. That's a mouth-full, so just repeat that in your head a bunch of times. We do machine learning because it can be used to find explicit rules so that we don't have to, because we're lazy and because it's not easy and because as data changes the rules might change too and we don't want to have to do it again. Broadly speaking, ML algorithms are used to do two things: make predictions (which we refer to as supervised learning) or find structure in the data (which we refer to as unsupervised learning). Making predictions is a very common task, and one that we humans don't seem to be good at, so supervised learning algorithms are by far the more commonly used ones in practice. -->

<!-- If we go back to our cookbook analogy, I mentioned that a cookbook is a set of algorithms, in this case recipes. A recipe is not an ML algorithm, because it doesn't used data to infer for example how much salt to use: it simply tells you how much salt to use. Now imagine we were too lazy to write a cookbook. But we had a magic algorithm that would watch cooking shows on TV for hours and hours every day and try to learn, which sounds pretty aweful if you ask me and I actually like cooking occasionally, but at the end this magical algorithm would produce one or several "ideal" recipes based on what it saw. Now the recipes too are themselves are algorithms, but not ML algorithms because they're explicit in the sense of being unambiguous instructions for cooking a meal. The only machine learning algorithm here is our magical algorithm that's addicted to cooking shows. And the data to our magical algorithm is a video of a cooking show, and its output is one or several "ideal" recipes (I say ideal because machine learning algorithms try to find some sort of optimum, even though it's hard to describe what exactly an idal recipe is). And usually, we'd expect that the more data we have, the better the recipes it produces. We'd also expect that better data would produce better recipes. Of course "better" is somewhat subjective here, but let's say for example that if we hope for at least some of these recipes to be healthy, we probably don't want our algorithm to binge-watch Paula Dean the whole time, so we throw some Jamie Oliver into the mix. Setting aside the fact that there would probably be some ethical issues around forcing an "intelligent" algorithm like that watch cooking shows hours on end, you can imagine that coming up with such a magical algorithm is a very difficult task, and so one probably doesn't exist at this point. In fact, machine learning problems that use video images (like facial recognition) are relatively new. So writing a cookbook is not one of those jobs that's going to be taken over by machines any time soon. Machine learning algorithms are still very limited in scope, but two things they can do well is make simple predictions (simple as in predicting a number or a category) and finding structure in the data. So maybe our cookshow-binging magical algorithm is far from producing a recipe that makes for a good meal, but at least it might be able to predict what meal someone is cooking (assuming the algorithm cannot listen or read, but only watch videos as a set of consecutive images) and that's a prediction problem, or what kinds of recipes there are (such as baking because for example it involes using eggs and flour, or roasting because it involves a big hunk of meat, or barbecue because it involves that guy with the spiky hair who only knows how to barbecue). Of course in this last example, the algorithm would know nothing about "baking" or "roasting". Instead it would sift through data and notice that some cook shows use a lot of the same ingredients or the same ratios or the same cook or what have you. And it many cases, it may make "mistakes" (and I'm using air quotes here because it's hard to tell what a mistake is). If for example we expect to see a separate category for "roasts" but the algorithm finds none, then whose fault is that? Do we need more data points, as in should the algorithm consume more cooking shows? Do we lack some important variables, as in do we need additional information that may not be captured by the video such as the inside-temperature of the meat (remember we're assuming the algorithm can't read or listen)? Or should we stop insisting that roasts deserve a special designation? And this is all assuming that we have an idea of what the different categories should be, which we sometimes don't. Of course the algorithm could also make a mistake when predicting something, and I'm not using air quotes here because this mistake is easy to catch. If the algorithm predicts that the video is one for baking a pizza and we watch it and realize it was a sweet potatoe pie instead, then that's a mistake, plain an simple. So we can see that there's some subjectivity in unsupervised learning that doesn't exist in supervised learning. -->

--------------------------------------------------------------------------------

# Two main types of ML problems

### supervised learning
- look at some examples (<u>labeled data</u>) and find a way to predict future (unlabeled) examples
- the <u>target variable</u> ("labels") contains the ground truth we want to **predict**
- by comparing predictions with the ground truth, we know how well we're doing

### unsupervised learning
- look at <u>unlabeled data</u> and find general patterns
- more subjective and difficult to interpret

<!-- So broadly speaking, ML algorithms are of two types: supervised and unsupervised learning. In order to do supervised learning, we need labeled data, which means data that has a column which corresponds to the variable we're trying to predict. We call that column the target. One good way to think of it is the that the target is the column with the ground truth. A supervised learning algorithm tries to predict what the value should be based on the relationship that it thinks exist between the target and the other variables is the data. So the algorithm can be used to make predictions for the target, which is why suprevised learning algorithms are also called predictive models. All we have to do is then compare our predictions to the ground truth to see how far off we are. This is great because it means that right off the bat we can dismiss any models that don't make good predictions, although as we'll see later, we should be suspicious of models that make very good predictions too. Data in unsupervised learning on the other hand is unlabeled, as in there is no target. This means there is no ground truth where unsupervised learning is concerned and a lot of room for subjectivity and more reliance on what makes sense for the problem at hand than just what the data says. -->

--------------------------------------------------------------------------------

# Supervised learning

We are trying to **predict** a variable (called <u>labels, target variable, response variable or dependent variable</u>) using other variables (called <u>features, explanatory variables, covariates, attributes or independent variables</u>).

- **regression** algorithms predict a *number* (numeric target)
- **classification** algorithms predict a *category* (categorical target)

Sometimes **regression** refers to a family of ML algorithms. For example, *linear regression* is a regression algorithm but *logistic regression* is a classification algorithm!

<!-- Most algorithms are of the supervised learning type, probably because prediction is a very important problem and one that we humans aren't good at. Let me clarify that we build a supervised learning algorithm to predict on future data, we're not talking just about predicting the future, in fact most supervised learning algorithm are not foretune-tellers. Future data is not so much about data about the future as it is about data we might obtain in the future but don't have now, and it represents what we don't know, or maybe I should say what we know we don't know, but let's not get philosophical. Future data could be potential customers we may be losing to competition, or anyone with a particular disease, or in fact data about the future, As we'll see later, the only requirement is for our future data to be fairly represented in our current data, so that whatever we learn from the current data can be generalized to the future data. So what are we predicting anyway? Well we're either predicting either a number, in which case we say we have a regression problem or we're predicting a category which we call a classification problem. So in regression our target is numeric, in classification it is categorical. Our features on the other hand, that's to say whatever other variables we think can help us make better predictions, can be numeric or categorical. We also call the target variable the response or dependent variable, and the features also go by a host of other names such as explanatory variables or independent variables. I know, it's way too many names for the same thing, and this reflects the fact that statistics is an inter-disciplinary subject and each discipline adopted its own set of terms. So if you're a computer scientist doing machine learning you're used to using features and target, if you're a statistician you're probably using explanatory and response variables, and if you're a psychologist maybe you perfer independent and dependent variables, and then there's the economists with their exogenous and endogenous variables, oh boy… Either way I highly recommended that you get familiar with these terms in case you come across them. -->

--------------------------------------------------------------------------------

# Supervised learning algorithms

Common examples of algorithms used include

- **tree-based algorithms** such decision tree, random forest, boosted trees
- **regression models** such as linear regression, logistic regression, lasso regression and elastic net
- **neural networks** including deep learning
- **support vector machines**
- **k-nearest neighbors**

Most of these algorithms can be used for *both* classification and regression, although the implementation is different in each case, and some algorithms are more appropriate than others.

<!-- Speaking about confusing things, let's go back to something I aluded to in the last slide but waited until we get here to raise it. Here's something to really grind your gears: the word regression as used by a statistician doesn't refer to algorithms that predict a number but a whole family of supervised learning algorithms with some commonalities. Usually statisticians don't use the word regression alone, but instead talk about linear and non-linear regression, polynomial regression, logistic regression, and so on. In some cases, such as logistic regression, the algorithm is actually a classification algorithm, not a regression algorithm, even though it has the word regression in it. So in this sense, we talk about regression algorithms or regression models, as opposed to say tree-based models. If you've been in this field for a while, usually it's pretty clear from context which "regression" we're talking about, so please be aware of that, and I try to elucidate some of this confusion in a later slide. So here are some example of supervised learning algorithms: we have tree-based models, regression models (where the word regression here is meant in the statistical context), neural networks and support vector machines and k-nearest neighbors. -->

--------------------------------------------------------------------------------

# Supervised learning: training

An ML algorithm is sometimes called a **model**. When we build a model on data we say we **train** or **fit** a model.

For example, we say we <mark>trained a decision tree on the data</mark>, or <mark>fitted a decision tree model to the data</mark>. The result is called a <u>trained model</u>. A trained model is also often referred to as a **model**, which can be confusing.

Sometimes, people use the word **model** for a trained model to distinguish it from the algorithm itself (which does not depend on data).

<!-- You may have heard data scientists refer to ML algorithms as models. It's a very common word to use and in fact I used it in the last slide when talking about regression models. A model is really just a simplification of something that's usually much more complex. When we put some very expensive clothes on an unattainably attractive human being and parade them around, we're basically saying yes, we're all different individuals, but if we buy these expensive clothes and wear them, all of us are going to look exactly like that. I think you're all with me when I say that's an over-simplification used as a marketing gimmick. We would like models to be simple, but not so simple that they become irrelevant. ML models are the same way. They can be simple or complex, but if they're too simple or too complex they're probably not very good models.

The process of feeding data to an ML model is called training a model, or fitting a model. For example, we might choose a decision tree as our model, train it on the data we have which includes the target variables and all the features, and as a result we get a tree-like structure that can be used to predict the target given the features. We call this a trained model, and this trained model can be used on any future data we get to obtain predictions, as long as the future data has the features the model expects in order to run the predictions. So think of the decision tree (as in the ML model) as one framework or one approach to solve this prediction problem. Another would be neural networks for example. The ML model is independent of the data. The trained model is what we get after we feed the data to the ML model. And so we can think of the trained model as an instance of the ML model, as is suggested by the data. Now you're going to love this: sometimes, we data scientists get a little sloppy in our choice of words and drop a word or two here and there, so you might hear people use the word model when they mean trained model. We do this because it's usually pretty clear from context which one we mean, and to help future data scientists train their ear to tell the difference, get it: "train" their ear. -->

--------------------------------------------------------------------------------

# Supervised learning: an analogy to training

Think of written language as a framework or a **model** for communication: it is a simplification of thoughts and emotions such that we can convey them to others (in written form).

- A written language can be an model (an abstraction, a framework).
- Written language can have different "flavors" (hieroglyphs, alphabets, emojis…).
- Some flavors are more complex than others (can express more complex thoughts).
- There are other frameworks for language: spoken language, miming, etc.

<!-- Time for another analogy: think of written language as a model because it is an attempt by us humans to communicate complex thoughts and emotions, and in this case it's not really a simple model because we can use it to communicate very complex things. Now if we train written language on the people in France, we get written French language. So written language is the model, French people taking pen to paper can be thought of as data, which makes the written French language the trained model we get if we feed that data to the model. And usually it's pretty clear from context when people talk about "written language" whether they're talking about written language as the abstraction for communicating thoughts, or written language as an instance of applying this framework to a group of people such as people living in France. So we usually refer to both the abstraction and an instance of the abstraction as models. For the same reason, both an ML algorithm itself and the trained model we get from appling the ML algorithm to some dataset are models, and the sloppiness is somewhat justified because it's usually clear from context. Another interesting parallel is that written language the abstraction can be thought of as a family of models and not necessarily just one, comprised of things like hieroglyphs, alphabets, and let's not forget emojis. Some of these are more complex and others are more simple, and complex here means that there are thoughts and emotions that some models express better than others. In the same way, the same family of ML models can have variations that make them more or less complex. Lastly, there are different frameworks for communication, such as spoken language, drawings or music or miming or mathematics if you think of those as languages, and similarly there are different families of ML algorithms such as tree-based versus regression basde, as we saw. -->

--------------------------------------------------------------------------------

# Supervised learning: scoring and evaluation

Once you have a trained model, you can use it to get predictions on *any* data (as long as it has the features needed by the model to run the predictions). This is called **scoring**.

If the data that you scored also has the target (or labels), we can compare scores (the predictions) to the target (the true values) to see how well the model predicts. This is called <u>evaluating a model</u>.

<!-- Once we have a trained model, we can make predictions on any data that has the same features as the ones used by the model to predict the target. Running predictions on a dataset is called scoring. Note that we trained model doesn't need the target itself to make predictions. In other words, we don't need labeled data in order to score: a trained model can be used to score labeled or unlabeled data. However, if the data we score is labeled, then in addition to scoring, we can also evaluate our scores, or predictions. That means that we can compare the predictions to the ground truth which is represented by the target variable. Without this, we'd never be able to tell how good the predictions are. How we evaluate the predictions depends on whether we're predicting numbers or categories, that is to say regression versus classification. -->

--------------------------------------------------------------------------------

# Regression evaluation metrics
| evaluation metric | definition | interpretation |
| ----------------- | ---------- | -------------- |
| Root Mean Squared Error | $\sqrt{\sum\frac{(observed - predicted)^2}{n}}$ | average prediction error |
| R-squared | $R^2$ where $R$ is the correlation between observed and predicted | percentage of variation *explained by* the model |

<!-- For regression algorithms, the most common evaluation metrics are the RMSE which stands for root mean squared error and the R-squared. The R in R-squared is just the correlation between the target variable and the predictions, or as statisticians would say it: the correlation between the observed values and predicted values. Since we're prediting a number, we can ask how far off our predictions are, on average, and that's what the RMSE answers. R-squared on the other hand expresses the fit as a percentage. To understand how to interpret R-squared you need to think like a statistician: first of all it should be clear that the target variable is something that varies, otherwise we would just predict the same number and be right every time. By building a model, we reduce its variation by a certain amount, in other words we explain away some of the variation by saying that they're predictable once we take into account the relationships between the features and the targed as captured by the model. What's left is variation that the model was not able to explain away. R-squared is the percentage of variation that the model was able to explain away. For example, a lot of the variation in people's height can be explained by their age, but not all of it of course otherwise everyone the same age would have the same height. So a model that tries to predict someone's height using their age can probably get a fairly good R-squared. -->

--------------------------------------------------------------------------------

# Binary classification

Binary (2 categories) classification is the most common kind of classification, because it can be used to answer (predict) **yes/no** or **true/false** questions.

A model makes predictions (positive or negative) which we compare to the actual answers (true or false). When the answers disagree we get a <span style="color:red">misclassification</span>. This can happen in two ways.

<!-- Evaluating classification models requires different evaluation metrics from regression. To simplify things, we're going to look at binary classification, which is the case of predicting between two categories only. This is because this kind of prediction problem is very common in real life, where we use machine learning algorithm to decide things such as whether a loan should be accepted or rejected, someone has cancer or not, or whether I look like Tom Cruise or Brad Pit. But also because for multi-class classification, where more than two categories are involved, very similar evaluation metrics exist and so it's mostly the math that's more involved so we stick to the binary case and leave it up to you to read about multi-class classification. -->

--------------------------------------------------------------------------------

# Confusion matrix

| | we actually observe positive case | we actually observe negative case |
| ------------------- | :------------: | :-------------: |
| **the model predicts a positive case** | <span style="color:blue">TP</span>| <span style="color:red">FP</span>|
| **the model predicts a negative case** | <span style="color:red">FN</span>| <span style="color:blue">TN</span>|

<!-- While there are some single-number evaluation metrics we can look for classification algorithms, it's hard to come down on a single number that says it all. So the best place to go is the confusion matrix. This is a matrix where the correctly-predicted cases show across the diagonals of the matrix and everything else is errors, or what we commonly call misclassifications. For binary classification, the matrix is two-by-two and conventially we name one of the classes TRUE and the other FALSE. The model's predictions are then either positive or negative, and a perfect model is one that predicts all the true cases and positive and all the false cases and negative.  But most datasets are noisy and so most models make mistakes, and there are only two kinds of possible mistakes or misclassifications: FPs, which is when we wrongly classify something as positive when its FALSE, in other words when it should have been classified as negative, and FNs which is the reverse scenario. The important point we want to remember from this slide is that we should pay attention to both of these numbers, although depending on the context one may be more important than the other, in the sense that we can be less forgiving of high misclassification for TPs than we are for TNs or vice versa. -->

--------------------------------------------------------------------------------

# Binary classification evaluation metrics

| evaluation metric | definition | interpretation |
| ----------------- | ---------- | -------------- |
| accuracy | <div style="text-align:center">$\frac{TP + TN}{TP + FP + FN + TN}$</div> | percentage of correctly classified cases |
| ROC curve | a visual representation of the model's performance | refer to [this great article](http://www.win-vector.com/blog/2009/11/i-dont-think-that-means-what-you-think-it-means-statistics-to-english-translation-part-1-accuracy-measures/) |
| AUC | area under the ROC curve | close to 0.5 is bad close to 1 is good |

<!-- With that said, we can try to come up with a single-number summary for evaluating binary classification models, and we start with the obvious one: the accuracy. The accuracy of a model is the fraction of misclassified cases. It seems like a pretty reasonable metric, but for simple reasons we kind of hinted at in the last slide, it not a good evaluation metric on its own, especially when we have inbalanced data (which is when there are a lot more of one category than the other in the data). A much better metric is the AUC, which is the area under the ROC. So what's the ROC you ask? Well the explanation would get us into territory I don't want to drag us into, so let me just say that it's a visual that probably does the best job of showing how well any given model can do at the limit. I've posted a link here that talks more about ROC, and I we examine what an ROC plot looks like when we get to the lab. -->

--------------------------------------------------------------------------------

# Supervised learning: recap

| term               | what is needed                              | results in           |
| ------------------ | ------------------------------------------- | -------------------- |
| training (a model) | appropriate ML algorithm + labeled data     | trained model        |
| scoring (data)     | trained model + data (labeled or unlabeled) | scores (predictions) |
| evaluating a model | scoring labeled data                        | evaluation metrics   |

More about scoring and model evaluation in the next chapter.

<!-- We're about to work on the coming lab and since we learned a lot, we're going to work on some extensive exercises to reinforce what we learned. But before starting on the lab I want to do a quick recap. So to train a model, we pick a model, or an ML algorithm and feed some labeled data to it. What we get is a trained model, which we also just call a model when we're being sloppy. With a trained model, we can score data to get predictions, and the data in this case doesn't have to be labeled, but if we want to evaluate a model's predictions then we need to score data that's labeled so we can compare the predictions to the ground truth.  -->

--------------------------------------------------------------------------------

| the machine learning community calls it…     | the community of statisticians calls it…           |
| -------------------------------------------- | -------------------------------------------------- |
| learning algorithm (or model)                | model                                              |
| supervised learning algorithm                | predictive model                                              |
| trained model (or just model)                | fitted model                                       |
| supervised learning                          | prediction problem                                 |
| unsupervised learning                        | data-mining or pattern recognition                 |
| features or attributes                       | explanatory or independent variables               |
| target or labels                             | response or dependent variables                    |
| training                                     | fitting                                            |
| scoring                                      | predicting                                         |

<!-- A big challenge when getting our feet wet with data science is just getting used to the jargon. There are a lot of terms that are thrown around and it doesn't help that some of it is not new words but existing words that have been reappropriated and given a new meaning. For example, the word "variable" means something very different to a statistician or data scientist than it does in a programming context. The situation as we saw is somewhat aggrevated by the fact that machine learning practitioners sometimes use a different set of terminology when talking about the same thing, which depends somewhat on their background, be it statistics, computer science, or even signal processing, and somewhat on just personal preference and who they think the cool guys are. So as part of this course, I've made it my mission to get you familiar with the jargon, and to save you from having to go back and review things on your own, I've summarized here some of the terms that we used so far. I won't go over it again but please take a moment to review them and make sure you're comfortable with them. For the most part, I try to adhere to a system for this course, but I might momentarily switch just to throw you a curve ball. -->

--------------------------------------------------------------------------------

# Quiz

True or false: In supervised learning, we have a target variable, but in unsupervised learning we only have features.

--------------------------------------------------------------------------------

# Answer

True

> The word "supervised" refers to the fact that we know the "ground truth" and therefore the predictions from the predictive model need to get as close as possible to this ground truth. In unsupervised learning there is no ground truth and results are much more subjective and difficult to evaluate.

--------------------------------------------------------------------------------

# Quiz

What is needed to train a model? Score data? Evaluate a model?

--------------------------------------------------------------------------------

# Answer

> We need labeled data to train a model. We also need to pick an ML algorithm that works for the problem at hand.
> We need a trained model and new data to score. The new data doesn't need to have labels.
> We need score labeled data to evaluate it.

--------------------------------------------------------------------------------

# Quiz

True or false: Labeled data is needed to train a (predictive) model, but not to evaluate it.

--------------------------------------------------------------------------------

# Answer

False.

> Labeled data is needed to both train a model and evaluate it. This is because when we evaluate a model, we compare the model's predictions to the ground truth.

--------------------------------------------------------------------------------

# Quiz

True or false: To score data using a trained model, the data must be labeled.

--------------------------------------------------------------------------------

# Answer

False.

> Once we have a trained model we can score data, labeled or unlabeled, to obtain predictions. But if the data is labeled, we can also evaluate the predictions.

--------------------------------------------------------------------------------

# LAB 4
## Regression

Expected lab duration: 45 minutes.

--------------------------------------------------------------------------------

<a name="backtolab4"> </a>

[Here is a screenshot](#screenshotlab4) of the finished experiment. Let's say you want to predict `price` using `horsepower`, `city-mpg`, and `body-style`. 

1. Is this a supervised or unsupervised learning problem?
2. Is it a classification or regression problem?
3. What are the target and features?
4. What are the response and explanatory variables?

--------------------------------------------------------------------------------

You have a few choices of algorithms you can try, and you will try **linear regression** and **decision tree** because they are fundamental building blocks for other more complex algorithms, and because they are easier to interpret which can help you build intuition around how ML algorithms work.

--------------------------------------------------------------------------------

Create a linear regression model for predicting price and run it (a screenshot of the final experiment is shown in the next slide).

1. Connect <button>Select Columns in Dataset</button> to the data and select only the columns we want to keep (the target and features).
2. Drag in <button>Linear Regression</button> and uncheck the box that says "Allow unknown level in categorical features".
3. Connect it to <button>Train Model</button> and select the target.
4. Run the experiment.

--------------------------------------------------------------------------------

<a href="#backtolab4" name="screenshotlab4">
<div style="text-align:center"><img src ="./images/simple-regression-example.jpg" width="700"/>
</div>
</a>

--------------------------------------------------------------------------------

5. Right-click on <button>Train Model</button> and choose "Trained model" then "Visualize". The numbers you are looking at translate into the following prediction equation:

```
predicted price = - 364.378
                  + 156.012 * horsepower
                  - 52.7053 * city-mpg
                  - 3510.22 (if body-type is "hatchback")
                  + 2793.26 (if body-type is "convertible")
                  + 1519.70 (if body-type is "hardtop")
                  - 1116.29 (if body-type is "station wagon")
                  - 50.8291 (if body-type is "sedan")
```

--------------------------------------------------------------------------------

6. Take the third row of the data and pass it through the above equation (you can use Excel to calculate predicted price). <mark>The difference between the observed price and predicted price for each row is called the **residual**.</mark> What is the residual for the third row?

For this model, we could compute the predicted values for every row by simply creating a new column (using <button>Execute R Script</button> or <button>Execute Python Script</button>) because the calculation is straight-forward.

--------------------------------------------------------------------------------

However imagine a linear model with dozens of features and you can see that hard-coding the above equation can get tedious. For more complex models such as neural networks and *ensemble models* hard-coding it would be a nightmare. Foretunately, we have <button>Score Model</button> to run predictions on the data without our having to hard-code it.

7. Connect <button>Train Model</button> and <button>Select Columns in Dataset</button> to <button>Score Model</button> to run predictions on the data.
8. To check your predictions by right-click on <button>Score Model</button> and choose "Score dataset" and "Visualize". Check that your prediction for the third row of the data matches what we found in (6).

--------------------------------------------------------------------------------

8. Connect <button>Score Model</button> to <button>Evaluate Model</button> and run it to evaluate the predictions. Note that we can do this here because the data we scores the ordinal data used to train the model (so it is labeled). We evaluate models so we make sure they are a good fit.
9. Right-click on <button>Evaluate Model</button> and select "Evaluation results" and "Visualize" to see the evaluation metrics. How is your overall fit for this model?

More on model evaluation in the next chapter.

--------------------------------------------------------------------------------

A **decision tree** is a very different kind of algorithm from linear regression. Linear regression describes the relationship between the features and the target a single equation. A decision tree keeps splitting the data into subsets until within each subset (the <u>leaves</u> of the tree) the target has similar values, and between the subsets the target has different values on average.

Sometimes when we use a decision tree to predict a number, we refer to it as a **regression tree** and reserve the word **decision tree** for use in classification.

--------------------------------------------------------------------------------

10. Change <button>Linear Regression</button> to <button>Decision Forest Regression</button> and set "Number of decision trees" to 1 and "Maximum depth of decision tree" to 4 and uncheck "Allow unknown values for categorical features". Run the whole experiment.
11. Right-click on <button>Train Model</button> and choose "Trained model" and "Visualize".
12. Right-click on <button>Score Model</button> and choose "Scored dataset" and "Visualize". The predictions are shown in the column called `Scored Label Mean`. Why is it common to see the same set of numbers for the predictions?

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/decision-tree-example.jpg" width="900"/></div>

--------------------------------------------------------------------------------

# END of LAB.

--------------------------------------------------------------------------------

# LAB 5
## classification

Expected lab duration: 30 minutes.

--------------------------------------------------------------------------------

<a name="backtolab5a"> </a>

1. Return to the experiment from the previous lab and click on <button>Select Columns in Dataset</button> and add the column `num-of-doors` to the columns selected.
2. Click on <button>Train Model</button> and change the target variable to `num-of-doors`.
3. Replace the algorithm with a <button>Two-Class Decision Forest</button> and set "Number of decision trees" to 1.
4. Re-run the experiment.

A screenshot of the experiment is shown in the [here](#screenshotlab5a).

--------------------------------------------------------------------------------

<a href="#backtolab5a" name="screenshotlab5a">
<div style="text-align:center"><img src ="./images/simple-classification-example.jpg" width="700"/></div>
</a>

--------------------------------------------------------------------------------

5. Right-click on <button>Score Model</button> and choose "Scored dataset" and "Visualize".
6. The predictions are shown in a column called `Scored Labels`. Each prediction is associated with a probabilty in the column `Scored Probabilties`. Find a row where a misclassification occured and see if you can guess why.
7. Right-click on <button>Evaluate Model</button> and choose "Evaluation results" and "Visualize". Report the accuracy and the AUC for this model.
8. What do the false negatives and false positives represent?

--------------------------------------------------------------------------------

<a name="backtolab5b"> </a>

9. Replace <button>Two-Class Decision Forest</button> with <button>Two-Class Logistic Regression</button> and re-run the experiment.
10. Is the new model better or worse than the old one? Justify your answer.
11. We can compare two models side by side in Azure ML. To do so, we copy and paste <button>Train Model</button> and <button>Score Model</button> and connect <button>Two-Class Decision Forest</button> to <button>Train Model</button>. See the screenshot [here](#screenshotlab5b).
12. Re-run the experiment and examine the side-by-side evaluation.

--------------------------------------------------------------------------------

<a href="#backtolab5b" name="screenshotlab5b">
<div style="text-align:center"><img src ="./images/classification-compare-models.jpg" width="800"/></div>
</a>

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

# Unsupervised learning

Unsupervised learning is about *finding structure* (natural groupings) in the data. There is no target, only features.

- The **$k$-means** algorithm attempts to find clusters in the observations (rows), such that two observations in the same cluster have similar features.
- **Principal component analysis** attempts to find clusters in the variables (columns) such that two variables within the same cluster contain similar (redundant) information.

<!-- As we alluded to before, supervised learning is far more common than unsupervised learning, partly because prediction is a common problem, but also because the ultimate test for a supervised learning algorithm is how good its predictions are. We'll talk more about this in the next chapter, but for now we turn our attention to unsupervised learning algorithms, which as we'll see are much harder to evaluate compared to supervised learning algorithms. In fact, the word unsupervised here refers to the fact that in this case there is no target, only features, and as such there is no ground truth. This makes unsupervised learning more subjective and hard to interpret. -->

--------------------------------------------------------------------------------

# Choosing the right $k$

<div style="text-align:center"><img src ="./images/clustering-visual.jpg" width="800"/></div>

<!-- Let's look at the poster-child example of unsupervised learning: k-means clustering. Let's say we have a dataset with only two features. We choose two because otherwise it's hard to visualize this problem. If I asked you how many groupings (also known as clusters) you see in here, I'd probably get some different answers. Some of you might say two, some four, and some six, and evreyone would be wrong and everyone would be right. So the correct answer is "It depends. How many clusters do you want to see?", but that's a scary answer, right? Well, at least we can say that we're not completely at sea here, because some answers require a bigger leap of faith than others. But we should also be in agreement that there isn't a single answer. -->

--------------------------------------------------------------------------------

# $k$-means clustering

- The **$k$-means clustering** is an algorithm that attempts to find grouping in the rows of the data. 
- It finds similar data points (observations) when we compare their features. 
- So $k$-means clustering <mark>finds **redundancy** in the data across rows</mark>.
- We choose $k$ (the number of clusters) and $k$-means gives us a new column showing the cluster assignments for each row.

<!-- So we looked at the two-dimensional case, but k-means can apply to more dimensions. The goal is to compare different observations across their features and find a unique cluster that each observation fall into. Let me rephrase this in the following way: replace observation with row, feature with column, and we get k-means compares different rows across columns and finds a unique cluster that each row falls into. It does require us to choose k, as we saw in the last slide but we can usually make a reasonable guess about that. So what's the point of doing this? Well, one way to think about it is that by grouping similar observations we are finding redundancy in the data. We are saying that two observations from different clusters have some differences where such and such feature is concerned, but most of the differences can be accounted for by the differences between their corresponding clusters. Similarly, we're saying that two observations within the same cluster are different as far as such and such feature goes, but their differences are negligible compared to observations in other clusters. In other words, observations within the same cluster are redundant, and as far as we're concerned all of them could be thought of as one and represented by their cluster centroid, which is sort of like the average profile for that cluster. Now I was intentionally sloppy when I said such and such features, because of course the hard question to answer is which features are responsible for making this cluster different from this other cluster and to what extent. This is why usually running the k-means algorithm is only the beginning, because now the hard task of differentiating one cluster from another begins, and it's also why we usually prefer a smaller k, because the larger the k the harder it becomes to justify smaller and smaller differences across more and more clusters. -->

--------------------------------------------------------------------------------

# Quiz

In $k$-means clustering, what are the advantages and disadvantages of choosing a higher $k$?

--------------------------------------------------------------------------------

# Answer

> A higher $k$ means we have more clusters. The advantage is that we can capture more complex patterns in the data (in this case think of it as more *niche* clusters", if this is desirable. The disadvantage is that having more clusters means we have to do more work to understand and explain differences between them. A much larger $k$ also means longer run-time for the algorithm.

--------------------------------------------------------------------------------

# LAB 6
## $k$-means clustering

Expected lab duration: 30 minutes.

--------------------------------------------------------------------------------

<a name="backtolab6"> </a>

We are going to run the $k$-means clustering algorithm to see how it can divide the cars into groups. A screenshot of the final experiment is shown [here](#screenshotlab6).

1. Create a new experiment with <button>Automobile price data (Raw)</button> and use <button>Select Columns in Dataset</button> to drop the columns `symboling`, `normalized-losses`, `make`, `fuel-type`, `engine-location`, `bore`, `stroke` and `compression-ratio`.
2. Use <button>Clean Missing Data</button> to replace any missing data from numeric columns with the  average of the non-missing data for that column.
3. Drag in <button>Normalize Data</button> and use a MinMax transformation and apply it to all the numeric columns.

--------------------------------------------------------------------------------

<a href="#backtolab6" name="screenshotlab6">
<div style="text-align:center"><img src ="./images/simple-clustering-example.jpg" width="700"/></div>
</a>

--------------------------------------------------------------------------------

<mark>**Normalizing** a variable means that we change its scale by applying a mathematical transformation to it.</mark> The **MinMax** transformation replaces the variable $X$ with the following rescaled version of $X$:

$$\frac{X - min(X)}{max(X) - min(X)}$$

This puts the variable $X$ on a scale of 0 to 1. Some ML algorithms require us to normalize variables before passing them to the algorithm otherwise variables on a larger scale skews the results. Some algorithms have normalization built into them, so we don't have to use <button>Normalize Data</button>.

Normalizing is also sometimes called <u>standardizing</u> or <u>rescaling</u>.

--------------------------------------------------------------------------------

4. Drag in <button>K-Means Clustering</button> and set "Number of controids" to 4.
5. Drag in <button>Train Clustering Model</button> and select all the columns in the data.
6. Drag in <button>Edit Metadata</button> so we can look at the data with a column containing the cluster assignments.
7. Run the experiment and right-click on <button>Edit Metadata</button> and select "Results dataset" and "Visualize". Scroll to the right to find the column with the cluster assignment.
8. Right-click on <button>Edit Metadata</button> and select "Results dataset" and "Save as Dataset". Call it `Automobile data (with clusters)`. We will return to this data in the next lab.

--------------------------------------------------------------------------------

9. Now begins the hard part of understanding what makes the clusters different from one another. Click on the `Assignment` column to see a bar plot of the clusters. The numbers 0-3 (one for each cluster) are only nominal. Use the "compare to" drop-down list to create two-dimensional plots that compare the distribution a given column across the 4 clusters. Two such examples are shown in the next slide, one for `price` (numeric) and one for `fuel-type` (categorical). Compare the distribution of at least 3 variable across the 4 clusters and based on that put together a "profile" for each cluster.

--------------------------------------------------------------------------------

<img src ="./images/clusters-vs-price.jpg" width="500"/>
<img src ="./images/clusters-vs-fueltype.jpg" width="500"/>

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

# Principal component analysis

- **Principal pomponent analysis** attempts to find groupings of the features.
- It finds features that are similar (relay similar information because they are highly correlated) and combines them into one feature called a principal component. 
- <mark>PCA finds redundancy in the data across columns</mark> and each principal component (PC) tries to capture <u>left-over variation</u> that was not captured by PCs that came before it.
- PCA is an example of a <u>dimensionality reduction</u>: Usually, the first few principal components captures most of the variation in the data. So we replace our original $p$ features with the first $m$ principal components, where $m$ should be much smaller than $p$.

<!-- Another common example of an unsupervised learning algorithm is principal component analysis. In a way, you could say that principal component analysis does to features what k-means does to observations: it tries to find redundancy, but in the columns instead of the rows. When two observations are similar it implies that their features are about the same. When two features are similar it implies that there's some kind of relationship that binds the two together and that the relationship holds true for most of the observations in the data. Redundancy in our observations is usually okay, and in fact it's something we should expect. And we can always use k-means to see which observations are close to each other and what their average profile is, if that's something we care to know about. Redundancy in the features on the other hand can spell trouble for us down the road, for many reasons which we'll alude to only briefly at the end of this chapter. So PCA does two things for us, and this is where the analogy we drew with k-means comes apart a little: first of all PCA gives us principal components, which are new features that can be derived by combining the original features. The first principal component captures most of the variation in the original features, in other words it contains the most information, followed by the next principal component, and so on. And on top of that, each principal component is unrelated to the others, which means they all carry a unique sort of information. So we pick the top m principal components as containing most of the same information as the original features, even though m is usually quite a bit smaller than p, the number of original features, because unlike the original features the PCs are not redundant. It's usually hard to tell what kind of "information" each principal component relays, because each principal component is derived in a way by taking a weighted average of the original features. But this is how you can think of it: the first PC is an abstract feature that brings out the most important "aspect" of the original features, the second PC is an abstract feature that brings out the next most important "aspect" of the original features, and so on. Only thing is, it's not exactly easy to tell which "aspect" exactly PC1 represents, and which "different aspect" PC2 represents, and so on, but that's why we call it unsupervised learning. And just like k-means, we can examine the principal components and try to make more sense of them, but in practice it's hard, time-consuming and somewhat subjective. -->

--------------------------------------------------------------------------------

# LAB 7
## Principal component analysis

Expected lab duration: 30 minutes.

--------------------------------------------------------------------------------

The $k$-means algorithm (and other algorithms that rely on "locality") suffer from two problems:

- Numeric variables with larger scale can influence it more. As we saw, the remedy was to rescale the variables.
- <mark>When there are lots of features, it becomes harder to find "similar" points, because even small differences are magnified over many dimensions. This is referred to as the <u>curse of dimensionality</u>.</mark> One remedy for this is to use principal component analysis to reduce the dimensionality of the data prior to clustering.

--------------------------------------------------------------------------------

<a name="backtolab7"> </a>

A screenshot of this lab can be seen [here](#screenshotlab7). Return to the clustering experiment from the last lab, but make the following changes:

1. Use <button>Select Columns in Dataset</button> to keep all numeric columns except `normalized-losses`.
2. Use <button>Clean Missing Data</button> to replace any missing data from numeric columns with the  average of the non-missing data for that column.
3. Use <button>Normalize Data</button> and use a Z-Score transformation and apply it to all the numeric columns. A Z-Score transformation replaces the variable $X$ with $\frac{X - mean(X)}{sd(X)}$.
4. Drag in <button>Principal Component Analysis</button> on all the columns and choose 5 for "Number of dimensions to reduce to" and uncheck the "Normalize dataset" box. Run the experiment.

--------------------------------------------------------------------------------

<a href="#backtolab7" name="screenshotlab7">
<div style="text-align:center"><img src ="./images/simple-pca-example.jpg" width="700"/></div>
</a>

--------------------------------------------------------------------------------

5. Right-click on <button>Edit Metadata</button> and choose "Results dataset" and "Visualize". Do you see your principal components? Which principal component does the best job of discriminating between the clusters? 
6. Right-click on <button>Edit Metadata</button> and choose "Results dataset" and "Save as Dataset" and call it `Automobile data (with clusters using PCA)`.
7. Start a new experiment and drag in `Automobile data (with clusters)` and `Automobile data (with clusters using PCA)` and connect both to <button>Add Columns</button> so we combine them column-wise into one data.
8. Drag in <button>Select Columns in Dataset</button> and choose only the original columns in the data and the cluster assignments. The columns end up in the order you select them.

--------------------------------------------------------------------------------

9. Right-click on <button>Add Columns</button> and choose "Results dataset" and "Visualize".
10. Use <button>Edit Metadata</button> to change the variable names for the cluster assignments to `clusters_wo_pca` and `clusters_with_pca` (Careful which is which!).
11. Create a two-way table comparing cluster assignments with and without PCA. What has changed?
12. Pick one cluster try examine its features to see what old "profile" with the new "profile". Did we do a better job of separating profiles with the new cluster assignments using PCA? Answering this question is not easy and takes a lot of "slicing and dicing".

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/clustering-withpca-compare.jpg" width="600"/></div>

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

| $k$-means                                    | principal component analysis                  |
| -------------------------------------------- | --------------------------------------------- |
| finds redundancy across rows                 | finds redundancy across columns               |
| must choose $k$ before                       | must choose $m$ (the top PCs)                 |
| groups observations into distinct clusters   | combines features into orthogonal PCs         |
| create a column of cluster assignments       | creates one column per principal components   |
| each observation falls into a unique cluster | each PC is a weighted average of all features |
| clusters can still share similarities        | PCs are orthogonal to each other              |
| "profiling" cluster centroids can be hard    | interpreting PCs is hard                      |

<!-- Let's summarize what we learned about k-means and PCA so you can compare and contrast the two algorithms. I think their biggest common denominator is that both algorithms ultimately look for redundancy in the data, with k-means going across rows and PCA going across columns. But k-means does so by assigning similar points into the same cluster, and PCA figures out how to combine the original features to get the first PC, then the second PC, and so on. One big distinction between PCA and k-means clustering is that k-means gives us distinct clusters and every row of the data falls into one and only one cluster. PCA on the other hand gives us principal components, where each principal component is a linear combination (like a weighted average) of all the original features in the data. Any one principal component may have higher weights associated with certain features, but the distinction is not clear-cut. On the other hand, PCs have the advantage of being orthogonal to each other, which is a fancy word for saying they are not related to each other so that each PC represents a separate "aspect" of the features, whereas clusters in k-means can still share similarities, just not across the whole feature set. -->

--------------------------------------------------------------------------------

# Some additional observations

--------------------------------------------------------------------------------

Because unsupervised learning deals with unlabeled data, we can still **"train"** a **"model"** on data and **"score"** data using a trained model (quotes are used to emphasize that the terms are used more loosely), but what makes it unsupervised is that <mark>evaluating a model is very difficult and subjective because no true labels are present</mark>.

It is best to avoid terms like training and scoring with unsupervised learning algorithms.

<!-- Because the data is unlabeled in unsupervised learning, there is no "training", no "model", no "scoring", and especially no "evaluating" to be had. But you might sometimes hear data scientists say that they "trained" a k-means model on a dataset, which basically just means they ran the algorithm on the dataset. In fact, if we go with the broad definition of models, we can call k-means a model, and in fact we could even call it a predictive model in the sense that if we have future data, we can still assign each row to a cluster which cluster centroid it is closest to. So even scoring makes sense in this context. But this still doesn't make k-means a supervised learning algorithm, because the data is remains unlabeled and as such our clusters are hard to evaluate. Personally, I prefer to use words like training and scoring only in the context of supervised learning algorithm to avoid the confusion. -->

--------------------------------------------------------------------------------

Although clustering and PCA are unsupervised learning algorithms, machine learning workflows often involve <mark>combining supervised and unsupervised learning algorithm</mark>. Examples:

- run $k$-means to build clusters and use clusters as one of the features in a predictive model
- run PCA and use the top few principal components as features in a linear regression model: this is called principal component regression
- run PCA on a dataset with lots of features and use only the top $m$ to run $k$-means on the data: this is useful because $k$-means does not perform well on high-dimensional data.

<!-- Let's make one last point about machine learning algorithms. We started the chapter by distinguishing between supervised and unsupervised learning algorithms, but in practice a workflow involving machine learning can mix and match these two in order to solve difficult problems. Here's a few examples showing how: we could use k-means to build clusters, which results in a new column in our data showing the cluster assignments, and we could throw this in as one of the features in a predictive model. We can run PCA and use the top few PCs as the features in a linear regression models, and if we do that then we probably want to throw the original features out of the model. This is called principal component regression. The benefit of using PCs as features is that they are orthogonal, and this is a plus in linear regression because having redundant features (what statisticians call multi-collinearity) can cause our predictions to be somewhat erratic. -->

--------------------------------------------------------------------------------

# Let's recap

### supervised learning algorithms
- regression and classification
- prediction and scoring
- RMSE, MAE, R and R-squared
- accuracy, precision, recall
- training and test set

### unsupervised learning algorithms
- $k$-means clustering
- principal component analysis (PCA)

<!-- So this is it folks. We covered a lot in this chapter so take a look at some of the terms and topics we covered and make sure that you return and review them if need be. In the next chapter, we'll focus mainly on supervised learning algorithms and delve deeper into how to prepare the data for predictive modeling and how to fairly evaluate our predictive models. See you then. -->

--------------------------------------------------------------------------------

# End of chapter

--------------------------------------------------------------------------------

# Chapter 4
## Concepts in Machine Learning

--------------------------------------------------------------------------------

# What we will learn

- Fitting, training, modelling
- Predicting, scoring
- Pre-processing:
    - Aggregating, cleaning, reshaping, feature extraction.
    - Handling missing values and outliers
    - Feature creation
- Model complexity, overfitting and underfitting
- Model interpretability vs prediction accuracy

--------------------------------------------------------------------------------

# The Machine Learning Process

<div style="text-align:center"><img src ="./images/machine-learning-process.jpg" width="900"/></div>

--------------------------------------------------------------------------------

# Part 1: Pre-processing data

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/machine-learning-process-1.jpg" width="900"/></div>

--------------------------------------------------------------------------------

Once we have a business questions in mind we need to get the data ready. <mark>Data in its raw form is almost never ready for modeling</mark>, so we begin by pre-processing data. <u>Pre-processing</u> data is everything we do to the raw data before we can feed it to one of the machine learning algorithms. Common pre-processing tasks involve:

- Aggregate, sample data
- Clean data by treating missing values and/or outliers
- Feature extraction and transformation
- feature engineering

--------------------------------------------------------------------------------

# Aggregate and/or sample

- Raw data is sometimes too <u>granular</u> for modeling, or <u>biased</u> toward more frequent observations.
- <mark>The granularity of the data affects the interpretation of our model</mark> and we can aggregate data to make it less granular.
- Aggregating data can also dampen the number of missing values and the effect of outliers.
- Sampling data can remove bias posed by more frequent observations in the raw data.

--------------------------------------------------------------------------------

# Treat missing values and outliers

- Some models are more "sensitive" to missing values and outliers than others.
- There are many ways to <u>impute</u> missing values, some get very fancy.
- In some cases, outliers are exactly what we're interested in, such as anomaly detection. In other cases, outliers can get in the way of building good models.
- <mark>What exactly should be an outlier is somewhat subjective.</mark>

--------------------------------------------------------------------------------

# Feature extraction and transformation

Depending on the model, transforming our features can make them easier to interpret or more accurate. Here are some common transformations we might consider:

- **Normalization or standardization** has to do with <u>rescaling</u> variables so they are more or less on the same scale.
- **Binning, bucketing, or discretizing** turns a variable with high-cardinality into one with low cardinality. It can be applied to both numeric and categorical features.
- A new feature can be a clever combination of existing features which can reduce redundancy in the data or bring out some of its more hidden aspects (feature engineering can do the same).

--------------------------------------------------------------------------------

# Feature engineering

- <u>Feature engineering</u> is the idea is that we can automatically extract new features from the raw data that give us more accurate models than the original features.
- But it can also can make it hard to interpret our models.
- Some models such as neural networks have feature engineering built into the algorithm. Others may require more trial-and-error (such as using principal components in regression).

--------------------------------------------------------------------------------

# Part 2: Model building and evaluation

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/machine-learning-process-2.jpg" width="900"/></div>

--------------------------------------------------------------------------------

# An analogy for training and testing

- You are going to take an exam (call it future exam) in a subject you know almost nothing about (like a driver's test)
- You have a practice exam sheet with lots of questions
- You can use it to study for the future exam
- <mark>How do you estimate (predict) your score on the future exam?</mark>

--------------------------------------------------------------------------------

# Answer

You can't use the training portion to test yourself because you could then "study" by just memorizing the answers.

To remedy this, we use the <u>holdout method</u>: *randomly* divide the practice exam into two parts
- Call the bigger part the <u>training portion</u> and use it to study
- Call the smaller part the <u>testing portion</u> and use it to test yourself by pretending it's the future exam

If you learned well from the training portion, your score on the future exam should be only slightly worse than your score on the testing portion.

--------------------------------------------------------------------------------

# Overfitting

- A similar situation to "memorizing the answers" can happen with models.
- <mark>A good model should capture meaningful trends (signals) in the training data, meaning trends that generalize to data outside the training data (out-of-sample as statisticians call it).</mark>
- An apparent trend that fails to generalize to out-of-sample data (noise) should be ignored by the model. Otherwise the model is said to overfit.
- Without a test data, we can't distinguish the signal from the noise.
- The more "complex" models are more likely to overfit.

--------------------------------------------------------------------------------

# Model complexity

- The same model can be made more complex by including more features or by different choices for some of its <u>hyperparameters</u> (such asa tree's depth). Hyperparameters are inputs to the model that must be specified but can not be directly *learned*.
- Some models are just more complex than others (such as a random forest versus a decision tree, neural networks versus linear models, …). More complex models are said to be <u>high-variance</u>, and more simple models are said to be <u>high-bias</u>.

--------------------------------------------------------------------------------

# Complexity for the same model

<div style="text-align:center"><img src ="./images/train-test-sets.jpg" width="700"/></div>

--------------------------------------------------------------------------------

# Complexity for different models

<div style="text-align:center"><img src ="./images/model-accuracy-interpretability.jpg" width="700"/></div>

--------------------------------------------------------------------------------

|don't do this|why?|do this instead|
|-|-|-|
|simply throw all our variables at the model|multi-collinearity (feature redundancy)|variable selection or feature engineering|
|simply pick the most accurate model|more likely to overfit, harder to interpret, maybe less efficient|decide on the right trade-off between accuracy and complexity|

--------------------------------------------------------------------------------

# "Models should be simple, but not simplistic."

--------------------------------------------------------------------------------

Click on the image to download.
<div style="text-align:center"><a href="http://download.microsoft.com/download/A/6/1/A613E11E-8F9C-424A-B99D-65344785C288/microsoft-machine-learning-algorithm-cheat-sheet-v6.pdf"><img src ="./images/azureml-algo-cheatsheet.jpg" width="800"/></a></div>

--------------------------------------------------------------------------------

# "Machine learning is part art part science."

--------------------------------------------------------------------------------

# Resources:

You can learn more here about how to choose a machine learning algorithm: 

https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-algorithm-choice#considerations-when-choosing-an-algorithm

--------------------------------------------------------------------------------

# Quiz

True or false: When building models, there is no point extracting less granular features from more granular features (for example, month from a datetime column). More information is always better.

--------------------------------------------------------------------------------

# Answer

False.

> More granularity is only good as far as it contributes more to the "signal" and less to the "noise". So while it's not easy to give a straight-forward answer (because it depends on the use-case) it is false to say that more granular features are always better.

--------------------------------------------------------------------------------

# Quiz

- What are the benefits of more complex models?
- What are the benefits of simpler models?

--------------------------------------------------------------------------------

# Answer

> More complex models can have higher predictive accuracy than more simple models, but this usually comes at the cost of longer training time and scoring time. More complex models are also need more data, otherwise predictions can have high variance. Finally, more complex models make it harder to explain how the predictions came about. Simple models require less data, are more explainable, usually train faster and they can be even easier to deploy.

--------------------------------------------------------------------------------

# Quiz

True or false: overfitting affects more simple models.

--------------------------------------------------------------------------------

# Answer

False.

> Complex models are more prone to overfitting than more simple models. We can offset that effect by using more data, but we may need *a lot* more data.

--------------------------------------------------------------------------------

# Quiz

A model shows very high error rate on both training and test data. What should be the next steps?

--------------------------------------------------------------------------------

# Answer

> If the error is high both on the training and the test set, then the model is failing to capture significant relationships. In this case we need to try a more complex model. We can also try to find more informative features.

--------------------------------------------------------------------------------

# Quiz

Why does having more features not necessarily result in better models?

--------------------------------------------------------------------------------

# Answer

> Throwing more features at an algorithm is usually only helpful if (1) the feature is a useful predictor for what we're trying to model and (2) the feature contains new information that other features so far don't already capture (otherwise, we will have too many correlated features which can increase the variance of our predictions).

--------------------------------------------------------------------------------

# LAB 8
## Revisiting model evaluation

Expected lab duration: 30 minutes.

--------------------------------------------------------------------------------

<a name="backtolab8"> </a>

In this exercise, we run an experiment similar to the ones from the last chapter, but using a more complex model. We then add a new module that splits the data into training and test set. We examine the effect of splitting the data on the model's evaluation metrics. Finally, we repeat all of this for a simpler model to see if we can see the same effect. A screenshot of this lab can be seen [here](#screenshotlab8).

--------------------------------------------------------------------------------

1. Start a new experiment and drag in the <button>Automobile price data (Raw)</button>.
2. Drag in <button>Select Columns in Dataset</button> and keep the following features: `body-style, num-of-doors, wheel-base, engine-size, horsepower, highway-mpg, price`.
3. Drag in <button>Two-Class Boosted Decision Tree</button> and in the drop-down for "Create trainer mode" select "Parameter range". This allows us to select different values for the two hyperparameters in th model, such as the maximum number of leaves, the minimum leaf size, the learning rate, and the number of trees to construct. Uncheck the box that says "Allow unknown levels…"

--------------------------------------------------------------------------------

4. Train, score and evaluate a <button>Two-Class Boosted Decision Tree</button> for predicting `num-of-doors`. You should be familiar with this process now.
5. The AUC we obtained was on the training data, so it can make us over-confident in the model's predictive ability. Use <button>Split Data</button> to first split the data into training and test sets (use an 75-25 split). Notice that <button>Split Data</button> has two outlets. The one on the right is the training data, and the one on the left is the test data. Note that you can hold the CTRL key and select multiple modules, copy them and paste them back into the canvas.

--------------------------------------------------------------------------------

6. Train the data on the training dataset, then score the test data and evaluate your scores.
7. Compare the AUC from evaluating the scores on the training data to the AUC from evaluating the scores on the test. Which one is higher? Why?
8. Replace <button>Two-Class Boosted Decision Tree</button> with <button>Two-Class Logistic Regression</button> and rerun the experiment. What do you see now?

--------------------------------------------------------------------------------

<a href="#backtolab8" name="screenshotlab8">
<div style="text-align:center"><img src ="./images/boosted-nosplit-split.jpg" width="800"/></div>
</a>

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

# Ensemble models

A boosted decision tree is an example of an <u>ensemble model</u>. The idea behind ensemble models is that while any single model may not make great predictions, we improve our predictions by using the "wisdom of crowds": We can build multiple "variations" of the same model (algorithm) and combine their results (<mark>by averaging them if it's regression and using majority rule if it's classification</mark>). In addition to making better predictions, ensemble models usually also make more stable predictions: small changes in the data cause only small changes in the predictions.

Two of the most common ensemble modeling techniques are <u>bagging</u> and <u>boosting</u>.

--------------------------------------------------------------------------------

# Bagging

- An ensemble where the *same* model is built multiple times on different samples of the data.
- An example of a **random forest**, which is just a collection of decision trees.
- Bagging can be done <u>in parallel</u>, since each model is built independently.
- Bagging reduces a model's variance, not its bias, so it's suitable for complex models.

--------------------------------------------------------------------------------

# Boosting

- A sequential ensemble method where each model is trying improve upon the previous model by putting more emphasis on those observations the previous model had difficulty predicting
- An example is a gradient boosted decision tree.
- Boosting reduces a model's bias, not its variance, so it's suitable for high-bias (simpler) models.

--------------------------------------------------------------------------------

# Part 3: Model deployment

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/machine-learning-process-3.jpg" width="900"/></div>

--------------------------------------------------------------------------------

# What we will learn

- Development and production
- Scaling and consumption
- The Azure Machine Learning Studio
- The data science process
- The data science workflow

--------------------------------------------------------------------------------

# Development vs production

- When we develop models, we want to be unhindered so we can focus on the analysis, but this mindset can get us trouble when taking our code to production.
- We should consider how the model is to be used in production. In a production environment <mark>we are not just concerned with model accuracy, but also how the model scales with data (scalability) and how the model is consumed (operationalization)</mark>.
- The requirement imposed on us by the production environment can often send us back to the development phase to reiterate.

--------------------------------------------------------------------------------

# Scoring in production

In production models are usually used to make predictions, also known as <u>scoring</u>. Predictions can be made 

- **in batch**: scoring future data in one go, done on a schedule (such as nightly or hourly) as future data accumulates, can be used to power up dashboards and reporting systems.
- **online**: scoring a single case with <u>real-time response time</u>, can be used to make <u>intelligent applications</u>.

Operationalizing a model to make batch vs online predictions usually involves very different considerations.

--------------------------------------------------------------------------------

# Model retraining in production

A model's accuracy may degrade over time, as the future data that the model scores starts to deviate from the training data that was supposed to represent it. If a sample of the data at the time the model was built looks "different" (statistically speaking) from a sample of the data now. So we occasionally <u>retrain</u> or <u>refresh</u> models to reflect these changes in the model and improve the accuracy of future predictions.

--------------------------------------------------------------------------------

# What can go wrong in production?

|what happens|possible solutions|
|-|-|
|scoring is slow|choose a simpler model or scale out (parallel scoring is easy)|
|retraining (or refreshing) models fails on larger datasets|choose a simpler model or scale out (non-trivial)|
|predictions occasionally fail|check edge cases and make sure output is specific and predictable|

--------------------------------------------------------------------------------

# Quiz

- What’s the most common way a dashboard consumes models?
- What’s the most common way a webapp consumes models?

--------------------------------------------------------------------------------

# Answer

> A dashboard can have models generate predictions in batch so the predictions are ready to be served by the dashboard. However, it's also possible to have real-time dashboards where models need to score new data as it streams in.
> A webapp usually needs to be able to score data *online* (as opposed to *batch*).

--------------------------------------------------------------------------------

# Quiz

For each of the terms below state if the concept is more relevant to development or to production:
Model evaluation

- Variable selection
- Scoring future data
- Scoring the test data
- How well a model scales

--------------------------------------------------------------------------------

# Answer

> Variable selection: we do this during training
> Scoring future data: we test this during development and implement it in production
> Scoring the test data: we do this so we can evaluate a model during training
> How well a model scales: this is a question that usually comes up in the context of scoring in production, but we can also ask this question during development when we have big data and longer training times

--------------------------------------------------------------------------------

# Quiz

State two reasons for why more accurate models are not always better.

--------------------------------------------------------------------------------

# Answer

> More accurate models are generally more complex, so they are less explainable and demand longer training time and longer scoring time (which can affect production).


--------------------------------------------------------------------------------

### In Azure Machine Learning, we can

- Deploy web services
- Retrain models through APIs
- Manage web service endpoints
- Scale a web service
- Consume web service

--------------------------------------------------------------------------------

Both batch and online scoring is available in Azure Machine learning as a web service:

- **Request-Response Service (RRS)**: A low latency, highly scalable service that provides an interface to the stateless models created and deployed by using Machine Learning Studio.
- **Batch Execution Service (BES)**: An asynchronous service that scores a batch for data records.

--------------------------------------------------------------------------------

# LAB 9
## Deploying a model in AzureML

Expected lab duration: 15 minutes.

--------------------------------------------------------------------------------

<a name="backtolab9"> </a>

1. Return to the last lab and delete all the modules associated shown in [this screenshot](#screenshotlab9), then rerun the experiment.
2. Click on "Set Up Web Service" and choose "Predictive Web Service" which is a scoring web service. This creates a new tab next to "Training experiment" called "Predictive experiment". You see some changes happening and modules being rearranged in the canvas. Describe what changed. Why did <button>Evaluate Model</button> disappear? Why is <button>Automobile price data (Raw)</button> greyed out? What are the two modules that were added in?

--------------------------------------------------------------------------------

<a href="#backtolab9" name="screenshotlab9">
<div style="text-align:center"><img src ="./images/modules-to-delete.jpg" width="700"/></div>
</a>

--------------------------------------------------------------------------------

3. Run the experiment, then click on "Deploy Web Service". On the new page that opens click on "New Web Services Experience". On this page, we can test and monitor our web service.
4. Under "Basic" click on the link called "Test endpoint". Under "input1", fill in the following values for the inputs: `body-style = sedan`, `horsepower = 102`, and `city-mpg = 18`. Then scroll down and click on "Test Request Response". Under "output1" you should now see the predicted price in the field called "Scored Labels".
5. Is this an example of batch prediction or online? Why were the other input fields not required?
6. Browse around the other sections and see if you can guess what each section is used for.

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/web-service-dashboard.jpg" width="900"/></div>

--------------------------------------------------------------------------------

# END OF LAB

--------------------------------------------------------------------------------

# Let's recap

- Fitting, training, modelling
- Predicting, scoring
- Pre-processing:
- Aggregating, cleaning, reshaping, feature extraction.
- Handling missing values and outliers
- Feature creation
- Model complexity, overfitting and underfitting
- Model interpretability vs prediction accuracy

--------------------------------------------------------------------------------

# The data science workflow

<div style="text-align:center"><img src ="./images/data-science-workflow.jpg" width="700"/></div>

--------------------------------------------------------------------------------

# Resources

- Data pipeline scenarios in AzureML: https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-data-science-plan-sample-scenarios
- Scaling an Azure Machine Learning web service by adding additional endpoints: https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-scaling-webservice

--------------------------------------------------------------------------------

# End of chapter

--------------------------------------------------------------------------------

# The end

--------------------------------------------------------------------------------

## thank you
www.linkedin.com/in/sethmott/

--------------------------------------------------------------------------------

<div style="text-align:center"><img src ="./images/microsoft-logo-white.jpg" /></div>

--------------------------------------------------------------------------------

