import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
json_response = response.json()

assert response.status_code == 200
print(json_response)         # ✅ parsed JSON data



##### POST call ####

response = requests.post("https://jsonplaceholder.typicode.com/posts", json = {"title": "foo", "body": "bar", "userId": 1},headers={"Content-Type": "application/json"})
json_response = response.json()
assert response.status_code == 201, 'post method failed'
print(json_response)