'''Using the JSONPlaceholder API, write a Python program to perform the following operations:

Ask for a username and retrieve the user's name and email using GET.
Ask the user for name, username, and email, create a dictionary, and add the user using POST.
Ask for a user ID and delete the user using DELETE.
Ask for a username, update the user's information using PUT.'''

import requests

url = "https://jsonplaceholder.typicode.com/users"

# GET - Search user by username
username = input("Username: ")
users = requests.get(url).json()

for u in users:
    if u["username"].lower() == username.lower():
        print(u["name"], u["email"])

# POST - Create new user
user = {
    "name": input("Name: "),
    "username": input("Username: "),
    "email": input("Email: ")
}

response = requests.post(url, json=user)
print("Created:", response.json())

# DELETE - Delete user
user_id = input("User ID to delete: ")

response = requests.delete(f"{url}/{user_id}")
print("Delete status:", response.status_code)

# PUT - Update user
username = input("Username to update: ")

for u in users:
    if u["username"].lower() == username.lower():

        updated = {
            "name": input("New name: "),
            "username": u["username"],
            "email": input("New email: ")
        }

        response = requests.put(
            f"{url}/{u['id']}",
            json=updated
        )

        print("Updated:", response.json())
        break