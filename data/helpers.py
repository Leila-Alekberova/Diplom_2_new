from faker import Faker

class UserData:
    @staticmethod
    def create_fake_user():
        fake = Faker()
        registration_fake_user ={
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return registration_fake_user

    @staticmethod
    def create_email():
        fake = Faker()
        registration_fake_email = {
            "email": fake.email()}
        return registration_fake_email

    @staticmethod
    def create_password():
        fake = Faker()
        registration_fake_password = {
            "password": fake.password()}
        return registration_fake_password

    @staticmethod
    def create_name():
        fake = Faker()
        registration_fake_name = {
            "password": fake.name()}
        return registration_fake_name



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