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
    Load users from users.json with error handling.

    Returns:
        list: A list of user dictionaries or an empty list if an error occurs.
    """
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{COLOR_RED}Error: 'users.json' not found.{COLOR_RESET}")
    except json.JSONDecodeError as err:
        print(f"{COLOR_RED}Error parsing JSON: {err}{COLOR_RESET}")
    return []


def print_user(user):
    """Print a single user's information in formatted color output."""
    print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")
    print(
        f"{COLOR_YELLOW}ID: {user.get('id', 'N/A')}{COLOR_RESET} "
        f"{COLOR_GREEN}Name: {user.get('name', 'N/A')}{COLOR_RESET}, "
        f"Age: {user.get('age', 'N/A')} "
        f"{COLOR_MAGENTA}Email: {user.get('email', 'N/A')}{COLOR_RESET}"
    )
    print(f"{COLOR_CYAN}{'*' * 50}{COLOR_RESET}")


def filter_users(field, value, case_insensitive=False):
    """
    Filter users by field and value, printing matching results.

    Args:
        field (str): Field to filter by (e.g., 'name', 'age', 'email').
        value (Any): Value to match.
        case_insensitive (bool): Whether to match case-insensitively.
    """
    users = load_users()
    if not users:
        return

    if case_insensitive:
        filtered = [
            u for u in users
            if str(u.get(field, "")).lower() == str(value).lower()
        ]
    else:
        filtered = [u for u in users if u.get(field) == value]

    if filtered:
        for user in filtered:
            print_user(user)
    else:
        print(f"{COLOR_RED}No users found with that {field}.{COLOR_RESET}")


def is_valid_email(email):
    """Return True if an email address has a valid basic structure."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def main():
    """Entry point: interactively filter users by name, age, or email."""
    print(f"{COLOR_CYAN}{'=' * 49}{COLOR_RESET}")
    print(f"{COLOR_GREEN}   Welcome to the User Filter Tool   {COLOR_RESET}")
    print(f"{COLOR_CYAN}{'=' * 49}\n{COLOR_RESET}")

    valid_options = ("name", "age", "email")
    prompt = (
        f"{COLOR_YELLOW}Filter by (name / age / email): {COLOR_RESET}"
    )
    filter_option = input(prompt).strip().lower()

    if filter_option not in valid_options:
        print(
            f"{COLOR_RED}Invalid option. Choose name, age, or email."
            f"{COLOR_RESET}"
        )
        return

    if filter_option == "name":
        while True:
            name = input(
                f"{COLOR_YELLOW}Enter name: {COLOR_RESET}"
            ).strip()
            if name:
                filter_users("name", name, case_insensitive=True)
                break
            print(f"{COLOR_RED}Name cannot be empty.{COLOR_RESET}")

    elif filter_option == "age":
        while True:
            age_input = input(
                f"{COLOR_YELLOW}Enter age: {COLOR_RESET}"
            ).strip()
            if not age_input:
                print(f"{COLOR_RED}Age cannot be empty.{COLOR_RESET}")
                continue
            if not age_input.isdigit():
                print(f"{COLOR_RED}Please enter a valid number.{COLOR_RESET}")
                continue

            age = int(age_input)
            if age < 0:
                print(f"{COLOR_RED}Age must be positive.{COLOR_RESET}")
                continue

            filter_users("age", age)
            break

    elif filter_option == "email":
        while True:
            email = input(
                f"{COLOR_YELLOW}Enter email: {COLOR_RESET}"
            ).strip()
            if not email:
                print(f"{COLOR_RED}Email cannot be empty.{COLOR_RESET}")
                continue
            if not is_valid_email(email):
                print(f"{COLOR_RED}Invalid email format.{COLOR_RESET}")
                continue

            filter_users("email", email, case_insensitive=True)
            break


if __name__ == "__main__":
    main()