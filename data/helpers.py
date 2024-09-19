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

