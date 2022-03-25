import pytest
from utils.request_helper import ApiClient


@pytest.fixture
def api():
    return ApiClient(base_address='https://automationexercise.com/api/')
