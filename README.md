<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 20px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
        }
        code {
            background: #f4f4f4;
            border: 1px solid #ddd;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background: #f4f4f4;
            border: 1px solid #ddd;
            padding: 10px;
            overflow-x: auto;
            border-radius: 8px;
        }
        ul {
            list-style: disc inside none;
        }
        li {
            margin-bottom: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>User Management Application</h1>
        <p>This application is a basic user management system built in Python. It allows users to register, log in, log out, and view their identity. All user data is stored in a <code>users.json</code> file.</p>

        <h2>Features</h2>
        <ul>
            <li><strong>Register:</strong> Create a new user by providing a username, password, and email.</li>
            <li><strong>Login:</strong> Log in using the registered username and password.</li>
            <li><strong>Identity:</strong> View the currently logged-in user's information.</li>
            <li><strong>Logout:</strong> Log out from the application.</li>
            <li><strong>Persistent Storage:</strong> User data is saved to a JSON file (<code>users.json</code>).</li>
        </ul>

        <h2>Usage</h2>
        <p>Run the Python script and follow the on-screen menu options:</p>
        <pre>
Menü**********************************************
1- Register
2- Login
3- Logout
4- Identity
5- Exit
Seçiminiz: 
        </pre>

        <h2>Code Structure</h2>
        <ul>
            <li><code>User</code> class: Represents a user with <code>username</code>, <code>password</code>, and <code>email</code> attributes.</li>
            <li><code>UserRepository</code> class: Manages user operations, including registration, login, logout, and identity retrieval.</li>
            <li><code>users.json</code>: Stores user data persistently.</li>
        </ul>

        <h2>How to Run</h2>
        <ol>
            <li>Make sure you have Python 3 installed on your machine.</li>
            <li>Save the script to a file (e.g., <code>user_management.py</code>).</li>
            <li>Run the script using the command:
                <pre>python user_management.py</pre>
            </li>
            <li>Follow the menu options to register, log in, or manage users.</li>
        </ol>

        <h2>Example JSON File</h2>
        <p>The <code>users.json</code> file will look something like this after users are registered:</p>
        <pre>
[
    "{\"username\": \"user1\", \"password\": \"pass1\", \"email\": \"user1@example.com\"}",
    "{\"username\": \"user2\", \"password\": \"pass2\", \"email\": \"user2@example.com\"}"
]
        </pre>

        <h2>Notes</h2>
        <ul>
            <li>Ensure the <code>users.json</code> file is in the same directory as the script.</li>
            <li>If the file does not exist, it will be created automatically after the first user registration.</li>
        </ul>

        <p>Happy coding!</p>
    </div>
</body>
</html>
