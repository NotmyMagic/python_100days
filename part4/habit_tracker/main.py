import requests
from datetime import datetime

USERNAME = "notmymagic"
TOKEN = "osid83nn5dj8skm"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
 "token": TOKEN,
 "username": USERNAME,
 "agreeTermsOfService": "yes",
 "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# {"message":"Success. Let's visit https://pixe.la/@notmymagic , it is your profile page!","isSuccess":true}

graph_config = {
    "id": "graph1",
    "name": "Books Read",
    "unit": "chapter",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# {"message":"Success.","isSuccess":true}

today = datetime.now()


pixel_create_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many chapters have you read today? ")
}

pixel_endpoint = f"{graph_endpoint}/graph1"

response = requests.post(url=pixel_endpoint, json=pixel_create_data, headers=headers)
print(response.text)
print("Please go here to see your graph: https://pixe.la/v1/users/notmymagic/graphs/graph1.html")

pixel_edit_data = {
    "quantity": "1",
}

pixel_edit_endpoint = f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"

# response = requests.put(url=pixel_edit_endpoint, json=pixel_edit_data, headers=headers)
# print(response.text)

# response = requests.delete(url=pixel_edit_endpoint, headers=headers)
# print(response.text)