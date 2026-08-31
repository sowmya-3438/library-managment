from database import issued_books, returned_books

def view_history():

    print("\n LIBRARY HISTORY ")

    print("\nISSUED BOOKS ")
    
    if issued_books:
        for record in issued_books:
            print("Username:", record["username"])
            print("Book ID:", record["book_id"])         
    else:
        print("No issued book history found.")
    print("\n RETURNED BOOKS ")

    if returned_books:
        for record in returned_books:
            print("Username:", record["username"])
            print("Book ID:", record["book_id"])
        
    else:
        print("No returned book history found.")


def view_my_history(username):

    print("\n MY HISTORY ")
    found = False
    print("\n ISSUED BOOKS ")

    for record in issued_books:
        if record["username"] == username:
            print("Book ID:", record["book_id"])
            found = True
    print("\n RETURNED BOOKS ")
    for record in returned_books:
        if record["username"] == username:
            print("Book ID:", record["book_id"])
            found = True
    if not found:
        print("No history found.")