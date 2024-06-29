import pytest
import requests
import allure
import json
from data import *

class TestOrder:
    @allure.title('Создание заказа с цветом Black')
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [(dates['firstName'], dates['lastName'], dates['address'], dates['metroStation'], dates['phone'], dates['rentTime'], dates['deliveryDate'], dates['comment'], dates['color'][2])])
    def test_order_color_black(self,firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color ):
        payload = {
            "firstName": firstName,
    "lastName": lastName,
    "address": address,
    "metroStation": metroStation,
    "phone": phone,
    "rentTime": rentTime,
    "deliveryDate": deliveryDate,
    "comment": comment,
    "color": color
        }

        headers = {"Content-type": "application/json"}
        payload_1 = json.dumps(payload)
        response = requests.post(f"{url}/api/v1/orders", data=payload_1,
                                 headers=headers)
        assert response.status_code == 201 and ('track' in response.json())

    @allure.title('Создание заказа с цветом Grey')
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [(dates['firstName'], dates['lastName'], dates['address'], dates['metroStation'], dates['phone'], dates['rentTime'], dates['deliveryDate'], dates['comment'], dates['color'][3])])
    def test_order_color_grey(self,firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color ):
        payload = {
            "firstName": firstName,
    "lastName": lastName,
    "address": address,
    "metroStation": metroStation,
    "phone": phone,
    "rentTime": rentTime,
    "deliveryDate": deliveryDate,
    "comment": comment,
    "color": color

        }
        headers = {"Content-type": "application/json"}
        payload_1 = json.dumps(payload)
        response = requests.post(f"{url}/api/v1/orders", data=payload_1, headers=headers)
        assert response.status_code == 201 and ('track' in response.json())


    @allure.title('Создание заказа с двумя цветами')
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [(dates['firstName'], dates['lastName'], dates['address'], dates['metroStation'], dates['phone'], dates['rentTime'], dates['deliveryDate'], dates['comment'], dates['color'][4])])
    def test_order_color(self,firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color ):
        payload = {
            "firstName": firstName,
    "lastName": lastName,
    "address": address,
    "metroStation": metroStation,
    "phone": phone,
    "rentTime": rentTime,
    "deliveryDate": deliveryDate,
    "comment": comment,
    "color": color
        }

        response = requests.post(f"{url}/api/v1/orders", data=payload)
        assert response.status_code == 201 and ('track' in response.json())

    @allure.title('Создание заказа без цвета')
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [(dates['firstName'], dates['lastName'], dates['address'], dates['metroStation'], dates['phone'], dates['rentTime'], dates['deliveryDate'], dates['comment'], dates['color'][1])])
    def test_order_no_color(self,firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color ):
        payload = {
            "firstName": firstName,
    "lastName": lastName,
    "address": address,
    "metroStation": metroStation,
    "phone": phone,
    "rentTime": rentTime,
    "deliveryDate": deliveryDate,
    "comment": comment,
    "color":[]
        }

        response = requests.post(f"{url}/api/v1/orders", data=payload)
        assert response.status_code == 201 and ('track' in response.json())
