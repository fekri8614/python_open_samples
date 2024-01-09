# File: myhttpclient.py

import requests

class MyHTTPClient:
    def __init__(self, base_url):
        # Initialize the MyHTTPClient instance with a base URL for the API.
        self.base_url = base_url

    def make_request(self, method, endpoint, params=None, data=None, json_data=None):
        # Construct the full URL by combining the base URL and the specified endpoint.
        url = f"{self.base_url}/{endpoint}"

        # Set the default headers for the HTTP request, such as 'Content-Type'.
        headers = {'Content-Type': 'application/json'}  # You can customize headers as needed

        # Determine the HTTP method to be used and make the corresponding request.
        if method == 'GET':
            response = requests.get(url, params=params, headers=headers)
        elif method == 'POST':
            response = requests.post(url, params=params, data=data, json=json_data, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, params=params, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, params=params, data=data, json=json_data, headers=headers)
        else:
            # If an unsupported method is provided, print an error message and return None.
            print(f"Unsupported HTTP method: {method}")
            return None

        # Check if the HTTP request was successful (status code 200) and return the JSON response.
        if response.status_code == 200:
            return response.json()
        else:
            # If the request was not successful, print the error status code and return None.
            print(f"Error: {response.status_code}")
            return None

"""Example:
# File: main.py

from myhttpclient import MyHTTPClient

# Replace 'https://api.example.com' with the actual base URL of your API
base_url = 'https://api.example.com'
client = MyHTTPClient(base_url)

# Example GET request
result_get = client.make_request('GET', 'data_endpoint', params={'param1': 'value1'})
print("GET Result:", result_get)

# Example POST request with form data
result_post = client.make_request('POST', 'create', data={'key1': 'value1', 'key2': 'value2'})
print("POST Result:", result_post)

# Example DELETE request
result_delete = client.make_request('DELETE', 'delete_item', params={'id': '123'})
print("DELETE Result:", result_delete)

# Example PUT request with JSON data
result_put = client.make_request('PUT', 'update', json_data={'id': '123', 'new_value': 'updated'})
print("PUT Result:", result_put)"""
