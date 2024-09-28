import allure
import pytest
from helpers import RandomUserGeneration
from api import UserMethods


@allure.step('Создать данные для пользователя')
@pytest.fixture(scope='function')
def create_user():
    data_payload = RandomUserGeneration.generate_user_data()
    response = UserMethods.create_user(data_payload)
    yield data_payload, response


@allure.step('Залогиниться под пользователем и получить токен')
@pytest.fixture(scope='function')
def token(create_user):
    data_payload = create_user[0]
    login = UserMethods.login_user(data_payload)
    token = login.json()['accessToken']
    return token, login


@allure.step('Создать пользователя и залогиниться')
@pytest.fixture(scope='function')
def login_user(create_user, token, delete_user):
    data_payload = create_user[0]
    login = token[1]
    user_token = token[0]
    yield data_payload, login, user_token


@allure.step('Пользователь удален после теста')
@pytest.fixture(scope='function')
def delete_user(token):
    yield
    UserMethods.delete_user(token[0])
