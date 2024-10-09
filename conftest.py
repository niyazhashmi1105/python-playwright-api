import pytest
from datetime import datetime
import requests
import os
import json
from faker import Faker

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

@pytest.fixture()
def load_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data

@pytest.fixture()
def generate_firstname():
    faker = Faker()
    return faker.first_name()

@pytest.fixture()
def generate_lastname():
    faker = Faker()
    return faker.last_name()

@pytest.fixture()
def generate_int():
    faker = Faker()
    return faker.random_int(min=100, max=500)

@pytest.fixture()
def generate_checkin_checkout_date():
    faker = Faker()
    start_date = faker.future_date(end_date="+60d")
    end_date = faker.future_date(end_date="+90d")
    return start_date, end_date
