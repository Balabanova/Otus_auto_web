import pytest


@pytest.fixture(scope="session")
def base_url():
    url_dog = "https://dog.ceo"
    url_typicode = "https://jsonplaceholder.typicode.com"
    url_brewery = "https://api.openbrewerydb.org/v1"
    return {"url_dog": url_dog,
            "url_typicode": url_typicode,
            "url_brewery": url_brewery}


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")
    parser.addoption("--status_code", default=200)
