import pytest
import json

from app import app
from app import Water

@pytest.fixture()
def defapp():
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(defapp):
    return defapp.test_client()

# Test routes

def test_request_example_missing(client):
    response = client.get('/water')
    result = json.loads(response.data)
    assert 'water' not in result
    assert len(result.keys()) == 0

def test_request_example_water(client, monkeypatch):
    monkeypatch.setattr(Water, 'read_water', lambda : {'water': 100})
    response = client.get('/water')
    result = json.loads(response.data)
    assert 'water' in result
    assert result['water'] == 100

def test_add_water_missing(client):
    response = client.get('/add_water')
    result = json.loads(response.data)
    assert len(result.keys()) == 0
    
def test_add_water(client, monkeypatch):
    monkeypatch.setattr(Water, 'read_water', lambda : {'water': 100})
    monkeypatch.setattr(Water, 'save_water', lambda x: x)
    response = client.get('/add_water')
    result = json.loads(response.data)
    assert 'water' in result
    assert 'adding' in result
    assert len(result['adding']) == 1
    assert result['adding'][0]['quantity'] == 10
    
def test_add_water_user_missing(client):
    response = client.get('/add_water/1')
    result = json.loads(response.data)
    assert len(result.keys()) == 0

def test_check_alert(client):
    response = client.get('/add_alert/1')
    assert response.text == 'missing water information'

# Test Methods

def test_method_read_water():
    result_water = Water.read_water(water_path='./test_water.json')
    assert 'water' in result_water
    assert result_water['water'] == 8
    
def test_method_read_water_by_user():
    result_water = Water.read_water_by_user(1, 'test_water')
    assert 'water' in result_water
    assert result_water['water'] == 6
    
    
def test_method_save_water():
    Water.save_water(12, water_path='./test_dd_water.json')
    
def test_method_save_water_by_user():
    Water.save_water_by_user(1, 1, 'test_dd_water')