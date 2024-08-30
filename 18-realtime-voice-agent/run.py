#!/usr/bin/env python3
import requests
import json

headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9... ',
  'Content-Type': 'application/json'
}

print("\tCreate Room")
url = "https://api.cortex.cerebrium.ai/v4/1234567/realtime-agent/create_room"
payload = json.dumps({})
response = requests.request("POST", url, headers=headers, data=payload)
data = json.loads(response.text)

ROOM_URL = data["result"]["url"]
TOKEN = data["result"]["token"]

print("\t{}".format(ROOM_URL))
print("\n\t{}".format(TOKEN))

print("\n\tStart bot")
url = "https://api.cortex.cerebrium.ai/v4/1234567/realtime-agent/start_bot"
payload = json.dumps({"room_url": ROOM_URL, "token": TOKEN})
new_response = requests.request("POST", url, headers=headers, data=payload)
print(new_response.text)
