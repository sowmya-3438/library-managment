from database import books


def view_books():

    print("\n AVAILABLE BOOKS ")

    if not books:
        print("No books available")
        return

    for book in books:

        
        print("Book ID   :", book["id"])
        print("Book Name :", book["name"])
        print("Author    :", book["author"])
        print("Category  :", book["category"])
        print("Available :", book["available"])