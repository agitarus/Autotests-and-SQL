import requests
import configuration
import data


#Создание заказа и передача номера трека заказа в переменную response
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body, headers=data.headers)
response = post_new_order(data.create_order_body).json()['track']


#Получение информации о заказе по номеру трека
def get_order_from_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO+str(response)).status_code


#Сравнение кода ответа функции get_order_from_track() с кодом 200
def assert_200():
    order_status = get_order_from_track()
    assert order_status == 200
