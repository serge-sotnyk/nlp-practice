# Laravel Table Tenancy (laratt)
> Allow for multi-tenancy by using table prefix

[![Build Status](https://travis-ci.org/niiknow/laratt.svg?branch=master)](https://travis-ci.org/niiknow/laratt)[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE.md)

Also see [laratt-api](https://github.com/niiknow/laratt-api) where this project was originally built and refactored.

**Install**:
```
composer require niiknow/laratt
```

**Config**:
```
php artisan vendor:publish --provider="Niiknow\Laratt\LarattServiceProvider"
```

## Features
- [x] Use special character `$` for tenant and table separator.  Most database allow for this character.
- [x] Dynamic table as `tenant$table_name`
- [x] Tenant resolution use `X-Tenant` header by default; though, it is customizable by providing a static function for `resolver` config.
- [x] A generic Controller Trait that provide simple and flexible CRUD (create, retrieve, update, delete) REST endpoint.
- [x] Simple query and bulk delete `/list` REST endpoint.
- [x] jQuery DataTables as `/data` endpoint with [laravel-datatables](https://github.com/yajra/laravel-datatables) 
- [x] Pre-defined structured schema for `ProfileModel`
- [x] Schedulable and ecommerce schema type for `TableModel`
- [x] Cloud auditable (s3 backed) of individual record transaction.  This allow you to trigger aws lambda on some event instead of having to create scheduled jobs.
- [x] Being able to include and exclude table from auditable - so you don't have to audit things like when you're using it for logging, caching, or when client doesn't need it for some particular reason. 

**CONS** It doesn't support table relationship.

## API Schema
The image below is from our Swagger documentation of the [laratt-api](https://github.com/niiknow/laratt-api) project.
![](https://raw.githubusercontent.com/niiknow/laratt/master/api.png?raw=true)

[Table Schema](https://github.com/niiknow/laratt/blob/master/src/Models/TableModel.php#L77)

Special multi-tables endpoint @ `/api/v1/tables/{table}`; where `{table}` is the table name you want to create.  `{table}` must be all lower cased alphanumeric and underscore with mininum of 3 characters to 30 max.  Example, let say `x-tenant: clienta` and `{table} = product`, then the resulting table will be `clienta$product`.

Also note that there are two ids: `id` and `uid`. `id` is internal to **laratt**.  You should be using `uid` for all operations.  `uid` is an auto-generated guid, if none is provide during `insert`.

Providing a `uid` allow the API `update` to effectively act as an `merge/upsert` operation.  This mean that, if you call update with a `uid`, it will `update` if the record is found, otherwise `insert` a new record.

- `/list` endpoint is use for query and bulk `DELETE`, see: [Query Syntax](#query-syntax)
- `/data` endpoint is use for returning jQuery DataTables format using [laravel-datatables](https://github.com/yajra/laravel-datatables).
- `/import` bulk import is csv to allow for bigger import.  Up to 10000 records instead of some small number like 100 for Azure Table Storage (also see admin config to adjust).  This allow for efficiency of smaller file and quicker file transfer/upload.
- `/truncate` truncate all data from table.
- `/drop` drop a table.  Why not?  Now you can do all kind of crazy stuff with table.

What about your own/custom schema?  See example of our [Profile Schema](https://github.com/niiknow/laratt/blob/master/src/Models/ProfileModel.php#L78)

## Query-Syntax
This library provide simple query endpoint for search and bulk delete: `api/v1/profile/list` or `api/v1/tables/{table}/list`

### Limiting

To limit the number of returned resources to a specific amount:

```
/list?limit=10
/list?limit=20
```

### Sorting

To sort the resources by a column in ascending or descending order:

```
/list?sort[]=column:asc
/list?sort[]=column:desc
```

You could also have multiple sort queries:

```
/list?sort[]=column1:asc&sort[]=column2:desc
```

### Filtering

The basic format to filter the resources:

```
/list?filter[]=column:operator:value
```

**Note:** The `value`s are `rawurldecode()`d.

#### Filtering Options

| Operator | Description | Example |
| --- | --- | --- |
| eq | Equal to | `/list?filter[]=column1:eq:123` |
| neq | Not equal to | `/list?filter[]=column1:neq:123` |
| gt | Greater than | `/list?filter[]=column1:gt:123` |
| gte | Greater than or equal to | `/list?filter[]=column1:gte:123` |
| lt | Less than | `/list?filter[]=column1:lt:123` |
| lte | Less than or equal to | `/list?filter[]=column1:lte:123` |
| ct | Contains text | `/list?filter[]=column1:ct:some%20text` |
| nct | Does not contains text | `/list?filter[]=column1:nct:some%20text` |
| sw | Starts with text | `/list?filter[]=column1:sw:some%20text` |
| nsw | Does not start with text | `/list?filter[]=column1:nsw:some%20text` |
| ew | Ends with text | `/list?filter[]=column1:ew:some%20text` |
| new | Does not end with text | `/list?filter[]=column1:new:some%20text` |
| bt | Between two values | `/list?filter[]=column1:bt:123\|321` |
| nbt | Not between two values | `/list?filter[]=column1:nbt:123\|321` |
| in | In array | `/list?filter[]=column1:in:123\|321\|231` |
| nin | Not in array | `/list?filter[]=column1:nin:123\|321\|231` |
| nl | Is null | `/list?filter[]=column1:nl` |
| nnl | Is not null | `/list?filter[]=column1:nnl` |

You can also do `OR` and `AND` clauses. For `OR` clauses, use commas inside the same `filter[]` query:

```
/list?filter[]=column1:operator:value1,column2:operator:value2
```

For `AND` clauses, use another `filter[]` query.

```
/list?filter[]=column1:operator:value1&filter[]=column2:operator:value2
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

