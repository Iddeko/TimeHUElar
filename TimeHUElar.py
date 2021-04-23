import requests
import json
import time

#get token
url = "https://api.timeular.com/api/v3/developer/sign-in"

payload = {
  "apiKey"  : "MTExMDAyXzgwNDg4ZTU5NGIzYzRlMDU5ZjU2N2U2Njc3MWMzODc0",
  "apiSecret" : "MWUxYzQyNzJkMjZhNDVkNWE5NTZmYmE0MTQxYzU0MWY="
  }
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

token = str(response.text.encode('utf8')).split('"')[3]
print(response.text)

#get curent tracking

url = "https://api.timeular.com/api/v3/tracking"

payload = {}
headers = {
    'Authorization': f'Bearer {token}'
}

urlActivities = "https://api.timeular.com/api/v3/activities"
response = requests.get(urlActivities, headers=headers)
activities = {a["id"]:a["name"] for a in response.json()['activities']}
activities["None"] = "None"
previousActivity = None

while 1:
    response = requests.get(url, headers=headers, data = json.dumps(payload))
    activityId = None
    if response.json()["currentTracking"]:
        activityId =response.json()["currentTracking"]["activityId"]
    activity = activities[activityId] if activityId else "None"
    if  previousActivity !=  activity:
        previousActivity = activity
        print(activity)
    time.sleep(1)

