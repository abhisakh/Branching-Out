import json


def filter_users_by_name(name):
    """
    Filters and prints users from users.json whose name matches the given name.

    Args:
        name (str): The name to filter users by (case-insensitive).
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users
        if user["name"].lower() == name.lower()
    ]

    for user in filtered_users:
        print(user)


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

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    """
    Entry point for the user filtering script.
    Prompts the user to choose a filter option ('name' or 'age'),
    then asks for the filter value and displays matching users.
    """
    filter_option = input(
        "What would you like to filter by? "
        "(Currently, only 'name' and 'age' are supported): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input(
            "Enter a name to filter users: "
        ).strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        while True:
            try:
                age_to_search = int(input(
                    "Enter an age to filter users: "
                ).strip())
                filter_by_age(age_to_search)
                break
            except ValueError:
                print("Invalid age! Please enter a number.")

    else:
        print("Filtering by that option is not yet supported.")
