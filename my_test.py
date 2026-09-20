import requests

# A different, very simple website URL
url = "http://codewithharry.com"

print("--- Sending Request ---")
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Text:")
print(response.text)
