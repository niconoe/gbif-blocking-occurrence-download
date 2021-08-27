import os
import zipfile

import pytest
import requests
import vcr

from gbif_blocking_occurrences_download import download_occurrences


BASIC_PREDICATE = {
    "predicate": {
        "type": "equals",
        "key": "DATASET_KEY",
        "value": "8d860a04-f762-11e1-a439-00145eb45e9a",
    },
}


@vcr.use_cassette("vcr_cassettes/test_incorrect_credentials.yaml")
def test_incorrect_credentials():
    """An requests exception reports a 401 error if credentials are incorrect"""
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        download_occurrences(
            predicate=BASIC_PREDICATE,
            username="xxxx",
            password="yyyy",
            output_path="download.zip",
        )

    assert excinfo.value.response.status_code == 401


@vcr.use_cassette("vcr_cassettes/test_basic_use.yaml")
def test_basic_use(tmp_path):
    download_path = tmp_path / "download.zip"

    download_occurrences(
        predicate=BASIC_PREDICATE,
        username="niconoe2",
        password="temporary",
        output_path=download_path,
    )

    assert os.path.isfile(download_path)
    zipfile.ZipFile(download_path).testzip() is None
