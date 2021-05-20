import json
import pytest
import requests
import csv


def test_get(base_url):
    r = requests.get(base_url)
    print(base_url)
    assert r.status_code == 200


def test_book_create(base_url, book_create):
    pass


with open('1.csv', encoding='utf-8') as csvfile:
    books = []
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        book = {row[0]: row[1], row[2]: row[3]}
        books.append(book)
print(books)


@pytest.mark.parametrize("book_list", books)
def test_book_create_n(base_url, book_list, book_del):
    b = requests.post(f"{base_url}/books", data=book_list)
    assert b.status_code == 201
    book_del.update(b.json())


# role_data = [{"name": "Polonius1", "type": "Secondary1", "level": 21},
#    {"name": "Polonius2", "type": "Secondary2", "level": 22} ]

with open('2.json', 'r', encoding='utf-8') as f:
    role_data = json.load(f)
print(role_data)


@pytest.mark.parametrize("rol_list", role_data)
def test_create_role(book_create, base_url, rol_list):
    rol_list.update({"book": book_create["id"]})
    print(rol_list)
    resp = requests.post(f'{base_url}/roles', data=rol_list)
    assert resp.status_code == 201
    resp_body = resp.json()
    assert "id" in resp_body
    for key in rol_list:
        assert resp_body[key] == rol_list[key]


def test_create_role_n(book_create, base_url):
    role_data = {
        "name": "Polonius1",
        "type": "Secondary1",
        "level": 21,
        "book": 15
    }
    resp = requests.post(f'{base_url}/roles', data=role_data)
    assert resp.status_code == 400
