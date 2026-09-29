from database import get_connection


def add_book():

    print("\nADD BOOK")

    book_name = input("Enter book name: ")
    author = input("Enter author: ")
    category_id = int(input("Enter category ID: "))
    isbn = input("Enter ISBN: ")
    publisher = input("Enter publisher: ")
    publication_year = int(input("Enter publication year: "))
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:

        # Check category
        cursor.execute(
            """
            SELECT category_id, category_name
            FROM categories
            WHERE category_id = %s
            """,
            (category_id,)
        )

        category = cursor.fetchone()

        if category is None:

            print("\nInvalid category ID.")
            print("Available categories:")

            cursor.execute(
                """
                SELECT category_id, category_name
                FROM categories
                ORDER BY category_id
                """
            )

            categories = cursor.fetchall()

            for cat in categories:
                print(f"{cat[0]} - {cat[1]}")

            return

        query = """
            INSERT INTO books
            (
                book_name,
                author,
                category_id,
                isbn,
                publisher,
                publication_year,
                quantity,
                available_quantity,
                price
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                book_name,
                author,
                category_id,
                isbn,
                publisher,
                publication_year,
                quantity,
                quantity,
                price
            )
        )

        connection.commit()

        print("\nBook added successfully.")

    except Exception as e:

        connection.rollback()
        print("Error:", e)

    finally:

        cursor.close()
        connection.close()

# VIEW BOOKS


def view_books():

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            b.book_id,
            b.book_name,
            b.author,
            c.category_name,
            b.isbn,
            b.publisher,
            b.publication_year,
            b.quantity,
            b.available_quantity,
            b.price
        FROM books b
        JOIN categories c
            ON b.category_id = c.category_id
        ORDER BY b.book_id
    """

    try:

        cursor.execute(query)

        books = cursor.fetchall()

        print("\n ALL BOOKS")
       
        
        if not books:
            print("No books found.")
            return

        for book in books:

            print("\nBook ID:", book["book_id"])
            print("Book Name:", book["book_name"])
            print("Author:", book["author"])
            print("Category:", book["category_name"])
            print("ISBN:", book["isbn"])
            print("Publisher:", book["publisher"])
            print("Publication Year:", book["publication_year"])
            print("Quantity:", book["quantity"])
            print("Available:", book["available_quantity"])
            print("Price:", book["price"])

            print("-" * 80)

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()



# UPDATE BOOK


def update_book():

    print("\nUPDATE BOOK")

    book_id = int(input("Enter book ID to update: "))

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(
            """
            SELECT *
            FROM books
            WHERE book_id = %s
            """,
            (book_id,)
        )

        book = cursor.fetchone()

        if book is None:
            print("Book not found.")
            return

        print("\nCurrent Book Details")
        print("Book Name:", book["book_name"])
        print("Author:", book["author"])
        print("Quantity:", book["quantity"])
        print("Available:", book["available_quantity"])
        print("Price:", book["price"])

        book_name = input("Enter new book name: ")
        author = input("Enter new author: ")
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))

        old_quantity = book["quantity"]
        old_available = book["available_quantity"]

        # Number of books currently borrowed
        borrowed_quantity = old_quantity - old_available

        if quantity < borrowed_quantity:

            print(
                "Quantity cannot be less than "
                "currently borrowed copies."
            )

            return

        new_available = quantity - borrowed_quantity

        cursor.execute(
            """
            UPDATE books
            SET
                book_name = %s,
                author = %s,
                quantity = %s,
                available_quantity = %s,
                price = %s
            WHERE book_id = %s
            """,
            (
                book_name,
                author,
                quantity,
                new_available,
                price,
                book_id
            )
        )

        connection.commit()

        print("Book updated successfully.")

    except Exception as e:

        connection.rollback()
        print("Error:", e)

    finally:

        cursor.close()
        connection.close()

# DELETE BOOK


def delete_book():

    print("\nDELETE BOOK")

    book_id = int(input("Enter book ID to delete: "))

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            DELETE FROM books
            WHERE book_id = %s
            """,
            (book_id,)
        )

        if cursor.rowcount == 0:

            print("Book not found.")

        else:

            connection.commit()

            print("Book deleted successfully.")

    except Exception as e:

        connection.rollback()

        print("Cannot delete book.")
        print("Error:", e)

    finally:

        cursor.close()
        connection.close()
