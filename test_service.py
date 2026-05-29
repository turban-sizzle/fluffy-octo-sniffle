from service import Water
import pytest
import datetime
import os

# Test Methods

# class PathMonkey:
    
#      @staticmethod
#      def isfile(path):
#          return True

def test_method_read_water(monkeypatch):
    
    monkeypatch.setattr(Water, '_open_load_water', lambda water_path:{'water': 8})
    
    result_water = Water.read_water(water_path='./test_water.json')
    assert 'water' in result_water
    assert result_water['water'] == 8
    
def test_method_read_water_by_user(monkeypatch):
    monkeypatch.setattr(Water, '_open_load_water', lambda water_path:{'water': 6})
    result_water = Water.read_water_by_user(1, 'test_water')
    assert 'water' in result_water
    assert result_water['water'] == 6
    
    
def test_method_save_water(monkeypatch):
    monkeypatch.setattr(Water, '_write_water', lambda wp, wj: wj)
    Water.save_water(12, water_path='./test_dd_water.json')
    
def test_method_save_water_bad_json_1(monkeypatch):
    monkeypatch.setattr(Water, '_write_water', lambda wp, wj: wj)
    water = {'water': 10}
    water["adding"] = [{'added_at': str(datetime.datetime.now()), 'quantity': 10}]
    water_result = Water.save_water(water, water_path='./test_dd_water.json')
    assert len(water_result['adding']) == 1
    assert 'added_at' in water_result['adding'][0]

def test_method_save_water_bad_json_2(monkeypatch):
    monkeypatch.setattr(Water, '_write_water', lambda wp, wj: wj)    
    with pytest.raises(TypeError):
        water = {'water': 10, 'adding': []}
        water["adding"].append({'added_at': datetime.datetime.now(), 'quantity': 10})
        Water.save_water(water, water_path='./test_dd_water.json')
    
    
def test_method_save_water_by_user(monkeypatch):
    monkeypatch.setattr(Water, '_write_water', lambda wp, wj: wj)    
    water = Water.save_water_by_user({'water': 31}, 1, 'test_dd_water')
    assert water['water'] == 31
