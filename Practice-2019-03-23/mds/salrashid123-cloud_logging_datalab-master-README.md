
# Using Google CLoud Logging With Datalab/Jupyter Notebooks

[Google Cloud Datalab](https://cloud.google.com/datalab/docs/) allows users to easily visualize and transform data using standard Jupyter/iPython notebook syntax.  Google Cloud provides several client libraries that automatically provide dataframes populated with GCP Data.  For example, Datalab's [google.datalab.stackdriver.monitoring](https://googledatalab.github.io/pydatalab/datalab.stackdriver.monitoring.html)  package can be use in a notebook to render Cloud Monitoring data.  Similarly, [datalab.bigquery](https://googledatalab.github.io/pydatalab/datalab.bigquery.html) can cover BQ logs (the latter being the most common usecase by far).

However, this article focuses on something different:  using Google Cloud Logging data inside a notebook direcly.  GCP allows you to export your data from Cloud Logging to BQ which means you can apply BQ dataframes  anyway but applying logs within specific windows allows for quick ad-hoc analysis and visualizaitons.

Target audience for logs-based dataframes would be for devOPS, incident analyis, log-based metric visulizations or even data engineers seeing to refine and create explatory models.

> Disclaimer: i do not know pandas or dataframes.  The samples below is a crude pass at generating them from logs.  I hope you can use/extend the model here for (if you do find it useful, LMK)


## Setup

- Install [Visual Studio Code](https://code.visualstudio.com/)
- Add Following Extensions:
-  -  IPython for VSCode
-  -  Jupyter
-  -  VS Code Jupyter Notebook Preview
-  -  Python

- Then configure environment:

```bash
  virtualenv env
  source env/bin/activate
  pip install -r requirements
```

- Configure `VSCode` prjoject settings
-  - `.vscode/settings.json`
```json
    {
        "python.pythonPath": "${workspaceFolder}/env/bin/python",
        "python.linting.pylintEnabled": false
    }
```

### Monitoring

Using Datalab/Python notebooks is a fairly common usecase and is well documented:

  - https://cloudplatform.googleblog.com/2017/01/explore-Stackdriver-Monitoring-data-with-Cloud-Datalab.html
  - https://googledatalab.github.io/pydatalab/datalab.stackdriver.monitoring.html
  - https://cloud.google.com/monitoring/datalab/quickstart-datalab
  - https://github.com/googledatalab/notebooks/blob/master/tutorials/Stackdriver%20Monitoring/Time-shifted%20data.ipynb
- https://github.com/googledatalab
- https://github.com/googledatalab/notebooks/tree/master/samples


This article will not focus on this but here is a sample output using `VSCode` and the pregenerated dataframes from Cloud Monitoring:

-  ![images/gcm_notebook.png](images/gcm_notebook.png)

### Logging (AuditLogs)

Analytics using Google BigQuery based audit logs is likewise well documented.  If you export any AuditLogs to BigQuery, you can directly run analytics over large datasets in BQ:
 - [https://cloud.google.com/bigquery/audit-logs](https://cloud.google.com/bigquery/audit-logs)

The preceeding article describes raw BQ primitives but you can also create a dataframe easily in jupyter for BQ by hand:

- [https://cloud.google.com/bigquery/docs/visualize-jupyter](https://cloud.google.com/bigquery/docs/visualize-jupyter)

or just use [datalab.bigquery](https://googledatalab.github.io/pydatalab/datalab.bigquery.html) python module.

Finally, this article was about getting the full flexiblity to use cloud logging and dataframes.  To that end you can iterate over BQ logs usign `google.cloud.logging` primitives and consturct the dataframes.  In most cases, its better to use the built in bq dataframes.

  - [BQ AuditLogs datafarames with cloud Logging](https://gist.github.com/salrashid123/5bc0e0d954a959c90660860846f12f36)

  - ![images/bq_audit_dataframe.png](images/bq_audit_dataframe.png)


#### AppEngine

This is where it gets interesting: you can convert arbitrary logs into dataframes using cloud logging.  Any data you can query over cloud logs can get converted in for ad-hoc analysis and visualization _even without_ a BQ export.  Infact, you can precisely query the window/interval in logs and correlate it directly with datasources outside of GCP (i.,e create dataframe between cloud-providers).

In the example below, I'm using cloud logging to render GAE Application logs metadata:

  - ![images/gae_log_dataframe.png](images/gae_log_dataframe.png)

#### CustomLogs

Suppose you not only want a datafarame to cover application log metadata but rather go a level deeper and parse out a datafarame within a log event.

For example, if in appengine, i emit a log line in JSON like this:

- JSONPayload:
```json
{ 
  'page': 1,
  'fruits': [ 'apple', 'peach']
}
and
{ 
  'page': 2,
  'fruits': [ 'mango', 'peach']
}
```
  - ![images/gae_log_json.png](images/gae_log_json.png)


What I'd like to do is not just mine the logs but also the datainside it and create a dataframe from within that.  Thats also possible with cloud logging (and bigquery with its [JSON_EXTRACT_SCALAR](https://cloud.google.com/bigquery/docs/reference/legacy-sql#json_extract_scalar) capability.  

In the example below, you can modify the notebook to parse out the message and generate the dataframe with the embeded data too:

  - ![images/gae_log_json_parsing.png](images/gae_log_json_parsing.png)


  Here is a static dataframe demonstrating this

  - [GAE Log message Dataframe](https://gist.github.com/salrashid123/a95282518f79fe218786db087c84c55d) 




## Conclusion

You can ofcourse apply this to any logs in cloud logging (Audit, AppEngine, Compute Engine, GKE, etc).  My intent with this post isn't to provide a prescriptive solution but rather to point out some usecases for devOPS teams and dataengineers to quickly create notebooks based on any GCP logs.  The specific constructions of the dataframe isn't described here but please feel free to use the samples here to get started.


## Appendix


### Cloud Logging Filters

Sample filters you can apply for Cloud Logging

```python
resource.type="gae_app"
resource.type="bigquery_resource"
resource.type="gce_instance"
logName="projects/mineral-minutia-820/logs/cloudaudit.googleapis.com%2Factivity"
logName="projects/mineral-minutia-820/logs/cloudaudit.googleapis.com%2Fdata_access"


FILTER = ('resource.type="gae_app" AND logName="projects/mineral-minutia-820/logs/appengine.googleapis.com%2Frequest_log" AND timestamp >= "2018-06-27T00:00:00Z"')
FILTER = ('resource.type="bigquery_resource" AND severity="INFO" AND timestamp >= "2018-06-27T00:00:00Z"')
FILTER = ('logName="projects/mineral-minutia-820/logs/cloudaudit.googleapis.com%2Fdata_access" AND timestamp >= "2018-06-27T00:00:00Z"')
FILTER = ('logName="projects/mineral-minutia-820/logs/cloudaudit.googleapis.com%2Factivity" AND timestamp >= "2018-06-27T00:00:00Z"')
```

### Python protobuf imports

Due to [https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5514](https://github.com/GoogleCloudPlatform/google-cloud-python/issues/5514), Cloud Logging
does not correctly parse `proto_pb` messages that are returned.   To work around that, you need to configure each known protobuf package from the raw `.proto` file.

Specifically, the following imports will not work with google cloud logging python:

```python
      - import google.appengine.logging.v1.request_log_pb2
        `"type.googleapis.com/google.appengine.logging.v1.RequestLog"`
      - import google.cloud.audit.audit_log_pb2
        `"type.googleapis.com/google.cloud.audit.AuditLog"`
      - import google.cloud.bigquery.logging.v1.audit_data_pb2
        `"type.googleapis.com/google.cloud.bigquery.logging.v1.AuditData"`
      - import google.appengine.v1.audit_data_pb2
        `"type.googleapis.com/google.appengine.v1.AuditData"`
      - import google.iam.v1.logging.audit_data_pb2
        `"type.googleapis.com/google.iam.v1.logging.AuditData"`
      - import google.resourcemanager.audit_config_pb2
        `"type.googleapis.com/google.resourcemanager.AuditConfig"`
      - import google.api.servicecontrol.v1.log_entry_pb2
        `"googleapis/google/api/servicecontrol/v1/log_entry.proto"`
```

To do this, first

- install protoc

```
    curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip
    unzip protoc-3.2.0-linux-x86_64.zip -d protoc3
    sudo mv protoc3/bin/* /usr/local/bin/
    sudo mv protoc3/include/* /usr/local/include/
```

- Load and install the `.proto` files in the notebook folder setup in the 'install' step earlier:

```
      git clone https://github.com/googleapis/googleapis.git
```

```bash
      protoc --python_out=env/local/lib/python2.7/site-packages/  \
            --proto_path=googleapis \
            googleapis/google/appengine/logging/v1/request_log.proto

      touch env/local/lib/python2.7/site-packages/google/appengine/__init__.py \
        env/local/lib/python2.7/site-packages/google/appengine/logging/__init__.py \
        env/local/lib/python2.7/site-packages/google/appengine/logging/v1/__init__.py

      protoc --python_out=env/local/lib/python2.7/site-packages/  \
            --proto_path=googleapis googleapis/google/cloud/audit/audit_log.proto

      touch env/local/lib/python2.7/site-packages/google/cloud/audit/__init__.py

      protoc --python_out=env/local/lib/python2.7/site-packages/  \
            --proto_path=googleapis googleapis/google/cloud/bigquery/logging/v1/audit_data.proto

      touch env/local/lib/python2.7/site-packages/google/cloud/bigquery/__init__.py \
            env/local/lib/python2.7/site-packages/google/cloud/bigquery/logging/__init__.py \
            env/local/lib/python2.7/site-packages/google/cloud/bigquery/logging/v1/__init__.py

      protoc --python_out=env/local/lib/python2.7/site-packages/  \
            --proto_path=googleapis googleapis/google/appengine/v1/*.proto

      touch env/local/lib/python2.7/site-packages/google/appengine/v1/__init__.py

      protoc --python_out=env/local/lib/python2.7/site-packages/  \
            --proto_path=googleapis googleapis/google/iam/v1/*.proto

      touch env/local/lib/python2.7/site-packages/google/iam/v1/__init__.py \
            env/local/lib/python2.7/site-packages/google/iam/__init__.py

      protoc --python_out=env/local/lib/python2.7/site-packages/  \
            --proto_path=googleapis googleapis/google/iam/v1/logging/audit_data.proto

      touch env/local/lib/python2.7/site-packages/google/iam/v1/logging/__init__.py

      protoc --python_out=env/local/lib/python2.7/site-packages/  \
            --proto_path=googleapis googleapis/google/api/servicecontrol/v1/log_entry.proto

      touch env/local/lib/python2.7/site-packages/google/api/servicecontrol/v1/__init__.py \
            env/local/lib/python2.7/site-packages/google/api/servicecontrol/__init__.py
```

