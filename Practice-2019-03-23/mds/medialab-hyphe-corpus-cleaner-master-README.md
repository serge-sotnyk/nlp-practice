# Hyphe Corpus Cleaner

Simple script and related Docker container to automatically remove old corpus from an Hyphe instance.


## Cleaner options
The following options permit to set the clean policy :

- `CRON_SCHEDULE`: When you want start a clean. For example, to clean each day set `0 0 0 * * *`

A cron expression represents a set of times, using 6 space-separated fields.

Field name   | Mandatory? | Allowed values  | Allowed special characters
----------   | ---------- | --------------  | --------------------------
Seconds      | No         | 0-59            | * / , -
Minutes      | Yes        | 0-59            | * / , -
Hours        | Yes        | 0-23            | * / , -
Day of month | Yes        | 1-31            | * / , - ?
Month        | Yes        | 1-12 or JAN-DEC | * / , -
Day of week  | Yes        | 0-6 or SUN-SAT  | * / , - ?

- `HYPHE_API_URL`: Hyphe API URL to clean. For example, `http://HYPHE_HOST/HYPHE_PATH/api/`
- `HYPHE_MONGODB_HOST`: Mongo hostname.
- `HYPHE_MONGO_PORT`: Mongo hostname.
- `HYPHE_MONGO_DBNAME`: Mongo database name.
- `HYPHE_ADMIN_PASSWORD`: Admin password if set in backend config.
- `DAYSBACK`: Days to keep.
- `MAILER_HOST`: SMTP server hostname.
- `MAILER_PORT`: SMTP server port.
- `MAILER_FROM`: `From:` email address.
- `MAILER_TO`: `To:` email address(es). For example,  `name@provider.net,name2@provider.net`.


You also need to link this container to `mongo` and `backend` containers.

Sample for your `docker-compose.yml`:
```
services:
  cleaner:
    image: scpomedialab/hyphe-corpus-cleaner:latest
    links:
     - "mongo:mongo"
     - "backend:backend"
    environment:
     - CRON_SCHEDULE=0 30 04 * * *
     - HYPHE_MONGODB_HOST=mongo
     - HYPHE_API_URL=http://backend:6978/
     - HYPHE_MONGODB_PORT=27017
     - HYPHE_MONGODB_DBNAME=hyphe
```

