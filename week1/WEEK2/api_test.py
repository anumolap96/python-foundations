
import requests   # library used to make internet requests

# API endpoint that returns JSON data
url = "https://api.github.com"

# send request to server
response = requests.get(url)

# convert response JSON into Python dictionary
data = response.json()

# print the received data
print(data)