import requests
import json


r = requests.get("http://localhost:8000/external-fake-api/22/")

# print(r.content)
# print(type(r.content))
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
# print(json.dumps(r.json()))
# print(type(json.dumps(r.json())))

print(json.dumps({"a": [1,2,3]}))
print(type(json.dumps({"a": [1,2,3]})))

print(json.loads(json.dumps({"a": [1,2,3]})))
print(type(json.loads(json.dumps({"a": [1,2,3]}))))

# print(r.text)
# print(r.json())
# print(type(r.json()))
#
#
# print(json.dumps(r.json()))
# print(type(json.dumps(r.json())))
