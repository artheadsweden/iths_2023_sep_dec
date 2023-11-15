import requests
dn_data = requests.get("https://dn.se")
for i in range(1, 11):
    data = requests.get(f"http://numbersapi.com/{i}")

    print(data.text)

print(dn_data.text)