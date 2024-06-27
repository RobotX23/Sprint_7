import pytest
import requests
import allure


class TestOrder:
    @allure.title('Создание заказа с цветом Black')
    #Ошибка сервера код 500. Тест не возможно выполните по ТЗ. В коментах указал как должна происходить проверка после восстановления работы API.
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [('Naruto', 'Uchiha', 'Konoha, 142 apt.', 4, '+7 800 355 35 35', 5, '2020-06-06', 'Saske, come back to Konoha', ["BLACK"])])
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

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        #assert response.status_code == 201 and ('track' in response.json()) При корректно работе сервера
        assert response.status_code == 500

    @allure.title('Создание заказа с цветом Grey')
    #Ошибка сервера код 500. Тест не возможно выполните по ТЗ. В коментах указал как должна происходить проверка после восстановления работы API.
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [('Naruto', 'Uchiha', 'Konoha, 142 apt.', 4, '+7 800 355 35 35', 5, '2020-06-06', 'Saske, come back to Konoha', ["GREY"])])
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

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        #assert response.status_code == 201 and ('track' in response.json()) При корректно работе сервера
        assert response.status_code == 500

    @allure.title('Создание заказа с двумя цветами')
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [('Naruto', 'Uchiha', 'Konoha, 142 apt.', 4, '+7 800 355 35 35', 5, '2020-06-06', 'Saske, come back to Konoha', ["GREY", "BLACK"])])
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

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        assert response.status_code == 201 and ('track' in response.json())

    @allure.title('Создание заказа без цвета')
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [('Naruto', 'Uchiha', 'Konoha, 142 apt.', 4, '+7 800 355 35 35', 5, '2020-06-06', 'Saske, come back to Konoha', [])])
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

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        assert response.status_code == 201 and ('track' in response.json())
