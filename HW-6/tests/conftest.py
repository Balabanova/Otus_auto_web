import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://192.168.56.1:8081')


@pytest.fixture(scope="session")
def base_url(request):
    url = request.config.getoption('--url')
    return url


@pytest.fixture(scope="session")
def browser(request):
    br = request.config.getoption('--browser')

    _browser = None
    if br == "chrome":
        _browser = webdriver.Chrome()
    elif br == "firefox":
        _browser = webdriver.Firefox()
    elif br == "edge":
        _browser = webdriver.Edge()
    else:
        raise Exception("Этот браузер пока не поддерживается")

    yield _browser
    _browser.quit()
