from member.search_books import search_books
from member.view_books import view_books
from member.borrow_book import borrow_book
from member.return_book import return_book
from member.history import view_my_history


def member_menu(user_id):
    print("Logged in User ID:", user_id)


    while True:
        print("\n MEMBER MENU")
        print("1. Search Books")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View History")
        print("7. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            search_books()

        elif choice == "2":
            view_books()

        elif choice == "3":
            borrow_book(user_id)

        elif choice == "4":
            return_book(user_id)

        elif choice == "5":
            search_books()

        elif choice == "6":
            view_my_history(user_id)

        elif choice == "7":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice.")
