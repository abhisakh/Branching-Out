# 🌿 Branching Out
<img width="928" height="294" alt="1" src="https://github.com/user-attachments/assets/b75cd24e-74c0-43b6-b32c-86ba893cc58f" />


Branching Out is a lightweight, interactive Python CLI tool that allows you to search and filter user data stored in a JSON file.
It supports filtering by name, age, or email, and includes robust input validation, error handling, and colorized terminal output — all written in clean, PEP 8–compliant Python.

---

## ✨ Features

### 🔍 Search & Filter

- Filter users by name, age, or email

### 🧠 Smart Matching

- Case-insensitive matching for names and emails

### 🧰 Robust Validation

- Checks email format and validates age inputs

### ⚡ Error Handling

- Gracefully handles missing files, invalid JSON, and user mistakes

### 🎨 Colorized Output

- Friendly, readable results in ANSI-supported terminals

### 🪶 PEP 8 + PEP 257 Compliant

- Code formatted with a strict 80-character line limit

--- 

## 📂 Project Structure
```Bash

BranchingOut/
│
├── users.json          # JSON dataset (example below)
├── branching_out.py    # Main Python script
└── README.md           # Project documentation

```
---

## 🧾 Example users.json
```Bash
[
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 30, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 25, "email": "charlie@example.com"}
]
```
---
## 🚀 Usage
### 1. Run the Script
```Bash
python branching_out.py

```
### 2. Choose a Filter Option
When prompted, select one of:
```Bash
name / age / email

```

### 3. Enter a Search Value
Examples:
Alice → filters users by name (case-insensitive)
25 → filters users by age
bob@example.com → filters users by email
```Bash
=================================================
        Welcome to Branching Out
=================================================

What would you like to filter by? (name / age / email): name
Enter name: Alice
**************************************************
ID: 1 Name: Alice, Age: 25 Email: alice@example.com
**************************************************

```
---
## ⚙️ Requirements
- Python 3.7+
- Works on Linux, macOS, and Windows (ANSI-compatible terminals)
- ✅ Uses only standard libraries: json, re, sys
---

## ⚠️ Error & Input Handling
Branching Out includes comprehensive error handling and user input validation
to prevent crashes and guide the user with clear, color-coded feedback.

```Bash
| Scenario                                  | Behavior                                        |
| ----------------------------------------- | ----------------------------------------------- |
| **Missing `users.json`**                  | Displays: `Error: 'users.json' not found.`      |
| **Corrupted JSON**                        | Displays: `Error parsing JSON: <error message>` |
| **Empty Input (name/email/age)**          | Prompts again until valid input is entered      |
| **Invalid Age (non-numeric or negative)** | Rejects and re-prompts user                     |
| **Invalid Email Format**                  | Checked with regex; invalid ones rejected       |
| **No Matching Results**                   | Prints `No users found with that <field>.`      |
| **Keyboard Interrupt (Ctrl+C)**           | Gracefully exits with no traceback              |

```

Example of input validation message:
```Bash
Enter an age to filter users: abc
Invalid age! Please enter a number.
```
---
## 🧹 Code Style & Linting

This project follows PEP 8 and PEP 257 standards.

To check style automatically with flake8:
```Bash
pip install flake8
flake8 --max-line-length=80 branching_out.py

```
Optional .flake8 configuration:
```Bash
[flake8]
max-line-length = 80
ignore = E203, W503

```
---
## 📜 License

Released under the MIT License.
You’re free to use, modify, and distribute it for personal or educational projects.

---
## 🙋‍♂️ Author
**Abhisakh Sarma**
GitHub: [https://github.com/abhisakh](https://github.com/abhisakh)

_Contributions and feedback are always welcome!_
