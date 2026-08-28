from admin.user_management import add_user, view_users, delete_user
from admin.book_management import add_book, view_books, update_book, delete_book
from admin.category_management import add_category, view_categories, delete_category
from admin.reports import view_reports
from admin.history import view_history


def admin_menu():

    while True:

        print("\nADMIN ")
        print("1. User Management")
        print("2. Book Management")
        print("3. Category Management")
        print("4. Reports")
        print("5. View History")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":

            print("\n User Management ")
            print("1. Add User")
            print("2. View Users")
            print("3. Delete User")

            option = input("Enter your choice: ")

            if option == "1":
                add_user()

            elif option == "2":
                view_users()

            elif option == "3":
                delete_user()

            else:
                print("Invalid choice")

        elif choice == "2":

            print("\n Book Management ")
            print("1. Add Book")
            print("2. View Books")
            print("3. Update Book")
            print("4. Delete Book")

            option = input("Enter your choice: ")

            if option == "1":
                add_book()

            elif option == "2":
                view_books()

            elif option == "3":
                update_book()

            elif option == "4":
                delete_book()

            else:
                print("Invalid choice")

        elif choice == "3":

            print("\n-Category Management ")
            print("1. Add Category")
            print("2. View Categories")
            print("3. Delete Category")

            option = input("Enter your choice: ")

            if option == "1":
                add_category()

            elif option == "2":
                view_categories()

            elif option == "3":
                delete_category()

            else:
                print("Invalid choice")

        elif choice == "4":
            view_reports()

        elif choice == "5":
            view_history()

        elif choice == "6":
            print("Admin was log out")
            break

        else:
            print("Invalid your choice")