import allure
import requests
from urls import Urls


class UserMethods:
    @staticmethod
    @allure.step('Создание нового пользователя в системе')
    def create_user(payload):
        response = requests.post(f"{Urls.URL_MAIN}{Urls.URL_CREATE_USER}",
                                 data=payload,
                                 timeout=60)
        return response

    @staticmethod
    @allure.step('Логин пользователя в системе')
    def login_user(payload):
        response = requests.post(f"{Urls.URL_MAIN}{Urls.URL_LOGIN_USER}",
                                 data=payload,
                                 timeout=60)
        return response

    @staticmethod
    @allure.step('Обновление данных о пользователе')
    def update_user(user_token, payload):
        headers = {'Authorization': user_token}
        response = requests.patch(f"{Urls.URL_MAIN}{Urls.URL_UPDATE_USER}",
                                  headers=headers,
                                  data=payload,
                                  timeout=60)
        return response

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(user_token):
        headers = {'Authorization': user_token}
        response = requests.delete(f"{Urls.URL_MAIN}{Urls.URL_DELETE_USER}",
                                   headers=headers,
                                   timeout=60)
        return response


class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(user_token, ids):
        headers = {'Authorization': user_token}
        payload = {'ingredients': ids}
        response = requests.post(f"{Urls.URL_MAIN}{Urls.URL_CREATE_ORDER}",
                                 headers=headers,
                                 json=payload,
                                 timeout=60)
        return response

    @staticmethod
    @allure.step('Получение списка ингредиентов')
    def get_ingredients():
        response = requests.get(f"{Urls.URL_MAIN}{Urls.URL_GET_INGREDIENTS}",
                                timeout=60)
        ingredients = []
        for i in response.json()['data']:
            ingredients.append(i['_id'])
            return ingredients

    @staticmethod
    @allure.step('Получение списка заказов пользователя')
    def get_users_order_list(user_token):
        headers = {'Authorization': user_token}
        response = requests.get(f"{Urls.URL_MAIN}{Urls.URL_GET_USER_ORDERS}",
                                headers=headers,
                                timeout=60)
        return response
