from unittest.mock import patch

import earthkit.data as cml
import pytest

from earthkit_data_wekeo_source.wekeo import WekeoAPIKeyPrompt


def test_invalid_json():
    with pytest.raises(AssertionError):
        cml.from_source("wekeo-source", 0)


def test_incomplete_json():
    with pytest.raises(AssertionError):
        cml.from_source("wekeo-source", {})


@patch.object(WekeoAPIKeyPrompt, "check", return_value=None)
def test_valid_arguments(api_check):
    with patch("earthkit_data_wekeo_source.wekeo.Client"), patch(
        "earthkit_data_wekeo_source.wekeo.bytes_to_string"
    ), patch("earthkit_data_wekeo_source.wekeo.ask_yes_no", return_value=False):
        cml.from_source("wekeo-source", {"dataset_id": "dummy"})
        api_check.assert_called()
