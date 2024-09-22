import pytest
import requests
import sys
sys.path.insert(0,"C:/Users/alekberovalf/Desktop/Diplom/Diplom_2_new/")

from data.data import Urls, Handlers
from data.helpers import UserData

@pytest.fixture(scope='function')
def create_and_delete_user():
    payload = UserData.create_fake_user()
    response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=payload)
    token = response.json()["accessToken"]
    yield payload, token
    requests.delete(f'{Urls.MAIN_URL}{Handlers.DELETE_USER}', headers={'Authorization':token})
    #помимо token я использую payload,response  убрала
