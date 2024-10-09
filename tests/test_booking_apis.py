import pytest
from utils.api_client import APIClient
import globals


@pytest.fixture(scope='module')
def api_client():
    return APIClient()


def test_get_all_bookings(api_client,auth_token):

    headers = {
        "Authorization": f"Basic {auth_token}"
    }
    response = api_client.get_all_bookings("booking", headers)
    #print(response.json())
    assert response.status_code == 200, f"Expected Response code is 200 but got {response.status_code}"
    assert len(response.json()) > 0
    assert isinstance(response.json(), list), "Expected response to be a list of objects"


def test_create_booking(api_client,auth_token):
    headers = {
        "Authorization": f"Basic {auth_token}"
    }
    booking_details_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_client.create_booking("booking", headers, booking_details_data)
    #print(response.json())
    globals.booking_id = response.json()['bookingid']
    assert response.status_code == 200, f"Expected status code is 200 but got invalid {response.status_code}"
    assert response.json()['bookingid'] == globals.booking_id, f"Invalid booking id {response.json()['bookingid']}"
    assert response.json()['booking'][
               'firstname'] == "Jim", f"Invalid first name {response.json()['booking']['firstname']}"
    assert response.json()['booking'][
               'totalprice'] == 111, f"Invalid total price {response.json()['booking']['totalprice']}"
    return globals.booking_id


def test_get_booking_by_id(api_client):
    booking_id = globals.booking_id
    #print(booking_id)
    response = api_client.get_booking_by_id("booking", booking_id)
    #print(response.json())
    assert response.json()['lastname'] == "Brown", f"Invalid last name got {response.json()['lastname']}"
    assert response.json()['depositpaid'] == True, f"Invalid deposit paid received {response.json()['depositpaid']}"
    assert response.json()['bookingdates']['checkin'] == "2018-01-01", \
        f"Invalid booking checkin date {response.json()['bookingdates']['checkin']}"
    assert response.json()[
               'additionalneeds'] == "Breakfast", f"Invalid Additional needs {response.json()['additionalneeds']}"

@pytest.mark.usefixtures()
def test_update_booking_by_id(api_client,auth_token):
    booking_id = globals.booking_id
    #print(booking_id)

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token = {auth_token}"
    }
    update_data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_client.update_booking_by_id("booking", booking_id, update_data, headers)
    #print(response.json())
    assert response.status_code == 200, f"Invalid status code got {response.status_code}"
    assert response.json()['firstname'] == "James", f"Invalid last name got {response.json()['firstname']}"
    assert response.json()['depositpaid'] == True, f"Invalid deposit paid received {response.json()['depositpaid']}"
    assert response.json()['bookingdates']['checkin'] == "2018-01-01", \
        f"Invalid booking checkin date {response.json()['bookingdates']['checkin']}"
    assert response.json()[
               'additionalneeds'] == "Breakfast", f"Invalid Additional needs {response.json()['additionalneeds']}"


def test_delete_booking_by_id(api_client,auth_token):
    booking_id = globals.booking_id
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token = {auth_token}"
    }
    response = api_client.delete_booking_by_id("booking", booking_id,headers)
    assert response.status_code == 201,f"Failed to delete booking {response.status_code}"