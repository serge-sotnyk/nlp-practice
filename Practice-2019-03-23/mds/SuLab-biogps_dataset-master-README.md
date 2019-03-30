
## Detailed steps needed to have a local development version of [BioGPS](http://biogps.org/#goto=welcome), for dataset loading


## Setting up your local development environment:

Make sure you use **git** for version control (May 2016 Biogps_dataset was migrated to [Github](https://github.com/SuLab/biogps_dataset))

### Clone repository and make virtual environment (use your Github username of course!)

- `git clone https://github.com/JTFouquier/biogps_dataset.git`
- `virtualenv biogps`
- `source biogps/bin/activate`
- `pip install -r requirements.txt`

### You must have three main components running in order to see datasets

#### 1) SSH into the remote BioGPS database

Because the dataset database is much too large to install on computer for local development, you need to request a connection to our dev db server

#### 2) Run the local host server

The settings_dev file is a "secret file." Please see Chunlei or BioGPS project manager.

- `python3 manage.py runserver_plus --settings=biogps_dataset.settings_dev`

#### 3) Run Elastic Search

**Install Elastic Search using [these directions](https://www.astic.co/guide/en/elasticsearch/reference/current/_installation.html):**

Elastic search is a search server based on Lucene.

It is a full-text search engine with an HTTP web interface and schema-free JSON documents.

Elastic search is developed in Java and is released
as open source under the terms of the Apache License.

From within the elasticsearch folder that you set up, run:

- `./bin/elasticsearch`

## Next, get data from a BioGPS user/researcher
You will need to get an info sheet, factors sheet and RNAseq data/matrix file from a scientist.

### Does the local dataset you are loading have gene symbols in it and is it an RNAseq dataset?

If yes, then you **must** run **`reporter_to_entrezgene.py`**, which will use mygene.info to replace **gene symbols** with **Entrezgene IDs.**

Entrezgene IDs are absolutely necessary for Biogps.org data display, but for microarray datasets, keep the probe set reporters.

## Dataset Parsers:

- **load_ds** command which will load *remote* datasets (Microarray data from [ArrayExpress](https://www.ebi.ac.uk/arrayexpress/)) to remote server for dev or prod.
- **load_ds_local** command will load *local* datasets to the remote server for dev or prod. (written for RNAseq)

Run the command like this using Django manage.py, where "load_ds_local" can be other commands:
- `python3 manage.py load_ds_local --settings=biogps_dataset.settings_dev`

Then you must use the command es_index to "index the data", then the newly loaded dataset should appear in the chart file:
- `python3 manage.py es_index --settings=biogps_dataset.settings_dev`
Use the "-c" argument if you want to clear previous indexing
- `python3 manage.py es_index -c --settings=biogps_dataset.settings_dev`

Output looks something like this:
- `added 16 platform, added 5914 dataset`

## Open this url and you should see bar charts!
#### http://localhost:8000/static/data_chart.html

*Must sometimes restart the localhost and server that is containing the database, as well as elasticsearch.*

**For help:**
- `python3 manage.py load_ds --help --settings=biogps_dataset.settings_dev`

## Instances (models) to create during dataset loading:
If you don't know what a model is, then read about [Django](https://www.djangoproject.com/)!

* **dataset:**
    * Model with information about a certain dataset including metadata.

* **dataset_matrix:**

    * is the dataset matrix that contains the **entire** dataset from the RNA seq run. Meaning, you likely do not want to display an instance of this model all at once!

* **dataset_data:**
    * is one reporter gene, and all of it's expression information for all samples.

* **Dataset Platform:**
    * We created a new platform since now we're loading a sequencing (not microarray) dataset.
This is a sequencing platform, so does not have to be recreated every time.

    * Example input information:
        * RNA seq
        * reporters empty list
        * name = "generic RNA seq platform for mouse"
        * species = mouse

#### Biogps takes the average of samples for you so you don't need user average

### Misc. information for testing/developing BioGPS:

urls from mygene.info used to get the Entrezgene IDs from gene symbol (from reporter_to_entrezgene):

- `http://mygene.info/v2/query?q=symbol:CDK2`
- `http://mygene.info/v2/query?q=symbol:0610005C13Rik`

## To access the dataset via the shell:
- `python3 manage.py shell_plus --settings=biogps_dataset.settings_dev`

#### Run these commands from shell:

This returns the dataset object which is the foreign key for dataset data and dataset matrix:
- `ds = BiogpsDataset.objects.get(geo_gse_id="BDS_00015")`

This returns all the metadata (from info sheet and factors):
- `ds.__dict__`

## Viewing datasets on your BioGPS localhost

Dropdown menu in "probeset" is also considered the reporter gene on BioGPS

Go to the URL for the specific gene and dataset name (primary key of dataset or geo_gse_id)
geo_gse_id is also important: will be BDS_XXXXX next number in sequence)

Example dataset viewing urls:
- `http://localhost:8000/static/data_chart.html?gene=67669&dataset=10044`
- `http://localhost:8000/static/data_chart.html?gene=12566&dataset=BDS_00015`
- `http://localhost:8000/static/data_chart.html?gene=100152011&dataset=10078`

Example admin:
- `http://localhost:8000/admin/dataset/biogpsdataset/2427/`

Standard test gene is 1017, which is a *human* gene! So if you are using a mouse
dataset, this will understandably be missing:

CDK2 cyclin-dependent kinase 2, Homo sapiens (human)
Gene ID: 1017, updated on 6-Mar-2016

Cdk2 cyclin-dependent kinase 2, Mus musculus (house mouse)
Gene ID: 12566, updated on 6-Mar-2016

You can also check the "fixed reporters" data file to see which Entrezgene IDs are actually in your dataset for
viewing.

## To view the full dataset (api) for a dataset and gene:
- `http://localhost:8000/dataset/full-data/geo_gse_id%20test/gene/12566/`
- `http://localhost:8000/dataset/full-data/E-GEOD-16054/gene/1017/`
- `http://localhost:8000/dataset/full-data/BDS_00001/gene/1017/`


## Misc. Information

### Does your dataset have interesting tissue groups or organ systems?

If so, then change the color_idx in the json metadata (ex: admin/dataset/biogpsdataset/2509/) accordingly to group samples into meaningful groups. This is done manually due to the numerous variations of possible sample groupings

### Make sure to run Flake8 (to check for Pep8 compliance), prior to pushing code to biogps_dataset repository.
