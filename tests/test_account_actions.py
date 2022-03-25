import pytest
import allure
from testdata.testdata import UserAccounts
from utils.print_helper import print_json
from utils.assertions import assert_code, assert_msg


@allure.feature('Тесты верификации аккаунта')
class TestVerifyLogin:
    PATH = 'verifyLogin'

    @pytest.mark.positive
    @allure.story('Тест: верификация аккаунта')
    def test_post_to_verify_login(self, api):
        response_json = api.post(self.PATH, data={'email': UserAccounts.user1['email'],
                                                  'password': UserAccounts.user1['password']}).json()

        assert_code(response_json, 200)
        assert_msg(response_json, 'User exists!')

    @pytest.mark.negative
    @allure.story('Тест: верификация аккаунта без ввода email')
    def test_post_to_verify_login_without_email(self, api):
        response_json = api.post(self.PATH, data={'password': UserAccounts.user1['password']}).json()

        assert_code(response_json, 400)
        assert_msg(response_json, 'Bad request, email or password parameter is missing in POST request.')

    @pytest.mark.negative
    @allure.story('Тест: верификация аккаунта с недействительнми данными')
    def test_post_to_verify_login_with_invalid_details(self, api):
        response_json = api.post(self.PATH, data={'email': UserAccounts.user1['email'],
                                                  'password': 'asd'}).json()

        assert_code(response_json, 404)
        assert_msg(response_json, 'User not found!')

    @pytest.mark.negative
    @allure.story('Тест: отправка метода DELETE при верификации аккаунта')
    def test_delete_to_verify_login(self, api):
        response_json = api.delete(self.PATH, data={'email': UserAccounts.user1['email'],
                                                    'password': UserAccounts.user1['password']}).json()

        assert_code(response_json, 405)
        assert_msg(response_json, "This request method is not supported.")


@allure.feature('Тесты действий с аккаунтом')
class TestAccountCRUD:

    @pytest.mark.run(order=1)
    @pytest.mark.positive
    @allure.story('Тест: создание аккаунта')
    def test_post_to_create_account(self, api):
        response_json = api.post('createAccount', data=UserAccounts.user1).json()

        assert_code(response_json, 201)
        assert_msg(response_json, 'User created!')

    @pytest.mark.run(order=2)
    @pytest.mark.positive
    @allure.story('Тест: получение подробностей аккаунта по email')
    def test_get_account_detail_by_email(self, api):
        response_json = api.get('getUserDetailByEmail', params={'email': UserAccounts.user1['email']}).json()
        print_json(response_json)

        assert_code(response_json, 200)

    @pytest.mark.run(order=3)
    @pytest.mark.negative
    @allure.story('Тест: получение подробностей аккаунта по несуществующему email')
    def test_get_account_detail_by_invalid_email(self, api):
        response_json = api.get('getUserDetailByEmail', params={'email': 'asdasd@hamil.com'}).json()
        print_json(response_json)

        assert_code(response_json, 404)
        assert_msg(response_json, "Account not found with this email, try another email!")

    @pytest.mark.run(order=-2)
    @pytest.mark.positive
    @allure.story('Тест: изменение данных аккаунта')
    def test_put_to_update_account(self, api):
        response_json = api.put('updateAccount', data=UserAccounts.user2).json()

        assert_code(response_json, 200)
        assert_msg(response_json, 'User updated!')

    @pytest.mark.run(order=-1)
    @pytest.mark.positive
    @allure.story('Тест: удаление аккаунта')
    def test_delete_account(self, api):
        response_json = api.delete('deleteAccount', data={'email': UserAccounts.user1['email'],
                                                          'password': UserAccounts.user1['password']}).json()

        assert_code(response_json, 200)
        assert_msg(response_json, 'Account deleted!')
