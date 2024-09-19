import allure
import pytest
import requests
from data.data import Urls, Handlers, Users, Message, Ingredient
from data.helpers import UserData
from conftest import *

class TestCreateOrder:

    @allure.title("Создание заказа для авторизованного пользователя с ингредиентами")
    def test_create_order_auth_user(self, create_and_delete_user):
        response, payload, token = create_and_delete_user
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}', headers={'Authorization': f'{token}'},
                                 data=Ingredient.correct_ingredients)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа для неавторизованного пользователя с ингредиентами")
    def test_create_order_no_auth_user(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}',
                                 data=Ingredient.correct_ingredients)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа c некорректными ингредиентами неавторизованным пользователем")
    def test_create_order_without_ingredient(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}',
                                 data=Ingredient.incorrect_ingredients)
        assert response.status_code == 500
        assert Message.ERROR_INCORRECT_INGREDIENT in response.text

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_with_incorrect_hash(self):
        response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_ORDER}')
        assert response.status_code == 400
        assert Message.ERROR_WITHOUT_INGREDIENTS in response.text
