import allure
from data import responseText, other
from api import OrderMethods


class TestCreateOrder:

    @allure.title('Создание заказа c ингредиентами не авторизованным пользователем')
    def test_create_order_without_auth_with_ingredients_success(self):
        ingredients = OrderMethods.get_ingredients()
        order_response = OrderMethods.create_order(user_token='', ids=ingredients)
        assert order_response.status_code == 200
        assert order_response.json()['success'] is True

    @allure.title('Создание заказа c ингредиентами авторизованным пользователем')
    def test_create_order_with_auth_with_ingredients_success(self, login_user, token):
        ingredients = OrderMethods.get_ingredients()
        token = login_user[2]
        order_response = OrderMethods.create_order(user_token=token, ids=ingredients)
        assert order_response.status_code == 200
        assert order_response.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов авторизованным пользователем')
    def test_create_order_with_auth_without_ingredients_error(self, login_user, token):
        token = login_user[2]
        order_response = OrderMethods.create_order(user_token=token, ids='')
        assert order_response.status_code == 400
        assert order_response.json()['message'] == responseText.INGREDIENT_ID_MUST_PROVIDED

    @allure.title('Создание заказа без ингредиентов не авторизованным пользователем')
    def test_create_order_without_auth_without_ingredients_error(self):
        order_response = OrderMethods.create_order(user_token='', ids='')
        assert order_response.status_code == 400
        assert order_response.json()['message'] == responseText.INGREDIENT_ID_MUST_PROVIDED

    @allure.title('Создание заказа с некорректным хешем ингредиентов')
    def test_create_order_with_incorrect_hex_error_400(self):
        order_response = OrderMethods.create_order(user_token='', ids=other.INCORRECT_HASH)
        assert order_response.status_code == 500
