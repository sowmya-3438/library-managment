from librarian.book_management import add_book, view_books, update_book
from librarian.issue_book import issue_book
from librarian.return_book import return_book
from librarian.fine_management import add_fine, view_fines
from librarian.search_books import search_book
from librarian.history import view_history


def librarian_menu():

    while True:

        print("\n LIBRARIAN ")
        print("1. Book Management")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Fine Management")
        print("5. Search Books")
        print("6. View History")
        print("7. Logout")

        choice = input("Enter choice: ")

        if choice == "1":

            print("\n1. Add Book")
            print("2. View Books")
            print("3. Update Book")

            option = input("Enter choice: ")

            if option == "1":
                add_book()

            elif option == "2":
                view_books()

            elif option == "3":
                update_book()

        elif choice == "2":
            issue_book()

        elif choice == "3":
            return_book()

        elif choice == "4":

            print("\n1. Add Fine")
            print("2. View Fines")

            option = input("Enter choice: ")

            if option == "1":
                add_fine()

            elif option == "2":
                view_fines()

        elif choice == "5":
            search_book()

        elif choice == "6":
            view_history()

        elif choice == "7":
            print("Librarian logged out")
            break

        else:
            print("Invalid choice")