import requests

post_data = {
    'date': '2023-02-23', 
    'time': '12:23:10'
}

data = requests.post("http://127.0.0.1:5000/temps", json=post_data)

print(data.text)

post_data = {
    'height': 173, 
    'weight': 78
}

data = requests.post("http://127.0.0.1:5000/size", json=post_data)

print(data.text)


# # Convert to dict
# data = data.json()

# print(data['name'])
# print(data['age'])

# for i in range(1, 11):
#     data = requests.get(f"http://numbersapi.com/{i}")

#     print(data.text)
