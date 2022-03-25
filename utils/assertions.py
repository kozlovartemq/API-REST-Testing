import allure


@allure.step('Проверка: код ответа совпадает с ожидаемым.')
def assert_code(response_json: dict, expected_code: int):
    assert response_json['responseCode'] == expected_code, f'Wrong response code. ({response_json["responseCode"]})'


@allure.step('Проверка: сообщение ответа совпадает с ожидаемым.')
def assert_msg(response_json: dict, expected_msg: str):
    assert response_json['message'] == expected_msg, f'Wrong response message. ({response_json["message"]})'


@allure.step('Проверка: Искомый продукт найден.')
def assert_product_found(response_json: dict):
    assert response_json['products'] != [], 'The searching product did not found.'
