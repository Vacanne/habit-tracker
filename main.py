import requests
from datetime import datetime
USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH = "YOUR_GRAPH_NAME"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# use this response first
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# this one is second
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
# you can also change date with this
# today = datetime(year=2024, month=5, day=15)
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.9"
}
# this is the 3rd
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
date_to_update = "DESIRED DATE IN YYYYMMDD FORMAT"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date_to_update}"

new_pixel_data = {
    "quantity": "31.69"
}

response = requests.put(url=update_endpoint, json=new_pixel_data,headers=headers)
print(response.text)
