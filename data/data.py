class Urls:
    MAIN_URL = "https://stellarburgers.nomoreparties.site"

class Handlers:
    CREATE_USER = "/api/auth/register"
    LOGIN_USER = "/api/auth/login"
    LOGOUT_USER = "/api/auth/logout"
    DELETE_USER = '/api/auth/user'
    EDIT_USER = "/api/auth/user"

    UPDATE_TOKEN = "/api/auth/token"

    CREATE_ORDER = "/api/orders"
    GET_ORDERS = "/api/orders"

    GET_INGREDIENTS = "/api/ingredients"

    headers = {"Content-Type": "application/json"}

class Users:
    correct_user = {
        "email":"Alekberova_leila@yandex.ru",
        "password": "Alekberova_leila_password"}

    incorrect_email = {
        "email":"I!",
        "password": "Alekberova_leila_password"}

    incorrect_password = {
       "email":"Alekberova_leila@yandex.ru",
        "password": "1!"}

    double_user =  {
        "email":"Alekberova_leila@yandex.ru",
        "password": "Alekberova_leila_password",
        "name": "alekberova_leila"}

    user_without_email= {
        "email":"",
        "password": "Alekberova_leila_password",
        "name": "Alekberova_leila"}

    user_without_password = {
        "email": "Alekberova_leila@yandex.ru",
        "password": "",
        "name": "Alekberova_leila"}

    user_without_name = {
        "email": "Alekberova_leila@yandex.ru",
        "password": "Alekberova_leila_password",
        "name": ""}


class Ingredient:
    correct_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6c"]}

    incorrect_ingredients = {
        "ingredients": ["61c0c51", "61c0c5a2"]}

class Message:
    ERROR_UPDATE_WITHOUT_AUTHORISATION = "You should be authorised"
    ERROR_INCORRECT_INGREDIENT = "Internal Server Error"
    ERROR_WITHOUT_INGREDIENTS = "Ingredient ids must be provided"
    ERROR_ORDER_WITHOUT_AUTHORISATION = "You should be authorised"
    ERROR_DOUBLE_USER = "User already exists"
    ERROR_USER_WITHOUT_DATA = "Email, password and name are required fields"
