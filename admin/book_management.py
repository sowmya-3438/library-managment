from database import books


def add_book():

    name = input("Enter book name: ")
    author = input("Enter author: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))

    book = {
        "id": len(books) + 1,
        "name": name,
        "author": author,
        "category": category,
        "quantity": quantity,
        "available": quantity
    }

    books.append(book)

    print("Book was added successfully")


def view_books():

    if len(books) == 0:
        print("No  books was available")
        return

    for book in books:

        
        print("ID:", book["id"])
        print("Name:", book["name"])
        print("Author:", book["author"])
        print("Category:", book["category"])
        print("Quantity:", book["quantity"])
        print("Available:", book["available"])


def update_book():

    book_id = int(input("Enter your book ID: "))

    for book in books:

        if book["id"] == book_id:

            book["name"] = input("Enter book name: ")
            book["author"] = input("Enter author: ")
            book["category"] = input("Enter category: ")

            print("Book updated successfully")
            return

    print("Book not found")


def delete_book():

    book_id = int(input("Enter book ID: "))

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            print("Book was deleted successfully")
            return

    print("Book not found")