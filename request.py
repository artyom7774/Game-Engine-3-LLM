import requests

url = "https://artyom7777.pythonanywhere.com/ai"

data = {
    "message": "напиши программу которая пишет абракадабра каждые 5 кадров"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["response"])

else:
    print("ERROR:", response.json())
