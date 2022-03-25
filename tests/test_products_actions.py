import pytest
import allure
from testdata.testdata import Items
from utils.print_helper import print_json
from utils.assertions import assert_code, assert_msg, assert_product_found


@allure.feature('Тесты списка продуктов')
class TestProductsList:
    PATH = 'productsList'

    @pytest.mark.positive
    @allure.story('Тест: получение полного списка продуктов')
    def test_get_all_products_list(self, api):
        response_json = api.get(self.PATH).json()
        print_json(response_json)

        assert_code(response_json, 200)

    @pytest.mark.negative
    @allure.story('Тест: отправка метода POST к списку продуктов')
    def test_post_to_all_products_list(self, api):
        response_json = api.post(self.PATH, data=Items.item1).json()

        assert_code(response_json, 405)
        assert_msg(response_json, "This request method is not supported.")


@allure.feature('Тесты списка брендов')
class TestBrandsList:
    PATH = 'brandsList'

    @pytest.mark.positive
    @allure.story('Тест: получение полного списка брендов')
    def test_get_all_brands_list(self, api):
        response_json = api.get(self.PATH).json()
        print_json(response_json)

        assert_code(response_json, 200)

    @pytest.mark.negative
    @allure.story('Тест: изменение полного списка брендов')
    def test_put_to_all_brands_list(self, api):
        response_json = api.put(self.PATH).json()

        assert_code(response_json, 405)
        assert_msg(response_json, "This request method is not supported.")


@allure.feature('Тесты поиска продуктов')
class TestSearchProducts:
    PATH = 'searchProduct'

    @allure.story('Тест: поиск продуктов')
    @pytest.mark.parametrize('product', [pytest.param('Fancy Green Top', marks=pytest.mark.positive),
                                         pytest.param('adasd', marks=(pytest.mark.xfail(reason='Searching for nonexistent item'), pytest.mark.negative))],
                             ids=['valid_data', 'invalid_data'])
    def test_post_to_search_product(self, api, product):
        response_json = api.post(self.PATH, data={'search_product': product}).json()
        print_json(response_json)

        assert_code(response_json, 200)
        assert_product_found(response_json)

    @pytest.mark.negative
    @allure.story('Тест: поиск продуктов без параметра search_product')
    def test_post_to_search_product_without_data(self, api):
        response_json = api.post(self.PATH).json()

        assert_code(response_json, 400)
        assert_msg(response_json, 'Bad request, search_product parameter is missing in POST request.')
