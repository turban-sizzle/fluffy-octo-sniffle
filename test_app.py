import pytest
import json
import datetime

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
    response = client.put('/add_water')
    result = json.loads(response.data)
    assert len(result.keys()) == 0

@pytest.mark.parametrize('water', [{'water': 100}, {'water': 100, 'adding': []}])    
def test_add_water(client, monkeypatch, water):
    monkeypatch.setattr(Water, 'read_water', lambda : water)
    monkeypatch.setattr(Water, 'save_water', lambda x: x)
    response = client.put('/add_water')
    result = json.loads(response.data)
    assert 'water' in result
    assert 'adding' in result
    assert len(result['adding']) == 1
    assert result['adding'][0]['quantity'] == 10

    
def test_add_water_user_missing(client):
    response = client.put('/add_water/1')
    result = json.loads(response.data)
    assert len(result.keys()) == 0

def test_add_water_user(client, monkeypatch):
    monkeypatch.setattr(Water, 'read_water_by_user', lambda user_id : {'water': 100})
    monkeypatch.setattr(Water, 'save_water_by_user', lambda x, user_id: x)
    response = client.put('/add_water/1')
    result = json.loads(response.data)
    assert 'water' in result
    assert result['water'] == 110

@pytest.mark.parametrize('result_read_water,expected', [(None, 'missing water information'), ( {'water': 100}, 'everything is ok'), ({'water': 8}, 'alert missing water')])
def test_check_alert_over_10(client, monkeypatch, result_read_water, expected):
    monkeypatch.setattr(Water, 'read_water_by_user', lambda user_id : result_read_water)
    response = client.get('/check_alert/1')
    assert response.text == expected


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
    
def test_method_save_water_bad_json_1():
    water = {'water': 10}
    water["adding"] = [{'added_at': str(datetime.datetime.now()), 'quantity': 10}]
    water_result = Water.save_water(water, water_path='./test_dd_water.json')
    assert len(water_result['adding']) == 1
    assert 'added_at' in water_result['adding'][0]

def test_method_save_water_bad_json_2():
    with pytest.raises(TypeError):
        water = {'water': 10, 'adding': []}
        water["adding"].append({'added_at': datetime.datetime.now(), 'quantity': 10})
        Water.save_water(water, water_path='./test_dd_water.json')
    
    
def test_method_save_water_by_user():
    Water.save_water_by_user(1, 1, 'test_dd_water')
    
