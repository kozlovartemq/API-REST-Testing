import requests
import allure


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path, params=None, headers=None):
        url = f'{self.base_address}{path}'
        with allure.step(f'GET request to: {url}'):
            return requests.get(url=url, params=params, headers=headers)

    def post(self, path, params=None, data=None, json=None, headers=None):
        url = f'{self.base_address}{path}'
        with allure.step(f'POST request to: {url}'):
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    def put(self, path, params=None, data=None, headers=None):
        url = f'{self.base_address}{path}'
        with allure.step(f'PUT request to: {url}'):
            return requests.put(url=url, params=params, data=data, headers=headers)

    def delete(self, path, params=None, data=None, headers=None):
        url = f'{self.base_address}{path}'
        with allure.step(f'DELETE request to: {url}'):
            return requests.delete(url=url, params=params, data=data, headers=headers)
