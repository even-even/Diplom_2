import allure

from data import responseText
from api import OrderMethods


class TestGetUsersOrderList:
    @allure.title('Получение списка заказов авторизованным пользователем')
    def test_get_users_order_list_with_auth_success(self, login_user, token):
        token = login_user[2]
        order_list_response = OrderMethods.get_users_order_list(user_token=token)
        assert order_list_response.status_code == 200
        assert order_list_response.json()['success'] is True

    @allure.title('Нет возможности получить список заказов, если пользователь не авторизован')
    def test_get_users_order_list_with_not_auth(self):
        order_list_response = OrderMethods.get_users_order_list(user_token='')
        assert order_list_response.status_code == 401
        assert order_list_response.json()['message'] == responseText.SHOULD_AUTHORIZATION
