# gbif-blocking-occurrence-download

[![Run unit tests on push](https://github.com/niconoe/gbif-blocking-occurrence-download/actions/workflows/run_tests.yml/badge.svg)](https://github.com/niconoe/gbif-blocking-occurrence-download/actions/workflows/run_tests.yml)
[![PyPI version](https://badge.fury.io/py/gbif-blocking-occurrence-download.svg)](https://badge.fury.io/py/gbif-blocking-occurrence-download)

A simple Python function to help downloading occurrences from GBIF.

The function is blocking while GBIF are preparing the download, so a 15-30 minute execution time is not abnormal.

## Install

```
$ pip install gbif-blocking-occurrence-download
```

## Example use

To trigger a download, you'll need:

- A [GBIF](https://www.gbif.org) account (username and password).
- A predicate to describe your query. See [the documentation](https://www.gbif.org/developer/occurrence#predicates) to
  help writing a predicate.

Example code:

```python
import logging
import sys

from gbif_blocking_occurrences_download import download_occurrences

# Increase the log level to INFO if you want to see progress during the (potentially long) function execution
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

username = 'your_gbif_username'
password = 'your_gbif_password'

# See https://www.gbif.org/developer/occurrence#predicates
predicate = {
    "predicate": {
        "type": "equals",
        "key": "DATASET_KEY",
        "value": "b7ee2a4d-8e10-410f-a951-a7f032678ffe"
    },
}

download_occurrences(
    predicate,
    username=username,
    password=password,
    output_path="download.zip",
)
```

## Development

- We're using Poetry to manage dependencies, publish to PyPI, ...
- Code formatted with Black:
```bash
$ black .
```
- We're using pytest for unit testing

### New release

- Update `CHANGELOG.md`
- Update version number in `pyproject.toml`
- Run `$ poetry build` and `$ poetry publish`
- Push a tag on GitHub:
```bash
$ git tag vX.Y.Z
$ git push origin --tags
```

