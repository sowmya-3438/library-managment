from database import issued_books, returned_books


def view_history():

    print("\nIssued Books")

    for record in issued_books:

        print("Username:", record["username"])
        print("Book ID:", record["book_id"])

    print("\nReturned Books")

    for record in returned_books:

        print("Username:", record["username"])
        print("Book ID:", record["book_id"])


def view_my_history(username):

    print("\nMy History")

    found = False

    for record in issued_books:

        if record["username"] == username:

            print("Issued Book ID:", record["book_id"])
            found = True

    for record in returned_books:

        if record["username"] == username:

            print("Returned Book ID:", record["book_id"])
            found = True

    if not found:
        print("No history found")
