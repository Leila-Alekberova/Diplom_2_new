import sys
sys.path.insert(0,"C:/Users/alekberovalf/Desktop/Diplom/Diplom_2_new/")
import allure
import pytest
import requests
from data.data import Urls, Handlers, Users, Message
from data.helpers import UserData
from conftest import create_and_delete_user

class TestChangeUser:

    @allure.title("Изменение имени авторизованного пользователя")
    @pytest.mark.parametrize(
        'update_data',
        [
            {"email": UserData.create_email()},
            {"password": UserData.create_password()},
            {"name": UserData.create_name()}
        ])
    def test_change_auth_user_name(self, update_data, create_and_delete_user):
        response = requests.patch(f'{Urls.MAIN_URL}{Handlers.EDIT_USER}', headers={'Authorization':create_and_delete_user[1]},
                                  data=update_data)
        assert response.status_code == 200
        assert response.json()['success'] is True


    @allure.title('Изменение пароля авторизованного пользователя')
    @pytest.mark.parametrize(
        'update_data',
        [
            {"email": UserData.create_email()},
            {"password": UserData.create_password()},
            {"name": UserData.create_name()}])
    def test_change_pass_with_auth(self,update_data, create_and_delete_user):

        response = requests.patch(f'{Urls.MAIN_URL}{Handlers.EDIT_USER}',
                                  headers={'Authorization': f'{create_and_delete_user[1]}'},
                                  data=update_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Неуспешное изменение данных пользователя без авторизации')
    @pytest.mark.parametrize(
        'update_data',
        [{"email": UserData.create_email()},
            {"password": UserData.create_password()},
            {"name": UserData.create_name()}])
    def test_change_user_without_auth(self, update_data, create_and_delete_user):
        response = requests.patch(f'{Urls.MAIN_URL}{Handlers.EDIT_USER}', data=update_data)
        assert response.status_code == 401
        assert Message.ERROR_UPDATE_WITHOUT_AUTHORISATION in response.text

