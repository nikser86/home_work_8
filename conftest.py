import pytest
import requests

book_list = [
    {"title": "sfs fsedf", "author": "sdfsd sdvfsd"},
    {"title": "12312", "author": "1231"},
    {"title": "выапвыа", "author": "фіафівфів"}
]


@pytest.fixture()
def base_url():
    return 'http://pulse-rest-testing.herokuapp.com'


def book_create_p(base_url, book_list):
    book_data = {'title': 'Big book1', 'author': 'Herman'}
    resp = requests.post(f'{base_url}/books', data=book_list)
    book_body_resp = resp.json()
    yield book_body_resp
    resp = requests.delete(f'{base_url}/books/{book_body_resp["id"]}')


@pytest.fixture()
def book_del(base_url):
    d={}
    yield d
    print(d)
    if 'id' in d:
        resp = requests.delete(f'{base_url}/books/{d["id"]}')


@pytest.fixture()
def book_create(base_url):
    book_data = {'title': 'Big book1', 'author': 'Herman'}
    resp = requests.post(f'{base_url}/books', data=book_data)
    book_body_resp = resp.json()
    yield book_body_resp
    resp = requests.delete(f'{base_url}/books/{book_body_resp["id"]}')
