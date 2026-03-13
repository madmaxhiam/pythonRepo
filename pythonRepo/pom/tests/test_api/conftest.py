import pytest
import requests
from helpers.pet_store_helpers import json_create_or_update_a_pet

@pytest.fixture(scope="session")
def base_url():
    """URL API, который используется в тестах."""
    return "https://petstore.swagger.io/v2/pet"

@pytest.fixture(scope="function")
def headers():
    """Базовые заголовки для запросов."""
    return {"Content-Type": "application/json"}

@pytest.fixture(scope="function")
def pet_added( base_url, headers): # pylint: disable=W0621
    requests.post(f"{base_url}", json=json_create_or_update_a_pet(2,'dog','poppy'), headers=headers, timeout=1000)
