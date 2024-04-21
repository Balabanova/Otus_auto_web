from main import BaseReq
import pytest


@pytest.fixture(scope="class")
def setup(self, base_url):
    req = BaseReq(base_url["url_dog"])
    yield req


class TestDog:
    def test_random(self, setup):
        req = setup
        res = req.get("/api/breeds/image/random")
        assert res.status_code == 200
        assert res.json()['status'] == "success", f"Запрос вернул ошибку: {res.json()['message']}"

    def test_all_dog_images(self, setup):
        req = setup
        res = req.get("/api/breed/affenpinscher/images")
        assert res.status_code == 200
        assert res.json()['status'] == "success", f"Запрос вернул ошибку: {res.json()['message']}"

    def test_all_breed_images(self, setup):
        req = setup
        res = req.get("/api/breed/hound/images")
        assert res.status_code == 200
        assert res.json()['status'] == "success", f"Запрос вернул ошибку: {res.json()['message']}"

    @pytest.mark.parametrize("dog, status, code",
                             [("akita", "success", 200),
                              ("fifo", "error", 404),
                              ("lifo", "error", 404),
                              ("affenpinscher", "success", 200)])
    def test_dog(self, setup, dog, status, code):
        req = setup
        res = req.get(f"/api/breed/{dog}/images/random")
        assert res.status_code == code
        assert status == res.json()['status'], f"Запрос вернул ошибку: {res.json()['message']}"

    @pytest.mark.parametrize("breed, status, code",
                             [("hound", "success", 200),
                              ("mastiff", "success", 200)])
    def test_breed(self, setup, breed, status, code):
        req = setup
        res = req.get(f"/api/breed/{breed}/list")
        assert res.status_code == code
        assert status == res.json()['status'], f"Запрос вернул ошибку: {res.json()['message']}"
