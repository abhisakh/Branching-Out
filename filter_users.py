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

# ANSI color codes
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_CYAN = "\033[36m"
COLOR_MAGENTA = "\033[35m"


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
        print(f"{COLOR_RED}Error: 'users.json' file not found.{COLOR_RESET}")
    except json.JSONDecodeError:
        print(f"{COLOR_RED}Error: 'users.json' contains invalid JSON.{COLOR_RESET}")
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
            print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")
            print(f"{COLOR_YELLOW}ID: {user['id']}{COLOR_RESET} "
                  f"{COLOR_GREEN}Name: {user['name']}{COLOR_RESET}, "
                  f"Age: {user['age']} "
                  f"{COLOR_MAGENTA}Email: {user.get('email', 'N/A')}{COLOR_RESET}")
            print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")
    else:
        print(f"{COLOR_RED}No users found with that name.{COLOR_RESET}")


def filter_by_age(age):
    """
    Filters and prints users whose age matches the given input.

    Args:
        age (int): Age to filter users by.
    """
    users = load_users()
    if not users:
        return

    filtered_users = [user for user in users if user["age"] == age]

    if filtered_users:
        for user in filtered_users:
            print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")
            print(f"{COLOR_YELLOW}ID: {user['id']}{COLOR_RESET} "
                  f"{COLOR_GREEN}Name: {user['name']}{COLOR_RESET}, "
                  f"Age: {user['age']} "
                  f"{COLOR_MAGENTA}Email: {user.get('email', 'N/A')}{COLOR_RESET}")
            print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")
    else:
        print(f"{COLOR_RED}No users found with that age.{COLOR_RESET}")


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
        user for user in users if user.get("email", "").lower() == email.lower()
    ]

    if filtered_users:
        for user in filtered_users:
            print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")
            print(f"{COLOR_YELLOW}ID: {user['id']}{COLOR_RESET} "
                  f"{COLOR_GREEN}Name: {user['name']}{COLOR_RESET}, "
                  f"Age: {user['age']} "
                  f"{COLOR_MAGENTA}Email: {user.get('email', 'N/A')}{COLOR_RESET}")
            print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")
    else:
        print(f"{COLOR_RED}No users found with that email.{COLOR_RESET}")

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
    print(f"{COLOR_CYAN}================================================={COLOR_RESET}")
    print(f"{COLOR_GREEN}        Welcome to the User Filter Tool          {COLOR_RESET}")
    print(f"{COLOR_CYAN}=================================================\n{COLOR_RESET}")
    valid_options = ("name", "age", "email")
    filter_option = input(
        f"{COLOR_YELLOW}What would you like to filter by? "
        f"(name / age / email): {COLOR_RESET}"
    ).strip().lower()

    if filter_option not in valid_options:
        print(f"{COLOR_RED}Invalid filter option. Supported: name, age, email."
              f"{COLOR_RESET}")
    elif filter_option == "name":
        while True:
            name_to_search = input(
                f"{COLOR_YELLOW}Enter a name to filter users: {COLOR_RESET}"
            ).strip()
            if name_to_search:
                filter_users_by_name(name_to_search)
                break
            else:
                print(f"{COLOR_RED}Name cannot be empty. Please enter a valid name."
                      f"{COLOR_RESET}")
    elif filter_option == "age":
        while True:
            age_input = input(
                f"{COLOR_YELLOW}Enter an age to filter users: {COLOR_RESET}"
            ).strip()
            if not age_input:
                print(f"{COLOR_RED}Age cannot be empty. Please enter a valid number."
                      f"{COLOR_RESET}")
                continue
            if not age_input.isdigit():
                print(f"{COLOR_RED}Invalid age! Please enter a number."
                      f"{COLOR_RESET}")
                continue

            age_to_search = int(age_input)
            if age_to_search < 0:
                print(f"{COLOR_RED}Age must be a positive number.{COLOR_RESET}")
                continue

            filter_by_age(age_to_search)
            break
    elif filter_option == "email":
        while True:
            email_to_search = input(
                f"{COLOR_YELLOW}Enter an email to filter users: {COLOR_RESET}"
            ).strip()
            if not email_to_search:
                print(f"{COLOR_RED}Email cannot be empty.{COLOR_RESET}")
                continue
            if not is_valid_email(email_to_search):
                print(f"{COLOR_RED}Invalid email format. Try again.{COLOR_RESET}")
                continue

            filter_by_email(email_to_search)
            break
