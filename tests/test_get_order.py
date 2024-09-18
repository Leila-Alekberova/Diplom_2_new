import allure
import pytest
import requests
from data.data import Urls, Handlers
from data.helpers import UserData, Ingredient, Message
from conftest import *

class TestGetOrder:

    @allure.title("Получение заказов для авторизованного пользователя")
    def test_get_order_auth_user(self, create_and_delete_user):
        requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}',
                                     headers={'Authorization': f'{create_and_delete_user[2]}'},
                                     data=Ingredient.correct_ingredients)
        response = requests.get(f'{Urls.MAIN_URL}{Handlers.GET_ORDERS}', headers={'Authorization': f'{create_and_delete_user[2]}'})
        assert response.status_code == 200
        assert "true" in response.text

    @allure.title("Получение заказов для неавторизованного пользователя")
    def test_get_order_without_auth_user(self):
        response = requests.get(f'{Urls.MAIN_URL}{Handlers.GET_ORDERS}')
        assert response.status_code == 401
        assert Message.ERROR_ORDER_WITHOUT_AUTHORISATION in response.text