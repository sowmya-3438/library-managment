from database import users, books, issued_books, returned_books, fines


def view_reports():

    print("\nLIBRARY REPORT ")

    print("Total Users:", len(users))
    print("Total Books:", len(books))
    print("Issued Books:", len(issued_books))
    print("Returned Books:", len(returned_books))
    print("Fine Records:", len(fines))

    total_books = 0
    available_books = 0

    for book in books:

        total_books += book["quantity"]
        available_books += book["available"]

    print("Total Book Copies:", total_books)
    print("Available Copies:", available_books)