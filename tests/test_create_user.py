import requests
from jsonschema import validate
from tests.utils import load_json


def test_create_user():
    url = "https://reqres.in"
    endpoint = '/api/users'

    payload = {
        "name": "Kirill",
        "job": "penguin lifter"
    }

    response = requests.post(url + endpoint, data=payload)
    assert response.status_code == 201
    assert response.json()['name'] == 'Kirill'
    assert response.json()['job'] == 'penguin lifter'
    validate(response.json(), load_json('create_user.json'))
