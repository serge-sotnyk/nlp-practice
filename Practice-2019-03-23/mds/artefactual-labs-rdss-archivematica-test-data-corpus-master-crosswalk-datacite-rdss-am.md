
# Metadata Crosswalk - RDSS MVP

| [Datacite 4.0](https://schema.datacite.org/meta/kernel-4.0/doc/DataCite-MetadataKernel_v4.0.pdf)  | [JISC-RDSS-CDM](https://github.com/JiscRDSS/rdss-canonical-data-model/blob/master/Data-Model/Diagrams/alpha-model/logical-model.png) [v.19-06-2017](https://github.com/JiscRDSS/rdss-canonical-data-model/commit/263dfd40d007e7884bdade56ecde83e6d1bd335d) | [Archivematica 1.6](https://www.archivematica.org/en/docs/archivematica-1.6/user-manual/transfer/import-metadata/#import-metadata)
| ------------- | ------------- | ------------- |
| datacite:identifier | jisc:objectIdentifierValue  | archivematica:dc.identifier |
| datacite:identifierType   | jisc:objectIdentifierType | *defaults to DOI* |
| datacite:creator | *inherits from subproperty*  |  *inherits from subproperty* |
| datacite:creatorName   | jisc:objectContributor.PersonRole.Person.personGivenName <br />(*where ObjectContributor.PersonRole.person = "creator"*) | archivematica:dc.contributor |
| datacite:title | objectTitle | archivematica:dc.title |
| datacite:publisher | jisc:objectPublisher.OrganisationRole.Organisation.organisationName <br />(*where ObjectPublisher.OrganisationRole.organisation = "publisher"*) | archivematica:dc.publisher |
| datacite:publicationYear   | ObjectDate.dateValue <br />(*where dateType ="published"*) | archivematica:dcterms.issued |
| datacite:resourceTypeGeneral | jisc:objectResourceType | archivematica:dc.type |
| datacite:resourceType | *see JISC Resource Type profiles* | *as per JISC Resource Type profiles* |

**NOTE**: *Archivematica Dublin Core properties are mapped to* `premis:intellectualEntity` *in the Archivematica AIP.*

**NOTE**: *original metadata serializations and formats are stored with normalised metadata in Archivematica's archival information packages (AIPs).*

