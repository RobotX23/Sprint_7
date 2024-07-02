from helpers import *
import pytest
import allure
from data import *

class TestLog:

    @allure.title('Логирование курьера')
    def test_log(self):
        returne = register()
        payload = {
            "login": returne[0],
            "password": returne[1],
        }
        response = requests.post(f"{url}{endpoint_login}", data=payload)
        assert  response.status_code == 200 and ('id' in response.json())



    @allure.title('Логирование без пароля')
    @allure.description('Ответ не соответствует ТЗ')
    @pytest.mark.parametrize('login', [('xlxkeygczg')])
    def test_log_no_password(self, login):
        payload = {
            "login": login,
        }

        response = requests.post(f"{url}{endpoint_login}", data=payload)
        assert response.status_code == 400 and response.json()['message'] == not_enough_entrance

    @allure.title('Логирование без лога')
    @pytest.mark.parametrize('password', [('ubofchhpbg')])
    def test_log_no_logs(self, password):
        payload = {
            "password": password,
        }

        response = requests.post(f"{url}{endpoint_login}", data=payload)
        assert response.status_code == 400 and response.json()['message'] == not_enough_entrance

    @allure.title('Логирование с некорректным паролем')
    @pytest.mark.parametrize('login, password', [('xlxkeygczg','0')])
    def test_log_fall_password(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }

        response = requests.post(f"{url}{endpoint_login}", data=payload)
        assert response.status_code == 404 and response.json()['message'] == not_uz

    @allure.title('Логирование с некорректным логином')
    @pytest.mark.parametrize('login, password', [('0', 'ubofchhpbg')])
    def test_log_fall_login(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }

        response = requests.post(f"{url}{endpoint_login}", data=payload)
        assert response.status_code == 404 and response.json()['message'] == not_uz