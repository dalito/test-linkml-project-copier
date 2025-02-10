

# Slot: id


_A unique identifier for a thing_





URI: [schema:identifier](http://schema.org/identifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Represents a Person |  no  |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/dalito/test-linkml-project-copier




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:identifier |
| native | test_linkml_project_copier:id |




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for a thing
from_schema: https://w3id.org/dalito/test-linkml-project-copier
rank: 1000
slot_uri: schema:identifier
identifier: true
alias: id
domain_of:
- NamedThing
range: uriorcurie
required: true

```
</details>