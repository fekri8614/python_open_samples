# Replace 'https://api.example.com' with the actual base URL of your API
from myhttpclient.myhttpclient import MyHTTPClient


base_url = 'https://clever-planets-lick.loca.lt/data'
client = MyHTTPClient(base_url)

# Example GET request
result_get = client.make_request('GET', 'data_endpoint', params={'param1': 'value1'})
print("GET Result:", result_get)