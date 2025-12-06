import requests
import time

url = "https://ge3.pythonanywhere.com/ai"
# url = "http://127.0.0.1:5000/ai"

data = {"message": "напиши программу которая перемещает объект player вправо со скорость 2"}

response = requests.post(url, json=data)
ids = response.json()["ids"]

print(f"Request ID: {ids}")

while True:
    status = requests.get(f"{url}/status/{ids}").json()

    if status["status"] == "completed":
        print(status["response"])

        break

    if status["status"] == "error":
        print(f"Error: {status['error']}")

        break

    print("Waiting...")

    time.sleep(5)