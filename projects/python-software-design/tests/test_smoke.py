"""Smoke tests for python_software_design."""

import python_software_design


def test_version_is_exposed() -> None:
    assert python_software_design.__version__ == "0.1.0"
