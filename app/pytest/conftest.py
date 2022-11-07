import pytest

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# from ..config import AppConfig


@pytest.fixture

def endpoint():
    iptest = "127.0.0.1"
    port = "5000"
    protocol = "http"
    res = ""
    if len(protocol) > 0 and len(iptest) > 0 and len(port) > 0:
        res = protocol + "://" + iptest + ":" + port
    return res


@pytest.fixture
def flask_app_mock():
    """Flask application setup."""
    app_mock = Flask("app")
    db = SQLAlchemy()
    app_mock = None
    return app_mock


@pytest.fixture

def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_alchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock



@pytest.fixture

def app():
    app = Flask(__name__)
    db = SQLAlchemy()
    db.init_app(app)
    db.create_all()

 

@pytest.fixture

def base_url():

    protocol, iptest, port,  = "http", "127.0.0.1", "5000",

    res = f'{protocol}://{iptest}:{port}/api/v1'

    return res



@pytest.fixture

def headers():

    return {'pop-token': "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnZW50ZXJhL2RldiIsInVzZXJfbmFtZSI6IkNpUUE0Sm1OSzNOZnFES2huQlo1c1BWVk91Uzd0dk9zaUk5cjVRMzRSdnNCOGxJWTU3SVNNd0QzQ01ZVjZ4WUtxV3laZ0dTTlRkUTZuUWhMTytiWExVemF4REo5M1JFc0pTS1VUNE1NV2NjNjZTc1NxODdvaGNibjlBPT0iLCJzaXN0ZW1hIjoiNGU0MGE3NTgtNzI3MS00Y2IzLWFkMTktNWRmNWEwZDhjZTU0IiwiaXNzIjoiaHR0cHM6Ly9jbG91ZC5nb29nbGUuY29tL2lhcCIsImNvbXBhcm5ldFRva2VuIjoiNGU0MGE3NTgtNzI3MS00Y2IzLWFkMTktNWRmNWEwZDhjZTU0Iiwibm9tYnJlQ29tcGxldG8iOiJQb3J0YWwgT3BlcmF0aXZvIE5lZ29jaW8gTmVnb2NpbyIsImF1dGhvcml0aWVzIjpbInRydXN0Il0sInJvbCI6Ik5lZ29jaW8iLCJjbGllbnRfaWQiOiJ5YXMtcG9ydGFsLW9wZXJhdGl2byIsInBlcmZpbCI6IjRlNDBhNzU4LTcyNzEtNGNiMy1hZDE5LTVkZjVhMGQ4Y2U1NCIsImF1ZCI6WyJ5YXMtcG9ydGFsLW9wZXJhdGl2byJdLCJuYmYiOjMwMCwibm9taW5hIjoiNDkiLCJzY29wZSI6WyJ0cnVzdCJdLCJleHAiOjE2NDM2OTcxNTMsImlhdCI6MTY0MzY5NTk1MzA3MSwianRpIjoiU3VSR1QtUXlua0VyTDc1NzFhdkdtYm1kT1BjIn0.azq8YgnrR9qz3CO6plUVtpA6CnLuCzTiXB9ifcCP-Kiy6sobV7s_lcxpkX_N0r1vGfSKPMks6sM18tvifzTufIp7inPq9QtKEp7fbQQekK9eX8uimrQTiLKfX3A44_MkWmw9cx2j82H7u48WnKMk2fN5djr3wiuU5EZIweSTt-yTyS4C-c4rD4iZZWDP1Gl-eEIlUrZUmTc2sxrSSFa8W05VYQat9AKDMy4ldW1vLuFPyUBlLzXoXNF6QrD3C-eLCn0lyBvWq0Jf_KK139E42UOHW7QuN3yzgmAXO9PdBHulhH_pgjjJuHXnqCQnkXWDvUCSwIK50sdW8hpOgA6N3g"}



@pytest.fixture

def client():

    from main import app

    with app.test_client() as client:

        with app.app_context():

            yield client