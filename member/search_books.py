from database import get_connection


def search_books():

    print("\nSEARCH BOOK")

    search = input("Enter book title or author: ").strip()

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    query = """
        SELECT *
        FROM books
        WHERE book_name LIKE %s
           OR author LIKE %s
    """

    search_value = "%" + search + "%"

    try:
        cursor.execute(query, (search_value, search_value))
        books = cursor.fetchall()

        if not books:
            print("\nNo books found.")
            return

        print("\nSEARCH RESULTS")

        for book in books:
            print(book)

        

    except Exception as e:
        print("Error searching books:", e)

    finally:
        cursor.close()
        connection.close()
