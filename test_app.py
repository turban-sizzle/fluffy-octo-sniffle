import pytest
import json

from app import app

@pytest.fixture()
def defapp():
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(defapp):
    return defapp.test_client()


def test_request_example(client):
    response = client.get('/water')
    result = json.loads(response.data)
    assert 'water' not in result
    assert len(result.keys()) == 0

def test_add_water(client):
    response = client.get('/add_water')
    result = json.loads(response.data)
    assert len(result.keys()) == 0
    
def test_add_water_user(client):
    response = client.get('/add_water/1')
    result = json.loads(response.data)
    assert len(result.keys()) == 0

def test_check_alert(client):
    response = client.get('/add_alert/1')
    assert response.text == 'missing water information'
