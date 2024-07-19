import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from run import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'TakeWords' in response.data

def test_translate_route(client):
    response = client.get('/translate')
    assert response.status_code == 200
    assert b'TakeWords' in response.data

def test_nonexistent_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'Error 404' in response.data

def test_get_from_date(client):
    response = client.get('/api/v1.0/requests/yyyy-mm-dd')
    assert response.status_code == 200
    assert b'sorry' in response.data

def test_get_from_correct_date(client):
    response = client.get('/api/v1.0/requests/2024-07-12')
    assert response.status_code == 200
    assert b'user' in response.data

def test_get_user_url(client):
    response = client.get('/api/v1.0/user_requests/username')
    assert response.status_code == 200
    assert b'sorry' in response.data

def test_translate_text(client):
    response = client.get('/api/v1.0/translate?text=hello world')
    assert response.status_code == 200
    assert b'translate' in response.data

def test_get_words(client):
    response = client.get('/api/v1.0/words?url=https://pypi.org/project/Flask/')
    assert response.status_code == 200
    assert b'Pip' in response.data


