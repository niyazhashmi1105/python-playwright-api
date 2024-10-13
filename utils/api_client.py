import requests
from requests.auth import HTTPBasicAuth


class APIClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        pass

    def get_all_bookings(self, endpoint, headers, ):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=headers)
        return response

    def create_booking(self, endpoint, headers, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, headers=headers, json=data)
        return response

    def get_booking_by_id(self, endpoint, booking_id):
        url = f"{self.BASE_URL}/{endpoint}/{booking_id}"
        response = requests.get(url)
        return response

    def update_booking_by_id(self, endpoint, booking_id, data, headers):
        url = f"{self.BASE_URL}/{endpoint}/{booking_id}"
        response = requests.put(url, json=data, headers=headers)
        return response

    def partial_update_by_booking_id(self, endpoint, booking_id, username, password,data):
        url = f"{self.BASE_URL}/{endpoint}/{booking_id}"
        print(url)
        auth = HTTPBasicAuth(username, password)
        response = requests.patch(url, auth=auth, json=data)
        return response

    def delete_booking_by_id(self, endpoint, booking_id, headers):
        url = f"{self.BASE_URL}/{endpoint}/{booking_id}"
        response = requests.delete(url, headers=headers)
        return response
