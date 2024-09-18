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

