import allure
import pytest
from faker import Faker
from api import UserMethods
from data import responseText


class TestUpdateUser:
    fake = Faker(locale="ru_RU")

    @allure.title('Изменение данных пользователя (пользователь авторизован)')
    @pytest.mark.parametrize('update_data', [({'email': fake.email()}),
                                             ({'password': fake.password()}),
                                             ({'name': fake.name()})])
    def test_update_user_with_login_success(self, login_user, update_data, token):
        token = login_user[2]
        update_user = UserMethods.update_user(token, update_data)
        assert update_user.status_code == 200
        assert update_user.json()['success'] is True

    @allure.title('Изменение данных пользователя (пользователь не авторизован)')
    @pytest.mark.parametrize('update_data', [({'email': fake.email()}),
                                             ({'password': fake.password()}),
                                             ({'name': fake.name()})])
    def test_update_user_with_login_success(self, update_data):
        update_user = UserMethods.update_user(user_token='', payload=update_data)
        assert update_user.status_code == 401
        assert update_user.json()["message"] == responseText.SHOULD_AUTHORIZATION
