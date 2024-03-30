import socket
import re
from http.server import BaseHTTPRequestHandler
from io import BytesIO
from http import HTTPStatus


HOST = "127.0.0.1"
PORT = 61111

END_OF_STREAM = '\r\n\r\n'

STATUS_PATT = r"\/\?status=(\d{3})"


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message=None, explain=None):
        self.error_code = code
        self.error_message = message


def status_parser(req):
    status_code = re.search(STATUS_PATT, req)
    try:
        status_code = status_code.group(1)
        status = HTTPStatus(int(status_code)).phrase
    except (ValueError, AttributeError):
        status_code = "200"
        status = HTTPStatus(int(status_code)).phrase
    return f"{status_code} {status}"


def send_answer(req, addr):
    status_code = status_parser(req.requestline)

    answer = (
        f"""HTTP/1.1 {status_code}\n
Content-Type: text/html
Request Method: {req.command}
Response Status: {status_code}\n"""
    )
    # Если запрос без ошибки, то передаём все принятые заголовки обратно
    if status_code == '200 OK':
        for key in request.headers.keys():
            answer += f"""{key}: {request.headers[key]}\n"""

    # Отправка
    conn.sendall(answer.encode('utf-8'))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    while True:
        server.listen()
        conn, addr = server.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(65000)
            request = HTTPRequest(data)
            send_answer(request, addr)
