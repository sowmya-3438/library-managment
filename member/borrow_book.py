from database import books, issued_books


def borrow_book(username):

    print("\n BORROW BOOK ")

    if not books:
        print("No books available")
        return

    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("Enter a valid Book ID")
        return

    for book in books:

        if book["id"] == book_id:

            if book["available"] <= 0:
                print("Book is not available")
                return

            for record in issued_books:

                if record["username"] == username and record["book_id"] == book_id:
                    print("You already borrowed this book")
                    return

            book["available"] -= 1

            issued_books.append({
                "username": username,
                "book_id": book["id"],
                "book_name": book["name"]
            })

            print("Book borrowed successfully")
            return

    print("Book not found")