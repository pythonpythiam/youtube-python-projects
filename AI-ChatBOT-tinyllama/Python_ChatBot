import requests

while True:
    user = input("You: ")

    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": user,
            "stream": False
        }
    )

    print("AI:", r.json()["response"])
