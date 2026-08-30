from database import books, issued_books, returned_books


def return_book(username=None):

    if username is None:
        username = input("Enter username: ")

    book_id = int(input("Enter book ID: "))

    for record in issued_books:

        if record["username"] == username and record["book_id"] == book_id:

            issued_books.remove(record)

            for book in books:

                if book["id"] == book_id:
                    book["available"] += 1

            returned_books.append({
                "username": username,
                "book_id": book_id
            })

            print("Book returned successfully")
            return

    print("Book record not found")
  
