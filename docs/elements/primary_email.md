

# Slot: primary_email


_The main email address of a person_





URI: [schema:email](http://schema.org/email)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Represents a Person |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/dalito/test-linkml-project-copier




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:email |
| native | test_linkml_project_copier:primary_email |




## LinkML Source

<details>
```yaml
name: primary_email
description: The main email address of a person
from_schema: https://w3id.org/dalito/test-linkml-project-copier
rank: 1000
slot_uri: schema:email
alias: primary_email
domain_of:
- Person
range: string

```
</details>