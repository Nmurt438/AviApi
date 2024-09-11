Тест-кейсы
Предусловия: Необходим инструмент для получения запросов. При написании тест-кейсов, использовался Postman. 

1.Тест-кейс 1: Получить объявление по ID
   - Цель:Убедиться, что API возвращает правильное объявление по заданному ID.
   - Метод:GET
   - URL:`https://qa-internship.avito.com/api/1/item/:id`
   - Параметры:
     - :id = `7a8fe969-2a57-468e-82c9-1982d22023c5`
   - Ожидаемый результат: HTTP статус 200 и корректные данные объявления.

2. Тест-кейс 2: Получить все объявления по продавцу**
   - Цель: Убедиться, что API возвращает все объявления для заданного продавца.
   - Метод: GET
   - URL: `https://qa-internship.avito.com/api/1/:sellerID/item`
   - Параметры: 
     -sellerID = `3452`
   -Ожидаемый результат: HTTP статус 200 и список объявлений для данного продавца.

3. Тест-кейс 3: Сохранить объявление**
   - Цель: Проверить, что API позволяет сохранить новое объявление.
   - Метод: POST
   - **URL:`https://qa-internship.avito.com/api/1/item`
   - Тело запроса:
     json
     {
       "name": "Телефон",
       "price": 85566,
       "sellerId": 3452,
       "statistics": {
           "contacts": 32,
           "like": 35,
           "viewCount": 14
       }
     }
     
   - Ожидаемый результат: HTTP статус 200 OK  и успешное сохранение объявления.

Далее приведены автматизированные тесты, которые проверяют, успешно ли пройдены тест-кейсы. 
В результате прохождения тест-кейсов баги не были найдены. 

import requests
import unittest

class TestAvitoAPI(unittest.TestCase):
    
    BASE_URL = "https://qa-internship.avito.com/api/1"
    
    def test_get_item_by_id(self):
        item_id = "7a8fe969-2a57-468e-82c9-1982d22023c5"
        response = requests.get(f"{self.BASE_URL}/item/{item_id}")
        self.assertEqual(response.status_code, 200)
        #Дополнительные проверки на содержание данных
        
 
    def test_get_all_items_by_seller(self):
        seller_id = "3452"
        response = requests.get(f"{self.BASE_URL}/{seller_id}/item")
        self.assertEqual(response.status_code, 200)
        # Дополнительные проверки на содержание данных
        self.assertIsInstance(response.json(), list)

    def test_save_item(self):
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
        response = requests.post(f"{self.BASE_URL}/item", json=new_item)
        self.assertEqual(response.status_code, 200)
        # Дополнительные проверки на сохраненные данные

if __name__ == "__main__":
    unittest.main()

