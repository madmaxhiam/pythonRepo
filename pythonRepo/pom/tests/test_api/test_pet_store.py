import requests
import pytest
from helpers.pet_store_helpers import json_create_or_update_a_pet

@pytest.mark.integration
def test_create_a_pet(base_url, headers):
    """Проверка получения списка пользователей."""
    payload = json_create_or_update_a_pet(1, 'cat', 'Catty')
    response = requests.post(f"{base_url}", json=payload,headers=headers,timeout=1000)
    data = response.json()
    assert response.status_code == 200, "Питомец не создан"
    assert data["id"] == 1, "ID питомца не совпадает"
    assert data["name"] == "Catty", "Имя питомца некорректно"
    assert data["category"]["name"] == "cat", "Порода питомца некорректна"

@pytest.mark.integration
def test_get_a_pet(base_url, headers, pet_added):
    """Проверка получения списка пользователей."""
    response = requests.get(f"{base_url}/2",headers=headers, timeout=1000)
    data = response.json()
    assert response.status_code == 200, "Питомец не найден"
    assert data["id"] == 2, "ID питомца не совпадает"
    assert data["name"] == "poppy", "Имя питомца некорректно"
    assert data["category"]["name"] == "dog", "Порода питомца некорректна"

@pytest.mark.integration
def test_update_a_pet(base_url, headers, pet_added ):
    """Проверка получения списка пользователей."""
    payload = json_create_or_update_a_pet(21, 'big_cat', 'Floppy')
    response = requests.put(f"{base_url}", json=payload,headers=headers, timeout=1000)
    data = response.json()
    assert response.status_code == 200, "Питомец не создан"
    assert data["id"] == 21, "ID питомца не совпадает"
    assert data["name"] == "Floppy", "Имя питомца некорректно"
    assert data["category"]["name"] == "big_cat", "Порода питомца некорректна"

@pytest.mark.integration
def test_delete_a_pet(base_url, headers, pet_added):
    """Проверка получения списка пользователей."""
    response_delete = requests.delete(f"{base_url}/1", headers=headers, timeout=1000)
    data_del = response_delete.json()
    assert response_delete.status_code == 200, "Питомец не удален"
    assert data_del["message"] == "1", "Сообщение не корректно"
