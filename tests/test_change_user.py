import allure
import pytest
import requests
from data.data import Urls, Handlers, Users, Message
from data.helpers import UserData
from conftest import create_and_delete_user

class TestChangeUser:

    @allure.title("Изменение имени авторизованного пользователя")
    def test_change_auth_user_name(self, create_and_delete_user):
        token = create_and_delete_user[2]
        new_user_name = {"name": UserData.create_name()}
        response = requests.patch(f'{Urls.MAIN_URL}{Handlers.EDIT_USER}', headers={'Authorization': f'{token}'},
                                  data=new_user_name)
        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Изменение пароля авторизованного пользователя')
    def test_change_pass_with_auth(self, create_and_delete_user):
        token = create_and_delete_user[2]
        new_user_password = {"password": UserData.create_password()}
        response = requests.patch(f'{Urls.MAIN_URL}{Handlers.EDIT_USER}',
                                  headers={'Authorization': f'{token}'},
                                  data=new_user_password)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Неуспешное изменение данных пользователя без авторизации')
    @pytest.mark.parametrize(
        'update_data',
        [{"email": UserData.create_email()},
            {"password": UserData.create_password()},
            {"name": UserData.create_name()}])
    def test_change_user_without_auth(self, update_data):
        response = requests.patch(f'{Urls.MAIN_URL}{Handlers.EDIT_USER}', data=update_data)
        assert response.status_code == 401
        assert Message.ERROR_UPDATE_WITHOUT_AUTHORISATION in response.text

