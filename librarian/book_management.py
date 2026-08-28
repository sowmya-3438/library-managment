from database import books


def add_book():

    name = input("Enter book name: ")
    author = input("Enter author: ")
    category = input("Enter category: ")

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Enter a valid quantity")
        return

    book = {
        "id": len(books) + 1,
        "name": name,
        "author": author,
        "category": category,
        "quantity": quantity,
        "available": quantity
    }

    books.append(book)

    print("Book added successfully")


def view_books():

    print("\n BOOKS ")

    if not books:
        print("No books available")
        return

    for book in books:

        
        print("ID:", book["id"])
        print("Name:", book["name"])
        print("Author:", book["author"])
        print("Category:", book["category"])
        print("Available:", book["available"])


def update_book():

    try:
        book_id = int(input("Enter book ID: "))
    except ValueError:
        print("Invalid book ID")
        return

    for book in books:

        if book["id"] == book_id:

            book["name"] = input("Enter new book name: ")
            book["author"] = input("Enter new author: ")

            print("Book updated successfully")
            return

    print("Book not found")