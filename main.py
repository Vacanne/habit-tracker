import requests
from datetime import datetime

# Define your Pixela user details and graph name
USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH = "YOUR_GRAPH_NAME"

# Endpoint for creating a new user
pixela_endpoint = "https://pixe.la/v1/users"

# User parameters for creating a new user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment this section to create a new user (only needed once)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Endpoint for creating a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Configuration for the new graph
graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

# Headers for authentication
headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment this section to create a new graph (only needed once)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Endpoint for adding a pixel to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

# Get the current date
today = datetime.now()

# Data for the new pixel
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.9"
}

# Uncomment this section to add a new pixel
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Define the date to update the pixel in YYYYMMDD format
date_to_update = "20240606"  # Example date, change as needed

# Endpoint for updating an existing pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date_to_update}"

# Data for updating the pixel
new_pixel_data = {
    "quantity": "31.69"
}

# Send the request to update the pixel
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
