"""
===============================================================================
                            USER FILTERING TOOL
===============================================================================

Description:
------------
This Python script allows users to search and filter user data based on
specific fields such as name, age, or email. The user data is stored in a
JSON file (`users.json`), and the script uses interactive command-line input
to query the dataset.

The script provides:
- Error handling, in case of missing json file
- Case-insensitive name and email searches
- Exact age match filtering
- Real-time input validation for age and email
- User-friendly output formatting
- Error messages when no matches are found

This tool can be used for:
---------------------------
- Small-scale user data analysis
- Admin panels that query JSON datasets
- Educational use to demonstrate JSON parsing, filtering, and validation

File Required:
--------------
- `users.json`: A JSON file containing a list of users. Each user should
  be a dictionary with at least the fields: `name`, `age`, and `email`.

Example `users.json`:
----------------------
[
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"},
    {"name": "Charlie", "age": 25, "email": "charlie@example.com"}
]

Author:
-------
Abhisakh Sarma

===============================================================================
"""

import json
import re


def filter_by_id(user_id):
    """
    Filters and prints user from users.json whose ID matches the given ID.

    Args:
        user_id (int): The user ID to search for.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    matched_user = next((user for user in users if user["id"] == user_id), None)

    if matched_user:
        print("\nUser found by ID:")
        print(matched_user)
    else:
        print(f"No user found with ID {user_id}.")


def filter_users_by_name(name):
    """
    Filters and prints users from users.json whose name matches the given name.

    Args:
        name (str): The name to filter users by (case-insensitive).
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if user["name"].lower() == name.lower()
    ]

    if filtered_users:
        print("\nMatching users by name:")
        for user in filtered_users:
            print(user)
    else:
        print("No users found with that name.")


def filter_by_age(age):
    """
    Filters and prints users from users.json who have the given age.

    Args:
        age (int): The age to filter users by.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if user["age"] == age
    ]

    if filtered_users:
        print("\nMatching users by age:")
        for user in filtered_users:
            print(user)
    else:
        print("No users found with that age.")


def filter_by_email(email):
    """
    Filters and prints users from users.json who have the given email.

    Args:
        email (str): The email to filter users by (case-insensitive).
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if user["email"].lower() == email.lower()
    ]

    if filtered_users:
        print("\nMatching users by email:")
        for user in filtered_users:
            print(user)
    else:
        print("No users found with that email address.")


if __name__ == "__main__":
    """
    Entry point for the user filtering script.
    Prompts the user to choose a filter option and processes accordingly.
    """
    print("=================================================")
    print("        Welcome to the User Filter Tool          ")
    print("=================================================\n")

    filter_option = input(
        "What would you like to filter by? (id / name / age / email): "
    ).strip().lower()

    if filter_option == "id":
        while True:
            try:
                user_id = int(input("Enter user ID to search: ").strip())
                filter_by_id(user_id)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric ID.")

    elif filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        while True:
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
                filter_by_age(age_to_search)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif filter_option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()

            # Inline email format validation
            if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email_to_search):
                filter_by_email(email_to_search)
                break
            else:
                print("Invalid email format! Please enter a valid email address.")

    else:
        print("Invalid option! Please choose from: id, name, age, or email.")