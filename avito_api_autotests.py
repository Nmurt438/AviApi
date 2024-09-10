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

