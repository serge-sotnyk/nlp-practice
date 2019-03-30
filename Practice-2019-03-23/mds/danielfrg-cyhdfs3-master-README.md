# cyhdfs3

Cython based wrapper for [libhdfs3](https://github.com/PivotalRD/libhdfs3).

## Install

Requirements are basically [`libhdfs3`](https://github.com/PivotalRD/libhdfs3)
and [`cyavro`](https://github.com/PivotalRD/libhdfs3) both are available as conda
packages: `conda install -c https://conda.anaconda.org/blaze https://conda.anaconda.org/mvn libhdfs3 cyavro`

Then you should be able to: `pip install cyhdfs3`

## Basic usage

```python
# Needed by libhdfs3
import os
os.environ["LIBHDFS3_CONF"] = "/etc/hadoop/conf/hdfs-site.xml"

import cyhdfs3

# Default host: localhost, port: 8020
client = cyhdfs3.HDFSClient()

data = b'0' * 250 * 2 ** 20
data += b'1' * 250 * 2 ** 20

f = client.open('/tmp/temp', 'w')
f.write(data)
f.close()

f = client.open('/tmp/iris.csv', 'r')
print f.readline()
print f.readline()
print f.readline()
print f.readline()
print f.readline()
f.close()
```

## Development/Play environment

```bash
# Docker container with conda and libhdfs3: Connect to remote HDFS
docker build -t cyhdfs3 .
docker run -it -v $(pwd):/cyhdfs3 -v $(pwd)/../cyavro:/cyavro cyhdfs3

# Docker container with conda, libhdfs3 and HDFS (Pseudo Distributed mode)
docker build -t cyhdfs3.hdfs -f Dockerfile.hdfs .
docker run -it -p 8020:8020 -p 50070:50070 -v $(pwd):/cyhdfs3 -v $(pwd)/../cyavro:/cyavro cyhdfs3.hdfs

# Bash inside the container
docker exec -it $(docker ps -q -l) bash
```

