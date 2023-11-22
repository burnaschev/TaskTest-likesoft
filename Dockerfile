FROM python:3.10

WORKDIR /book

RUN pip install --upgrade pip

COPY requirements.txt /book

RUN pip install -r requirements.txt

COPY . .