import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1"

def test_get_item_by_id():
    item_id = "7a8fe969-2a57-468e-82c9-1982d22023c5"
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    
    assert response.status_code == 200

    json_data = response.json()  # Проверка, что ответ - это JSON
    assert isinstance(json_data, dict)
    assert "name" in json_data  # Проверьте наличие ключа 'name'
    assert "price" in json_data  # Дополнительная проверка на наличие ключа 'price'
    assert "sellerId" in json_data  # Дополнительная проверка на наличие ключа 'sellerId'


def test_get_all_items_by_seller():
    seller_id = "3452"
    response = requests.get(f"{BASE_URL}/{seller_id}/item")
    
    assert response.status_code == 200

    json_data = response.json()
    assert isinstance(json_data, list)  # Проверка, что ответ - это список
    if json_data:  # Проверка, что список не пустой
        assert isinstance(json_data[0], dict)  # Проверка, что первый элемент - словарь


def test_save_item():
    new_item = {
        "name": "Телефон",
        "price": 85566,
        "sellerId": 3452,
        "statistics": {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=new_item)
    
    assert response.status_code == 201

    json_data = response.json()
    assert "id" in json_data  # Проверка, что возвращается идентификатор нового элемента
    assert json_data["name"] == new_item["name"]  # Проверка на корректность созданного элемента


# pytest автоматически найдет и выполнит все функции, начинающиеся с test_.