# pubmedr

MappCPD worker that fetches articles from [Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/) and inserts them into the primary MappCPD resources table.

![resources](https://docs.google.com/drawings/d/1zJ4pQCb94syzpCvoqRBXwbMUvs8LhpFlFE2Gax6LTfM/pub?w=691&h=431)

See [MappCPD Architecture](https://github.com/mappcpd/architecture/wiki) for more info.


## Configuration

**Note:** As the web services are deployed together, and there are overlapping env vars for each of the services, the environment can be configured globally. See [web services configuration](/web-services#configuration).  

**Env vars**

```bash
# Admin auth credentials
MAPPCPD_ADMIN_PASS="demo-user"
MAPPCPD_ADMIN_USER"demo-pass"

# API
MAPPCPD_API_URL="https://mappcpd-api.com"

# Pubmed return batch size - too big can time out
MAPPCPD_PUBMED_RETMAX=200

# Local or remote (http) JSON config file (see below)
BATCH_FILE="https://s3-ap-southeast-1.amazonaws.com/demo-mappcpd/public/pubmedr/pubmed.json"
```

The option for a remote batch config file was added so that the config did not have to be uploaded with the repo. It contains an array of one or more Pubmed fetch configurations, eg:

```json
[{
		"run": true,
		"category": "Cardiology",
		"searchTerm": "%28cardiology%5BMeSH%20Terms%5D%20OR%20cardiology%5BAll%20Fields%5D%29%20AND%20loattrfree%20full%20text%5BFilter%5D%20AND%20medline%5BFilter%5D%20AND%20jsubsetaim%5Btext%5D",
		"relDate": 1000,
		"attributes": {
			"category": "Cardiology",
			"free": true,
			"public": true,
			"source": "Pubmed"
		},
		"resourceTypeID": 80
	},
	{
		"run": true,
		"category": "Physiotherapy",
		"searchTerm": "%28physiotherapy%5BMeSH%20Terms%5D%20OR%20physiotherapy%5BAll%20Fields%5D%29%20AND%20loattrfree%20full%20text%5BFilter%5D%20AND%20medline%5BFilter%5D%20AND%20jsubsetaim%5Btext%5D",
		"relDate": 1000,
		"attributes": {
			"category": "Physiotherapy",
			"free": true,
			"public": true,
			"source": "Pubmed"
		},
		"resourceTypeID": 80
	}
]
```

Fields in the config:

`run` : `true/false` - switch on or off

`category` : Descriptive, does nothing yet

`searchTerm` : the url encoded search term, test [here](https://www.ncbi.nlm.nih.gov/pubmed/advanced)

`relDate` : include articles published up to this many days back

`attributes` : a json string used for faceting, optional however `category` should be included for multi-category resource libraries

`resourceTypeID` : id of the resource type from primary database `ol_resource_type` table, used to provide facet search for *video*, *audio*, *document* etc.


## Pubmed Notes

The Pubmed query that fetches the article abstract (efetch) supports XML and *not* JSON. Go can access nested XML 
fields nicely so this works well.

Here's an example:
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17284678&retmode=xml&rettype=abstract

Pubmed search terms are complex. There is a lot of [documentation](https://www.ncbi.nlm.nih.gov/books/NBK25499/) and searches 
 can be tested [here](https://www.ncbi.nlm.nih.gov/pubmed/advanced).

Here is an example:
```
(((((((Cardiology) OR Cardiology[MeSH Terms]) AND Heart) OR Heart[MeSH Terms]))) AND "freetext"[Filter] AND jsubsetaim[text]) 
```

This first bit looks for articles related to "Cardiology" or "Heart"
```
(((((((Cardiology) OR Cardiology[MeSH Terms]) AND Heart) OR Heart[MeSH Terms])))
```

This bit filters results that include links to full text articles, free of charge. 
Although many listed as free are often not - yes I'm looking at you, Elsevier.
```
AND "freetext"[Filter]
```

... and the last section include articles from "Core Clinical" journals, or the [Abridged Index Medicus](https://www.nlm.nih.gov/bsd/aim.html).
 This filters also accommodates [Index Medicus](https://en.wikipedia.org/wiki/Index_Medicus) using the term `jsubsetim`  
```
AND jsubsetaim[text])
```

The other filter we need to apply is on `<MedlineCitation Status="Value">` node. Details on the `Summary` attribute 
can be found [here](https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html). 
  
From this information it seems as though we should include articles with the Status values of _MEDLINE_, 
_PubMed-not-Medline_, and _OLDMEDLINE_.    


(
    (Cardiology OR Heart)
    AND "freetext"[Filter] 
    AND "medline"[filter]
    AND jsubsetaim[text]  
    AND 
    (
    "random allocation"[MeSH Terms]
    OR
    "therapeutic use"[Subheading]
    )
)

Yields 18,000+

(
    (Cardiology OR Heart)
    AND "freetext"[Filter] 
    AND "medline"[filter]
    AND jsubsetaim[text]  
)

Yields 64,000+

(excluding time filters)

The above can be pasted directly into the search box here:

https://www.ncbi.nlm.nih.gov/pubmed/?term=((Cardiology+OR+Heart)+AND+%22freetext%22[Filter]+AND+%22medline%22[filter]+AND+jsubsetaim[text])

### Search Term Breakdown

This searches all text as well as mesh terms:
```
(Cardiology OR Heart)
```
 The above is translated as:
```
(("cardiology"[MeSH Terms] OR "cardiology"[All Fields]) OR ("heart"[MeSH Terms] OR "heart"[All Fields]))
```


This filters citations with links to free, full-text articles
```
AND "freetext"[Filter]
``` 

This filters MEDLINE citations: 
```
AND "medline"[filter]
```
Thus, we end up filtering articles with Medline Citation status = "MEDLINE", ie:
```xml
<MedlineCitation Status="MEDLINE" Owner="NLM">
   ...
</MedlineCitation>
```
This has two implications. Firstly, "MEDLINE" status means the articles have passed through  
quality processes. Secondly, it changes the fields that are returned containing useful keywords.

Without this filter the useful keywords are either contained in either `<Keywords>` or `<MeshHeading>`. 
  The reason is that the MeshHeading descriptors are only created once the article is elevated to MEDLINE status. 
  Given that we are applying this filter, the keywords *should* always be contained in the 
  `<MeshHeading>` node. For example:
  
```xml
<MeshHeading>
  <DescriptorName UI="D013318" MajorTopicYN="Y">Stroke Volume</DescriptorName>
</MeshHeading>
```


Note... these might be useful as well... strongest evidence:
"random allocation"[MeSH Terms]
"therapeutic use"[Subheading]

NOT medline[sb]) AND english[la] AND (systematic[sb] OR ((clinical[tiab] AND trial[tiab]) OR clinical trial[pt] OR random*[tiab] OR random allocation[mh] OR therapeutic use[sh])) AND free full text[sb]

## References

General: 
https://www.ncbi.nlm.nih.gov/books/NBK25499/

MedlineCitation Status: 
https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html

Differet databases & restricting to Medline only:
https://www.nlm.nih.gov/pubs/factsheets/dif_med_pub.html
 
Abridged Index Medicus:
https://www.nlm.nih.gov/bsd/aim.html

Subject Filters[sb]: 
https://www.nlm.nih.gov/bsd/pubmed_subsets.html

CareSearch example:
https://www.caresearch.com.au/caresearch/tabid/1743/Default.aspx


