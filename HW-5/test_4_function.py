import pytest
import requests


@pytest.fixture
def function_fix(request):
    url = request.config.getoption('--url')
    status_code = request.config.getoption('--status_code')
    return url, status_code


def test_function(function_fix):
    url, status_code = function_fix
    res = requests.get(url)
    code = res.status_code
    assert code == int(status_code), "It's not good"
