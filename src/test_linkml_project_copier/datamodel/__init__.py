from pathlib import Path
from .test_linkml_project_copier import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "test_linkml_project_copier.yaml"
