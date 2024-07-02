import pytest
import requests
import allure
import json
from data import *

class TestOrder:
    @allure.title('Создание заказа с цветом Black')
    @pytest.mark.parametrize('payload', [payload_color_black])
    def test_order_color_black(self,payload):
        headers = {"Content-type": "application/json"}
        payload_1 = json.dumps(payload)
        response = requests.post(f"{url}{endpoint_orders}", data=payload_1,
                                 headers=headers)
        assert response.status_code == 201 and ('track' in response.json())

    @allure.title('Создание заказа с цветом Grey')
    @pytest.mark.parametrize('payload', [payload_color_grey])
    def test_order_color_grey(self,payload):
        headers = {"Content-type": "application/json"}
        payload_1 = json.dumps(payload)
        response = requests.post(f"{url}{endpoint_orders}", data=payload_1, headers=headers)
        assert response.status_code == 201 and ('track' in response.json())


    @allure.title('Создание заказа с двумя цветами')
    @pytest.mark.parametrize('payload', [payload_color])
    def test_order_color(self,payload):
        response = requests.post(f"{url}{endpoint_orders}", data=payload)
        assert response.status_code == 201 and ('track' in response.json())

    @allure.title('Создание заказа без цвета')
    @pytest.mark.parametrize('payload', [payload_no_color])
    def test_order_no_color(self,payload):
        response = requests.post(f"{url}{endpoint_orders}", data=payload)
        assert response.status_code == 201 and ('track' in response.json())
