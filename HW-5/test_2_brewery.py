from main import BaseReq
import pytest


@pytest.fixture(scope="class")
def setup(base_url):
    req = BaseReq(base_url["url_brewery"])
    yield req


class TestBrewery:
    def test_perpage(self, setup):
        req = setup
        res = req.get(f"/breweries?per_page=3")
        assert res.status_code == 200
        assert len(res.json()) == 3, f"Возвращено неверное количество записей"

    @pytest.mark.parametrize("brew_id, name",
                             [("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "MadTree Brewing 2.0"),
                              ("9c5a66c8-cc13-416f-a5d9-0a769c87d318", "(512) Brewing Co")])
    def test_id_search(self, setup, brew_id, name):
        req = setup
        res = req.get(f"/breweries/{brew_id}")
        assert res.status_code == 200
        assert res.json()['name'] == name, f"Возвращена неверная запись по ID"

    @pytest.mark.parametrize("city", ["Austin", "Norman"])
    def test_city_filter(self, setup, city):
        req = setup
        res = req.get(f"/breweries?by_city={city}&per_page=3")
        assert res.status_code == 200
        for elem in res.json():
            assert elem['city'] == city, f"Фильтр по городам не работает"

    @pytest.mark.parametrize("state", ["California", "Wisconsin", "Texas"])
    def test_state_filter(self, setup, state):
        req = setup
        res = req.get(f"/breweries?by_state={state}&per_page=3")
        assert res.status_code == 200
        for elem in res.json():
            assert elem['state_province'] == state, f"Фильтр по штату не работает"

    @pytest.mark.parametrize("type_b", ["micro",
                                        "nano",
                                        "regional",
                                        "brewpub",
                                        "large",
                                        "planning",
                                        "bar",
                                        "contract",
                                        "proprietor",
                                        "closed"])
    def test_type_filter(self, setup, type_b):
        req = setup
        res = req.get(f"/breweries?by_type={type_b}&per_page=3")
        assert res.status_code == 200
        for elem in res.json():
            assert elem['brewery_type'] == type_b, f"Фильтр по типу пивного заведения не работает"
