<a href="https://github.com/copier-org/copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# test-linkml-project-copier

Test instance of linkml-copier-template.

## Website

[https://dalito.github.io/test-linkml-project-copier](https://dalito.github.io/test-linkml-project-copier)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [test_linkml_project_copier](src/test_linkml_project_copier)
    * [schema](src/test_linkml_project_copier/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/test_linkml_project_copier/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

The pre-defined commands are written for the command runner [just](https://github.com/casey/just/).
Use the `just` commands to generate project artefacts:
* `just` or `just --list`: list all pre-defined tasks
* `just site`: (re-)create everything
* `just deploy`: deploys site

## Credits

This project was created from the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier).
