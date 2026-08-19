import requests

API_URL = "https://java-aloha-napped.ngrok-free.dev/generate"

prompt = input("Enter your prompt: ")

response = requests.post(
    API_URL,
    json={"prompt": prompt},
    timeout=120
)

print("\nStatus Code:", response.status_code)
print("Response:")
print(response.text)