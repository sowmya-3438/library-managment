from member.search_books import search_book
from member.view_books import view_books
from member.borrow_book import borrow_book
from member.return_book import return_book
from member.history import view_my_history


def member_menu(username):

    while True:

        print("\n MEMBER ")
        print("1. Search Books")
        print("2. View Books")
        print("3. Issue/Borrow Book")
        print("4. Return Book")
        print("5. View My History")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            search_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            borrow_book(username)

        elif choice == "4":
            return_book(username)

        elif choice == "5":
            view_my_history(username)

        elif choice == "6":
            print("Member logged out")
            break

        else:
            print("Invalid choice")
