from main import BaseReq
from api_helper_generator import get_random_number, get_random_tuple
import pytest


@pytest.fixture(scope="class")
def setup(base_url):
    req = BaseReq(base_url["url_typicode"])
    yield req


class TestTypicode:
    @pytest.mark.parametrize("rec_id", get_random_number(5, 1, 100))
    def test_id_return_rec(self, setup, rec_id):
        req = setup
        res = req.get(f"/posts/{rec_id}")
        assert res.status_code == 200
        assert res.json()['id'] == rec_id, f"Ошибка! Возвращена неверная запись по ID"

    @pytest.mark.parametrize("title, body, user_id",
                             [("Hello", "world", "22"),
                              ("My", "name", "47"),
                              ("It's", "joke", "777")])
    def test_create_rec(self, setup, title, body, user_id):
        req = setup
        json = {"title": title, "body": body, "user_id": user_id}
        res = req.post(f"/posts", json)
        assert res.status_code == 201
        assert res.json()["id"] not in ('0', ''), f"Ошибка! POST запрос неудался"

    @pytest.mark.parametrize("rec_id, title, body",
                             [(1, "New_title_1", "new_body_1"),
                              (2, "New_title_2", "new_body_2"),
                              (3, "New_title_3", "new_body_3")])
    def test_patch_rec(self, setup, rec_id, title, body):
        req = setup
        patt = {'body': body,
                'id': rec_id,
                'title': title, }
        json = {"title": title, "body": body}
        res = req.patch(f"/posts/{rec_id}", json)
        assert res.status_code == 200
        for key, value in patt.items():
            assert value == res.json()[key], "Ошибка! PATCH запрос неудался"

    @pytest.mark.parametrize("rec_id", get_random_number(5, 1, 20))
    def test_delete_rec(self, setup, rec_id):
        req = setup
        res = req.delete(f"/posts/{rec_id}")
        assert res.status_code == 200
        assert res.json() == {}, "Ошибка! DELETE запрос неудался"

    @pytest.mark.parametrize("post_id", get_random_number(5, 1, 100))
    def test_filter_rec(self, setup, post_id):
        req = setup
        res = req.get(f"/posts/{post_id}/comments")
        assert res.status_code == 200
        for elem in res.json():
            assert elem["postId"] == post_id
