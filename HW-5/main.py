import pprint
import requests


class BaseReq:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, req_type, json_data={}):
        stop_flag = False
        response = None
        while not stop_flag:
            if req_type == "GET":
                response = requests.get(url)
            elif req_type == "POST":
                response = requests.post(url, json=json_data)
            elif req_type == "DEL":
                response = requests.delete(url)
            elif req_type == "PATCH":
                response = requests.patch(url, json_data)

            if response.status_code != 0:
                stop_flag = True

        print("\n")
        pprint.pprint(req_type)
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.json())

        return response

    def get(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        resp = self._request(url, "GET")
        return resp

    def post(self, endpoint: str, json_data):
        url = f"{self.base_url}{endpoint}"
        resp = self._request(url, "POST", json_data)
        return resp

    def delete(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        resp = self._request(url, "DEL")
        return resp

    def patch(self, endpoint: str, json_data):
        url = f"{self.base_url}{endpoint}"
        resp = self._request(url, "PATCH", json_data)
        return resp
