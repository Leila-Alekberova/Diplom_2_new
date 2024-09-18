import allure
import pytest
import requests
from data.data import Urls, Handlers
from data.helpers import UserData


class TestCreateUser:
    @allure.title("Создание нового пользователя")
    def test_create_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=UserData.create_fake_user())
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title("Создание дублирующего пользователя")
    def test_create_double_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=UserData.double_user)
        assert response.status_code == 403
        assert "User already exists" in response.text

    @allure.title("Создание пользователя без обязательных полей")
    @pytest.mark.parametrize("user_data", [UserData.user_without_email, UserData.user_without_password, UserData.user_without_name])

    def test_create_without_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403
        assert "Email, password and name are required fields" in response.text