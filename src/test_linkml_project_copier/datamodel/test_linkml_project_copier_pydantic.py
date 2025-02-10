from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'test_linkml_project_copier',
     'default_range': 'string',
     'description': 'Test instance of linkml-copier-template.',
     'id': 'https://w3id.org/dalito/test-linkml-project-copier',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'test-linkml-project-copier',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'test_linkml_project_copier': {'prefix_prefix': 'test_linkml_project_copier',
                                                 'prefix_reference': 'https://w3id.org/dalito/test-linkml-project-copier/'}},
     'see_also': ['https://dalito.github.io/test-linkml-project-copier'],
     'source_file': 'src/test_linkml_project_copier/schema/test_linkml_project_copier.yaml',
     'title': 'test-linkml-project-copier'} )

class PersonStatus(str, Enum):
    # the person is living
    ALIVE = "ALIVE"
    # the person is deceased
    DEAD = "DEAD"
    # the vital status is not known
    UNKNOWN = "UNKNOWN"



class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/dalito/test-linkml-project-copier'})

    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class Person(NamedThing):
    """
    Represents a Person
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/dalito/test-linkml-project-copier',
         'slot_usage': {'primary_email': {'name': 'primary_email',
                                          'pattern': '^\\S+@[\\S+\\.]+\\S+'}}})

    primary_email: Optional[str] = Field(default=None, description="""The main email address of a person""", json_schema_extra = { "linkml_meta": {'alias': 'primary_email', 'domain_of': ['Person'], 'slot_uri': 'schema:email'} })
    birth_date: Optional[date] = Field(default=None, description="""Date on which a person is born""", json_schema_extra = { "linkml_meta": {'alias': 'birth_date', 'domain_of': ['Person'], 'slot_uri': 'schema:birthDate'} })
    age_in_years: Optional[int] = Field(default=None, description="""Number of years since birth""", json_schema_extra = { "linkml_meta": {'alias': 'age_in_years', 'domain_of': ['Person']} })
    vital_status: Optional[PersonStatus] = Field(default=None, description="""living or dead status""", json_schema_extra = { "linkml_meta": {'alias': 'vital_status', 'domain_of': ['Person']} })
    id: str = Field(default=..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })

    @field_validator('primary_email')
    def pattern_primary_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid primary_email format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid primary_email format: {v}")
        return v


class PersonCollection(ConfiguredBaseModel):
    """
    A holder for Person objects
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/dalito/test-linkml-project-copier',
         'tree_root': True})

    entries: Optional[Dict[str, Person]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'entries', 'domain_of': ['PersonCollection']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Person.model_rebuild()
PersonCollection.model_rebuild()

