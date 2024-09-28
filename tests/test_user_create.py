import allure
import pytest
from helpers import RandomUserGeneration
from api import UserMethods
from data import responseText


class TestCreateUser:
    @allure.title('Создание пользователя с корректными данными')
    def test_create_user(self, create_user, delete_user):
        response = create_user[1]
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Нет возможности создать пользователя, когда он уже зарегистрирован')
    def test_create_double_user_return_status_code_403(self, create_user):
        data = create_user[0]
        response = UserMethods.create_user(data)
        assert response.status_code == 403
        assert response.json()['message'] == responseText.USER_ALREADY_EXISTS

    @allure.title('Нет возможности создать пользователя, когда одно из полей незаполненно')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_create_user_with_empty_field_error(self, field):
        user_data = RandomUserGeneration.generate_user_data()
        payload = user_data
        payload.pop(field)
        response = UserMethods.create_user(payload)
        assert response.status_code == 403
        assert response.json()['message'] == responseText.REQUIRED_FIELDS
