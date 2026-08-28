from database import users


def add_user():

    name = input("Enter name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (librarian/member): ").lower()

    if role not in ["librarian", "member"]:
        print("Invalid role")
        return

    for user in users:

        if user["username"] == username:
            print("Username already exists")
            return

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "username": username,
        "password": password,
        "role": role
    }

    users.append(new_user)

    print("User added successfully")


def view_users():

    print("\n USERS ")

    if not users:
        print("No users available")
        return

    for user in users:

        print("--------------------")
        print("ID       :", user["id"])
        print("Name     :", user["name"])
        print("Username :", user["username"])
        print("Role     :", user["role"])


def delete_user():

    username = input("Enter username: ")

    for user in users:

        if user["username"] == username:

            if user["role"] == "admin":
                print("Admin user cannot be deleted")
                return

            users.remove(user)

            print("User deleted successfully")
            return

    print("User not found")