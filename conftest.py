import sqlite3
from collections import namedtuple

from requests import session
from selenium import webdriver
import pytest
from faker import Faker  # Позволяет генерировать данные, pip3 install faker
from dataclasses import dataclass
import requests
#
#
# @pytest.fixture  # Таким образом, функция будет восприниматься, как фикстура
# def connect_database():
#     # Установка соединения с базой данных
#     connection = sqlite3.connect('test.db')
#
#     print("Соединение с БД установлено")
#
#     # Возвращение соединения с БД
#     return connection
#
#
# fake = Faker()  # Через этот обьект будет генерировать данные
#
#
# @pytest.fixture
# def generate_data():
#     login = fake.email()
#     password = fake.password()
#     UserData = namedtuple('UserData', ['login', 'password'])  # именованный tuple
#     return UserData(login, password)  # Возвращаем обьект
#
#
# @dataclass
# class UserData:
#     login: str
#     password: str
#
#
# @pytest.fixture
# def generate_data_new():
#     # Генерация данных
#     login = fake.email()
#     password = fake.password()
#
#     # Возвращение объекта UserData
#     return UserData(login, password)
#
#
# @pytest.fixture # autouse=True
# def generate_data_cls(request):
#     # Генерируем данные
#     request.cls.login = fake.email()
#     request.cls.password = fake.password()
#
#
# @pytest.fixture(name="driver")  # Имя driver ,autouse=True
# def webdriver_init(request):
#     driver = webdriver.Chrome()
#     request.cls.driver = driver


@pytest.fixture
def get_joke():
    response = requests.get("https://geek-jokes.sameerkumar.website/api")
    assert response.status_code == 200, "Server jokes doesn't work"
    if not response.text:
        return "None"
    else:
        return response.text
