import requests
from jsonschema import validate
from tests.utils import load_json


def test_update_user():
    url = "https://reqres.in/api/users"
    user_id = 2

    payload = {
        "name": "Kirill",
        "job": "pinguin lifter"
    }

    response = requests.put(url + f'/{user_id}', data=payload)
    assert response.status_code == 200
    assert response.json()['name'] == 'Kirill'
    assert response.json()['job'] == 'pinguin lifter'
    validate(response.json(), load_json('update_user.json'))
