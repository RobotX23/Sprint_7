from helpers import *
import pytest
import allure
from data import *

class TestUser:

    @allure.title('Создание курьера')
    def test_сreation(self):
        returne = register()
        assert returne[3] == 201 and returne[4] == True


    @allure.title('Проверка создание дубликата курьера')
    def test_duplicate(self):
        register1 = register()
        login = register1[0]
        password = register1[1]
        first_name = register1[2]
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f"{url}/api/v1/courier", data=payload)
        assert (response.json()['message'] == log_used) and response.json()['code'] == 409

    @allure.title('Создание курьера без вводных данных')
    def test_no_pass_and_log_and_firstname(self):
        response = requests.post(f"{url}/api/v1/courier")
        assert response.json()['code'] == 400 and response.json()['message'] == not_enough

    @allure.title('Создание курьера без пароля')
    @pytest.mark.parametrize('login', [('jkdfslsddas12312dsdvn')])
    def test_no_password(self, login):
        payload = {
            "login": login,
        }

        response = requests.post(f"{url}/api/v1/courier", data=payload)
        assert response.json()['message'] == not_enough and response.json()['code'] == 400

    @allure.title('Создание курьера без логина')
    @pytest.mark.parametrize('password', [('jkdfslsddas12312dsdvn')])
    def test_no_login(self, password):
        payload = {
            "password": password,
        }

        response = requests.post(f"{url}/api/v1/courier", data=payload)
        print(response.json())
        assert response.json()['message'] == not_enough and response.json()['code'] == 400

