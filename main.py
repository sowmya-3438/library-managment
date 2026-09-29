from login import login
from admin.admin_menu import admin_menu
from librarian.librarian_menu import librarian_menu
from member.member_menu import member_menu


def main():

    while True:

        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            user = login()

            if user:

                role = user["role"].lower()

                if role == "admin":
                    admin_menu()

                elif role == "librarian":
                    librarian_menu()

                elif role == "member":
                    member_menu(user["user_id"])

                else:
                    print("Invalid role")

        elif choice == "2":

            print("Thank you")
            break

        else:

            print("Invalid choice")


if __name__ == "__main__":
    main()