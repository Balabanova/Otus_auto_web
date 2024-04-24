import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://192.168.56.1:8081')


@pytest.fixture(scope="session")
def base_url(request):
    url = request.config.getoption('--url')
    return url


@pytest.fixture(scope="session")
def driver(request):
    br = request.config.getoption('--browser')

    _browser = None
    if br == "chrome":
        options = Options()
        options.add_argument("--disable-notifications")
        _browser = webdriver.Chrome(options=options)
    elif br == "firefox":
        _browser = webdriver.Firefox()
    elif br == "edge":
        _browser = webdriver.Edge()
    else:
        raise Exception("Этот браузер пока не поддерживается")

    yield _browser
    _browser.quit()


@pytest.fixture(scope='class')
def prod_name():
    name = ""
    yield name

