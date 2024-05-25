import requests
from jsonschema import validate
from tests.utils import load_json


def test_get_user():
    url = "https://reqres.in/api"
    user_id = 10
    response = requests.get(f'{url}/users/{user_id}')
    assert response.status_code == 200
    assert response.json()['data']['id'] == 10
    assert response.json()['data']['email'] == 'byron.fields@reqres.in'
    assert response.json()['data']['first_name'] == 'Byron'
    validate(response.json(), load_json('get_user.json'))


def test_get_not_found_user():
    url = "https://reqres.in/api"
    user_id = 1000
    response = requests.get(f'{url}/users/{user_id}')
    assert response.status_code == 404
    assert response.json() == {}
