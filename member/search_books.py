from database import books


def search_book():

    value = input("Enter book name or author: ").lower()

    found = False

    for book in books:

        if value in book["name"].lower() or value in book["author"].lower():

            
            print("ID:", book["id"])
            print("Name:", book["name"])
            print("Author:", book["author"])
            print("Category:", book["category"])
            print("Available:", book["available"])

            found = True

    if not found:
        print("Book not found")
