import pytest
import requests
import allure


class TestOrders:
    @allure.title('Проверка возвращения списка заказов')
    def test_orders(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        print (response.json())
        assert response.status_code == 200 and ('orders' in response.json())

