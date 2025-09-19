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


def load_users():
    """
    Loads users from users.json and handles file-related errors.

    Returns:
        list: A list of user dictionaries or an empty list if error occurs.
    """
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'users.json' file not found.")
    except json.JSONDecodeError:
        print("Error: 'users.json' contains invalid JSON.")
    return []


def filter_users_by_name(name):
    """
    Filters and prints users whose name matches the given input.

    Args:
        name (str): Name to filter users by.
    """
    users = load_users()
    if not users:
        return

    filtered_users = [
        user for user in users
        if user["name"].lower() == name.lower()
    ]

    if filtered_users:
        for user in filtered_users:
            print(f"Name: {user['name']}, Age: {user['age']}, "
                  f"Email: {user.get('email', 'N/A')}")
    else:
        print("No users found with that name.")


def filter_by_age(age):
    """
    Filters and prints users whose age matches the given input.

    Args:
        age (int): Age to filter users by.
    """
    users = load_users()
    if not users:
        return

    filtered_users = [
        user for user in users if user["age"] == age
    ]

    if filtered_users:
        for user in filtered_users:
            print(f"Name: {user['name']}, Age: {user['age']}, "
                  f"Email: {user.get('email', 'N/A')}")
    else:
        print("No users found with that age.")


def filter_by_email(email):
    """
    Filters and prints users whose email matches the given input.

    Args:
        email (str): Email address to filter users by.
    """
    users = load_users()
    if not users:
        return

    filtered_users = [
        user for user in users
        if user.get("email", "").lower() == email.lower()
    ]

    if filtered_users:
        for user in filtered_users:
            print(f"Name: {user['name']}, Age: {user['age']}, "
                  f"Email: {user.get('email', 'N/A')}")
    else:
        print("No users found with that email.")


def is_valid_email(email):
    """
    Validates basic structure of an email address using regex.

    Args:
        email (str): Email to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    """
    Entry point for the user filtering script.
    Allows filtering users by name, age, or email with input validation.
    """
    valid_options = ("name", "age", "email")
    filter_option = input(
        "Filter by 'name', 'age', or 'email': "
    ).strip().lower()

    if filter_option not in valid_options:
        print("Invalid filter option. Supported: name, age, email.")
    elif filter_option == "name":
        while True:
            name_to_search = input("Enter a name to filter users: ").strip()
            if name_to_search:
                filter_users_by_name(name_to_search)
                break
            else:
                print("Name cannot be empty. Please enter a valid name.")
    elif filter_option == "age":
        while True:
            age_input = input("Enter an age to filter users: ").strip()
            if not age_input:
                print("Age cannot be empty. Please enter a valid number.")
                continue
            if not age_input.isdigit():
                print("Invalid age! Please enter a number.")
                continue

            age_to_search = int(age_input)
            if age_to_search < 0:
                print("Age must be a positive number.")
                continue

            filter_by_age(age_to_search)
            break
    elif filter_option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()
            if not email_to_search:
                print("Email cannot be empty.")
                continue
            if not is_valid_email(email_to_search):
                print("Invalid email format. Try again.")
                continue

            filter_by_email(email_to_search)
            break
