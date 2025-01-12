# User Management Application

This application is a basic user management system built in Python. It allows users to register, log in, log out, and view their identity. All user data is stored in a `users.json` file.

## Features

- **Register:** Create a new user by providing a username, password, and email.
- **Login:** Log in using the registered username and password.
- **Identity:** View the currently logged-in user's information.
- **Logout:** Log out from the application.
- **Persistent Storage:** User data is saved to a JSON file (`users.json`).

## Usage

Run the Python script and follow the on-screen menu options:
```
***********************Menü***********************
1- Register
2- Login
3- Logout
4- Identity
5- Exit
Seçiminiz:
```
## Code Structure

- `User` class: Represents a user with `username`, `password`, and `email` attributes.
- `UserRepository` class: Manages user operations, including registration, login, logout, and identity retrieval.
- `users.json`: Stores user data persistently.

## How to Run

1. Make sure you have Python 3 installed on your machine.
2. Save the script to a file (e.g., `user_management.py`).
3. Run the script using the command:

    ```bash
    python user_management.py
    ```

4. Follow the menu options to register, log in, or manage users.

## Example JSON File

The `users.json` file will look something like this after users are registered:

```json
[
    {
        "username": "user1",
        "password": "pass1",
        "email": "user1@example.com"
    },
    {
        "username": "user2",
        "password": "pass2",
        "email": "user2@example.com"
    }
]
```

## Notes

- Ensure the `users.json` file is in the same directory as the script.
- If the file does not exist, it will be created automatically after the first user registration.

Happy coding!
