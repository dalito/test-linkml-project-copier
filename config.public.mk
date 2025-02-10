# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="test_linkml_project_copier"
LINKML_SCHEMA_AUTHOR="David Linke <david.linke@catalysis.de>"
LINKML_SCHEMA_DESCRIPTION="Test instance of linkml-copier-template."
LINKML_SCHEMA_SOURCE_PATH="src/test_linkml_project_copier/schema/test_linkml_project_copier.yaml"
LINKML_SCHEMA_GOOGLE_SHEET_MODULE=" personinfo_enums"
LINKML_SCHEMA_GOOGLE_SHEET_ID=""
LINKML_SCHEMA_GOOGLE_SHEET_TABS="personinfo enums"
LINKML_USE_SCHEMASHEETS=No

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile rdfs)
LINKML_GENERATORS_OWL_ARGS=

## pass args to trigger experimental java/typescript generation
LINKML_GENERATORS_JAVA_ARGS=
LINKML_GENERATORS_TYPESCRIPT_ARGS=

## pass args to pydantic generator which isn't supported by gen-project
## https://github.com/linkml/linkml/issues/2537
LINKML_GENERATORS_PYDANTIC_ARGS=
