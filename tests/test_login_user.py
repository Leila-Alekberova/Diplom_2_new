import allure
import pytest
import requests
from data.data import Urls, Handlers
from data.helpers import UserData

class TestLoginUser:

    @allure.title("Успешная авторизация существующего пользователя")
    def test_login_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN_USER}', data=UserData.correct_user)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title("Авторизация пользователя с некорректным логином")
    def test_login_user_incorrect(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN_USER}', data=UserData.incorrect_email)
        assert response.status_code == 401
        assert response.json()['success'] is False

    @allure.title("Авторизация пользователя с некорректным паролем")
    def test_login_user_incorrect(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN_USER}', data=UserData.incorrect_password)
        assert response.status_code == 401
        assert response.json()['success'] is False

    @allure.title("Авторизация пользователя с некорректным паролем")
    def test_login_user_incorrect(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN_USER}', data=UserData.incorrect_password)
        assert response.status_code == 401
        assert response.json()['success'] is False

