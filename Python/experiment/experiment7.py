import re

# Simulated database
users = []


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def is_strong_password(password):
    return (
        len(password) >= 8
        and any(char.isdigit() for char in password)
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
    )


def register_user(username, password, email):
    for user in users:
        if user['username'] == username:
            return False, 'Username already exists'

    if not is_valid_email(email):
        return False, 'Invalid email format'

    if not is_strong_password(password):
        return False, 'Password does not meet the requirements'

    user = {
        'username': username,
        'password': password,
        'email': email
    }
    users.append(user)

    return True, 'Registration successful'


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")

        success, message = register_user(username, password, email)
        if success:
            print("Registration successful")
        else:
            print("Registration failed:", message)


if __name__ == "__main__":
    main()
