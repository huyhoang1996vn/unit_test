import json
from flask_api import app
import pytest

@pytest.fixture
def input_value():
   input = 16
   return input

def test_get_all_books():
    # assert input_value % 2 == 0
    response = app.test_client().get('/api')
    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list
    
    
def test_handle():
   print("========== 11")
   assert 1 == 1  
    