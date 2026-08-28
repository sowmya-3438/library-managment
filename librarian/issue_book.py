from database import books, issued_books


def issue_book(username=None):

    if username is None:
        username = input("Enter member username: ")

    book_id = int(input("Enter book ID: "))

    for book in books:

        if book["id"] == book_id:

            if book["available"] <= 0:
                print("Book is not available")
                return

            issued_books.append({
                "username": username,
                "book_id": book_id
            })

            book["available"] -= 1

            print("Book issued successfully")
            return

    print("Book not found")