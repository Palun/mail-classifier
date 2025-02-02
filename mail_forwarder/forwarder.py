import json
import requests
import pprint

getComponentsURL = "https://api.statuspage.io/v1/pages/n814cl79vp6c/components"
headers = {"Authorization": "OAuth dc20ab8b-cb02-4fff-9374-e50635bb0e7c"}


r = requests.get(url=getComponentsURL, headers=headers)
data = r.json()

print(r.json)

components = {}
for obj in data:
    components[obj["name"]] = obj["id"]

# print(components)


# match name from email tokenizer

name = "Swedbank"

componentId = components[name]

postIncidentURL = "https://api.statuspage.io/v1/pages/n814cl79vp6c/incidents"
headers = {"Authorization": "OAuth dc20ab8b-cb02-4fff-9374-e50635bb0e7c"}
data = {
    "incident": {
        "name": "Bank Down",
        "status": "investigating",
        "body": "Everythiing is down",
        "component_ids": [componentId],
    }
}


r = requests.post(url=postIncidentURL, json=data, headers=headers)

print(r.text)
