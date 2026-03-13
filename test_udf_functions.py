import inspect

import pytest

from some_module.udf_functions import (
    extract_material,
    extract_package_size,
    extract_package_size_ml,
)
from tests.utils.test_data_source import TEST_DATA


@pytest.fixture
def input_strings():
    return TEST_DATA[inspect.currentframe().f_code.co_name]


@pytest.mark.parametrize(
    'expected_materials',
    [
        TEST_DATA['expected_materials'],
    ],
)
def test_extract_material(input_strings, expected_materials):
    result = [extract_material(item) for item in input_strings]
    assert result == expected_materials


@pytest.mark.parametrize(
    'expected_packages_and_sizes',
    [
        TEST_DATA['expected_packages_and_sizes'],
    ],
)
def test_extract_package_size(input_strings, expected_packages_and_sizes):
    result = [extract_package_size(item) for item in input_strings]
    assert result == expected_packages_and_sizes


@pytest.mark.parametrize(
    'expected_sizes_ml',
    [
        TEST_DATA['expected_sizes_ml'],
    ],
)
def test_extract_package_size_ml(input_strings, expected_sizes_ml):
    result = [extract_package_size_ml(item) for item in input_strings]
    assert result == expected_sizes_ml