import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Book Library' in response.data

def test_add_book(client):
    response = client.post('/add', data={
        'title': '1984',
        'author': 'George Orwell'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'1984' in response.data
    assert b'George Orwell' in response.data
