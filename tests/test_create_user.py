import allure
import pytest
import requests
from data.data import Urls, Handlers, Users, Message
from data.helpers import UserData


class TestCreateUser:
    @allure.title("Создание нового пользователя")
    def test_create_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=UserData.create_fake_user())
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title("Создание дублирующего пользователя")
    def test_create_double_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=Users.double_user)
        assert response.status_code == 403
        assert Message.ERROR_DOUBLE_USER in response.text

    @allure.title("Создание пользователя без обязательных полей")
    @pytest.mark.parametrize("user_data", [Users.user_without_email, Users.user_without_password, Users.user_without_name])

    def test_create_without_data(self, user_data):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403
        assert Message.ERROR_USER_WITHOUT_DATA in response.text