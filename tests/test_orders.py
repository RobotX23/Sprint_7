import pytest
import requests
import allure
from data import *


class TestOrders:
    @allure.title('Проверка возвращения списка заказов')
    def test_orders(self):
        response = requests.get(f"{url}/api/v1/orders")
        assert response.status_code == 200 and ('orders' in response.json())

