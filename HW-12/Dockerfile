FROM python:latest

WORKDIR /app

COPY ./HW-7_8/* .

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["pytest"]
