import pytest
from datetime import datetime
import requests
import globals

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope = "session", autouse=True)
def setup_teardown():
    print(" set up resources required for API Execution")
    yield
    print(" tearing down all resources")

@pytest.fixture(scope="session")
def auth_token():

    url = "https://restful-booker.herokuapp.com/auth"
    credentials = {
            "username": "admin",
            "password": "password123"
        }
    response = requests.post(url, json=credentials)
    assert response.status_code == 200, "Login failed!"
    token = response.json()["token"]
    assert token is not None, "Failed to retrieve token"
    return token

