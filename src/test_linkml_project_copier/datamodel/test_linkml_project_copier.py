# Auto generated from test_linkml_project_copier.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-06T22:54:55
# Schema: test-linkml-project-copier
#
# id: https://w3id.org/dalito/test-linkml-project-copier
# description: Test instance of linkml-copier-template.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Optional, Union

from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import (
    dataclasses_init_fn_with_kwargs,
)
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_dict
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace("PATO", "http://purl.obolibrary.org/obo/PATO_")
BIOLINK = CurieNamespace("biolink", "https://w3id.org/biolink/")
EXAMPLE = CurieNamespace("example", "https://example.org/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
TEST_LINKML_PROJECT_COPIER = CurieNamespace(
    "test_linkml_project_copier", "https://w3id.org/dalito/test-linkml-project-copier/"
)
DEFAULT_ = TEST_LINKML_PROJECT_COPIER


# Types


# Class references
class NamedThingId(URIorCURIE):
    pass


class PersonId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = TEST_LINKML_PROJECT_COPIER.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(NamedThing):
    """
    Represents a Person
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_LINKML_PROJECT_COPIER["Person"]
    class_class_curie: ClassVar[str] = "test_linkml_project_copier:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = TEST_LINKML_PROJECT_COPIER.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(
            self.vital_status, PersonStatus
        ):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonCollection(YAMLRoot):
    """
    A holder for Person objects
    """

    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_LINKML_PROJECT_COPIER["PersonCollection"]
    class_class_curie: ClassVar[str] = "test_linkml_project_copier:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = TEST_LINKML_PROJECT_COPIER.PersonCollection

    entries: Optional[
        Union[
            Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]
        ]
    ] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(
            slot_name="entries", slot_type=Person, key_name="id", keyed=True
        )

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):
    ALIVE = PermissibleValue(
        text="ALIVE", description="the person is living", meaning=PATO["0001421"]
    )
    DEAD = PermissibleValue(
        text="DEAD", description="the person is deceased", meaning=PATO["0001422"]
    )
    UNKNOWN = PermissibleValue(
        text="UNKNOWN", description="the vital status is not known"
    )

    _defn = EnumDefinition(
        name="PersonStatus",
    )


# Slots
class slots:
    pass


slots.id = Slot(
    uri=SCHEMA.identifier,
    name="id",
    curie=SCHEMA.curie("identifier"),
    model_uri=TEST_LINKML_PROJECT_COPIER.id,
    domain=None,
    range=URIRef,
)

slots.name = Slot(
    uri=SCHEMA.name,
    name="name",
    curie=SCHEMA.curie("name"),
    model_uri=TEST_LINKML_PROJECT_COPIER.name,
    domain=None,
    range=Optional[str],
)

slots.description = Slot(
    uri=SCHEMA.description,
    name="description",
    curie=SCHEMA.curie("description"),
    model_uri=TEST_LINKML_PROJECT_COPIER.description,
    domain=None,
    range=Optional[str],
)

slots.primary_email = Slot(
    uri=SCHEMA.email,
    name="primary_email",
    curie=SCHEMA.curie("email"),
    model_uri=TEST_LINKML_PROJECT_COPIER.primary_email,
    domain=None,
    range=Optional[str],
)

slots.birth_date = Slot(
    uri=SCHEMA.birthDate,
    name="birth_date",
    curie=SCHEMA.curie("birthDate"),
    model_uri=TEST_LINKML_PROJECT_COPIER.birth_date,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.age_in_years = Slot(
    uri=TEST_LINKML_PROJECT_COPIER.age_in_years,
    name="age_in_years",
    curie=TEST_LINKML_PROJECT_COPIER.curie("age_in_years"),
    model_uri=TEST_LINKML_PROJECT_COPIER.age_in_years,
    domain=None,
    range=Optional[int],
)

slots.vital_status = Slot(
    uri=TEST_LINKML_PROJECT_COPIER.vital_status,
    name="vital_status",
    curie=TEST_LINKML_PROJECT_COPIER.curie("vital_status"),
    model_uri=TEST_LINKML_PROJECT_COPIER.vital_status,
    domain=None,
    range=Optional[Union[str, "PersonStatus"]],
)

slots.personCollection__entries = Slot(
    uri=TEST_LINKML_PROJECT_COPIER.entries,
    name="personCollection__entries",
    curie=TEST_LINKML_PROJECT_COPIER.curie("entries"),
    model_uri=TEST_LINKML_PROJECT_COPIER.personCollection__entries,
    domain=None,
    range=Optional[
        Union[
            Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]
        ]
    ],
)

slots.Person_primary_email = Slot(
    uri=SCHEMA.email,
    name="Person_primary_email",
    curie=SCHEMA.curie("email"),
    model_uri=TEST_LINKML_PROJECT_COPIER.Person_primary_email,
    domain=Person,
    range=Optional[str],
    pattern=re.compile(r"^\S+@[\S+\.]+\S+"),
)
