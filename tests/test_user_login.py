import copy
import allure
import pytest
from helpers import RandomUserGeneration
from api import UserMethods
from data import responseText


class TestLoginUser:
    @allure.title('Успешный логин пользователя')
    def test_login_user_success(self, login_user):
        response = login_user[1]
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Нет возможности логина пользователя с неверным логином и паролем')
    def test_login_user_with_incorrect_login_and_password(self):
        data = RandomUserGeneration.generate_user_data()
        response = UserMethods.login_user(data)
        assert response.status_code == 401
        assert response.json()['message'] == responseText.INCORRECT_LOGIN_PASSWORD
