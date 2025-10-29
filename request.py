import requests

url = "https://artyom7777.pythonanywhere.com/ai"

data = {
    "message": "напиши программу которая выводит сумму 2 и 3 в консоль и что бы в консоль каждые 10 кадров писалось hello world"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(result["response"])

else:
    print("ERROR:", response.json())
