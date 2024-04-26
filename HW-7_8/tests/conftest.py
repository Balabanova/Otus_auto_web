import pytest
import logging
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://192.168.56.1:8081')
    parser.addoption('--launch', default='remote')
    parser.addoption('--executor', default='127.0.0.1')


@pytest.fixture(scope="session")
def base_url(request):
    url = request.config.getoption('--url')
    return url


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def driver(request):
    br = request.config.getoption('--browser')
    ex = request.config.getoption('--executor')
    la = request.config.getoption('--launch')

    if la == 'remote':
        if br == "chrome":
            options = ChromeOptions()
        elif br == "firefox":
            options = FirefoxOptions()
        else:
            raise Exception("Этот браузер пока не поддерживается")

        caps = {"browserName": br}

        for k, v in caps.items():
            options.set_capability(k, v)

        executor_url = f"http://{ex}:4444/wd/hub"
        driver = webdriver.Remote(command_executor=executor_url, options=options)
        driver.maximize_window()

    elif la == 'local':
        if br == "chrome":
            driver = webdriver.Chrome()
        elif br == "firefox":
            driver = webdriver.Firefox()
        else:
            raise Exception("Этот браузер пока не поддерживается")
    else:
        raise Exception("В --launch было передано что-то не то")

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    yield driver


@pytest.fixture(scope='class')
def prod_name():
    name = ""
    yield name


@pytest.fixture(scope="session")
def logger():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    def fin():
        attach = driver.get_screenshot_as_png()
        if request.node.rep_setup.failed:
            allure.attach(attach, name="screenshot", attachment_type=AttachmentType.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(attach, name="screenshot", attachment_type=AttachmentType.PNG)
    request.addfinalizer(fin)