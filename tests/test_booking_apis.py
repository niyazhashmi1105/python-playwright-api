import pytest
from requests.auth import HTTPBasicAuth

from conftest import load_data, generate_firstname
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
    assert response.status_code == 200, f"Expected Response code is 200 but got {response.status_code}"
    assert len(response.json()) > 0
    assert isinstance(response.json(), list), "Expected response to be a list of objects"


def test_create_booking(api_client,auth_token,load_data,generate_firstname):
    headers = {
        "Authorization": f"Basic {auth_token}"
    }

    boooking_details = load_data["booking_details_data"]
    fname = generate_firstname
    boooking_details['firstname'] = fname
    response = api_client.create_booking("booking", headers, boooking_details)
    globals.booking_id = response.json()['bookingid']
    assert response.status_code == 200, f"Expected status code is 200 but got invalid {response.status_code}"
    assert response.json()['bookingid'] == globals.booking_id, f"Invalid booking id {response.json()['bookingid']}"
    assert response.json()['booking'][
               'firstname'] == fname, f"Invalid first name {response.json()['booking']['firstname']}"
    assert response.json()['booking'][
               'totalprice'] == 111, f"Invalid total price {response.json()['booking']['totalprice']}"
    return globals.booking_id


def test_get_booking_by_id(api_client):
    booking_id = globals.booking_id
    #print(booking_id)
    response = api_client.get_booking_by_id("booking", booking_id)
    assert response.json()['lastname'] == "Brown", f"Invalid last name got {response.json()['lastname']}"
    assert response.json()['depositpaid'] == True, f"Invalid deposit paid received {response.json()['depositpaid']}"
    assert response.json()['bookingdates']['checkin'] == "2018-01-01", \
        f"Invalid booking checkin date {response.json()['bookingdates']['checkin']}"
    assert response.json()[
               'additionalneeds'] == "Breakfast", f"Invalid Additional needs {response.json()['additionalneeds']}"

@pytest.mark.usefixtures()
def test_update_booking_by_id(api_client,auth_token,load_data,generate_lastname):
    booking_id = globals.booking_id
    #print(booking_id)

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token = {auth_token}"
    }
    boooking_details = load_data["booking_details_data"]
    lname = generate_lastname
    boooking_details['lastname'] = lname

    response = api_client.update_booking_by_id("booking", booking_id, boooking_details, headers)
    assert response.status_code == 200, f"Invalid status code got {response.status_code}"
    assert response.json()['lastname'] == lname, f"Invalid last name got {response.json()['lastname']}"
    assert response.json()['depositpaid'] == True, f"Invalid deposit paid received {response.json()['depositpaid']}"
    assert response.json()['bookingdates']['checkin'] == "2018-01-01", \
        f"Invalid booking checkin date {response.json()['bookingdates']['checkin']}"
    assert response.json()[
               'additionalneeds'] == "Breakfast", f"Invalid Additional needs {response.json()['additionalneeds']}"

@pytest.mark.usefixtures()
def test_partial_update_booking_by_id(api_client,load_data,generate_firstname,generate_lastname):
    booking_id = globals.booking_id

    username = "admin"
    password = "password123"

    headers = {
        "Content-Type": "application/json",
    }
    patch_update_details = load_data["partial_update"]
    fname = generate_firstname
    lname = generate_lastname
    patch_update_details['firstname'] = fname
    patch_update_details['lastname'] = lname

    response = api_client.partial_update_by_booking_id("booking",booking_id, username,password, patch_update_details)
    assert response.status_code == 201, f"Invalid status code got {response.status_code}"
    assert response.json()['firstname'] == fname, f"Invalid first name got {response.json()['firstname']}"
    assert response.json()['lastname'] == lname, f"Invalid last name got {response.json()['lastname']}"


def test_delete_booking_by_id(api_client,auth_token):
    booking_id = globals.booking_id
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token = {auth_token}"
    }
    response = api_client.delete_booking_by_id("booking", booking_id,headers)
    assert response.status_code == 201,f"Failed to delete booking {response.status_code}"