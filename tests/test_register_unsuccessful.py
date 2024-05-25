import requests
from jsonschema import validate
from tests.utils import load_json


def test_login_unsuccessful():
    url = "https://reqres.in/api/register"

    payload = {
        "email": "sydney@fife"
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 400
    validate(response.json(), load_json('register_unsuccessful.json'))
