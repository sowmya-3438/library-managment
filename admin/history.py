from database import issued_books, returned_books


def view_history():
    print("\nLIBRARY HISTORY ")

    print("\n HISTORY ")

    print("\nIssued Books")

    for record in issued_books:
        print(record)

    print("\nReturned Books")

    for record in returned_books:
        print(record)