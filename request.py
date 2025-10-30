import requests

url = "https://artyom7777.pythonanywhere.com/ai"

data = {
    "message": "напиши программу которая показывает hello world 200 кадров"
}

response = requests.post(url, json=data)

now = 1

while response.status_code != 200:
    print(f"ATTEMPT: {now}")

    now += 1

    response = requests.post(url, json=data)

result = response.json()
print(result["response"])
