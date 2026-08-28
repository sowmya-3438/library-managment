from database import users


def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:

        if user["username"] == username and user["password"] == password:

            print("Login successful")
            print("Welcome", user["name"])

            return user

    print("Invalid username or password")

    return None