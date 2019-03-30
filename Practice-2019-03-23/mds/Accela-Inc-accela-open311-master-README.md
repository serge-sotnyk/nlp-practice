## Accela Open311

An Open311 server that integrates with Accela Automation.

## Supported Response Formats

JSON, XML

## API Methods

### Get Service Request Types

<code>http://[API endpoint]/services.[format]</code>

HTTP Method: GET

Parameters:

| Name  | Required  |
|:--|:-:|
|  jurisdiction_id | Y  | 

Sample Response:

```json
[
  {
    "module": "ServiceRequest",
    "service_code": "ServiceRequest/Animals/Animal Nuisance/NA",
    "value": "ServiceRequest-Animals-Animal.cNuisance-NA",
    "metadata": false,
    "type": "realtime",
    "keywords": "Animal Nuisance",
    "group": "ServiceRequest",
    "service_name": "Animals",
    "description": "Animal Nuisance"
  },
  {
    "module": "ServiceRequest",
    "service_code": "ServiceRequest/Buildings and Property/Fence Dispute/NA",
    "value": "ServiceRequest-Buildings.cand.cProperty-Fence.cDispute-NA",
    "metadata": false,
    "type": "realtime",
    "keywords": "Fence Dispute",
    "group": "ServiceRequest",
    "service_name": "Buildings and Property",
    "description": "Fence Dispute"
  }
]
```

### Get List of Service Requests

<code>http://[API endpoint]/requests.[format]</code>

HTTP Method: GET

Parameters:

| Name  | Required  |
|:--|:-:|
| jurisdiction_id | Y  | 
| limit | N |
| offset | N |

Sample Response:

```json
[
    {
        "address": "", 
        "agency_responsible": null, 
        "description": null, 
        "media_url": "http://thisisface.com", 
        "requested_datetime": null, 
        "service_code": "ServiceRequest-Water.cand.cSewage-Leaking.cFire.cHydrant-NA", 
        "service_name": "Leaking Fire Hydrant", 
        "service_request_id": "ISLANDTON-14CAP-00000-00070", 
        "status": "Received", 
        "updated_datetime": null
    }, 
    {
        "address": "", 
        "agency_responsible": null, 
        "description": null, 
        "media_url": "http://thisisface.com", 
        "requested_datetime": null, 
        "service_code": "ServiceRequest-Water.cand.cSewage-Leaking.cFire.cHydrant-NA", 
        "service_name": "Leaking Fire Hydrant", 
        "service_request_id": "ISLANDTON-14CAP-00000-00073", 
        "status": "Received", 
        "updated_datetime": null
    }
]
```

### Get a Specific Service Request

<code>http://[API endpoint]/requests/[service_request_id].[format]</code>

HTTP Method: GET

Parameters:

| Name  | Required  |
|:--|:-:|
| jurisdiction_id | Y  | 
| service_request_id | Y |

Sample Response:

```json
[
    {
        "address": "", 
        "agency_responsible": null, 
        "description": "This is the description.", 
        "media_url": "http://thisisface.com", 
        "requested_datetime": null, 
        "service_code": "ServiceRequest-Water.cand.cSewage-Leaking.cFire.cHydrant-NA", 
        "service_name": "Leaking Fire Hydrant", 
        "service_request_id": "ISLANDTON-14CAP-00000-00074", 
        "status": "Received", 
        "updated_datetime": "2014-07-02 18:23:44"
    }
]
```
### Create a New Service Request

<code>http://[API endpoint]/requests.[format]</code>

HTTP Method: POST

Parameters:

| Name  | Required | Details
|:--|:-:|:--|
| jurisdiction_id | Y | Thet jurisdiction the service request is being submitted to. | 
| api_key | Y | The API key. |
| service_name | Y | Name of the service request type. Value from **service_name** field in <code>/services</code> call.|
| service_code | Y | Value of **service_code** field in <code>/services</code> call. |
| lat | Y | Latitude of the location of the issue. |
| long | Y | Lingitude of the location of the issue. |
| description | N | Description of the issue being reported. |
| streetNumber | N | Street number of the location of the issue. |
| streetName | N | Street name of the location of the issue.|
| streetSuffix | N | Street suffix of the location of the issue.|
| city | N | City where the issue is observed. |
| state | N | State where where the issue is observed. |
| media_url | N | Fually qualified URL to media showing the details of an issue. |

Sample Request:

<pre>
curl -X POST "http://[API endpoint]/requests.json?jurisdiction_id=Islandton&api_key={your API key}
    &service_name=Garbage&service_code=ServiceRequest/Garbage/Trash%20Removal/NA
    &lat=39.050&long=-75.1667
    &description=This%20Is%20A%20Test%20Record
    &media_url=http://www.somedomain.com/image.jpg"

</pre>

Sample Response:

```json
[
    {
        "service_request_id": "ISLANDTON-14CAP-00000-00080"
    }
]
```

### Get Comments For a Service Request

<code>http://[API endpoint]/requests/comments/[service_request_id].[format]</code>

HTTP Method: GET

Parameters:

| Name  | Required  |
|:--|:-:|
| jurisdiction_id | Y  | 
| service_request_id | Y |

Sample Response:

```json
[
    {
        "comment": "This is a comment", 
        "jurisdiction_id": "Islandton", 
        "request_id": "ISLANDTON-14CAP-00000-0007V"
    }
]

```

### Add a Comment to a Service Request

<code>http://[API endpoint]/requests/comments/[service_request_id].[format]</code>

HTTP Method: POST

Parameters:

| Name  | Required  |
|:--|:-:|
| jurisdiction_id | Y  | 
| service_request_id | Y |
| api_key | Y |
| comment | Y |


Sample Response:

```json
{
    "success": true,
    "id": "e49093ee436011216bce26342400c192"
}
```

### Get an API Key

<code>http://[API endpoint]/apikey/new.[format]</code>

HTTP Method: PUT

Parameters:

| Name  | Required  |
|:--|:-:|
| jurisdiction_id | Y  | 
| email | Y |

Sample Response:

```json
{
    "key": "3e664199418013792fc157188c036dce"
}
```

### Get Service Request ID from Token

Method not implemented.


