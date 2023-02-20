from flask import testing
from server import app

client = testing.FlaskClient(app)

def test_success():
    assert client.get('/').status_code == 200


def test_fail():
    assert client.get('/favicon.ico').status_code == 404