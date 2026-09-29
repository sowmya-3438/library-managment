from database import get_connection


def add_category():

    print("\nADD CATEGORY")

    category_name = input("Enter category name: ")
    description = input("Enter description: ")

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    query = """
        INSERT INTO categories
        (category_name, description)
        VALUES (%s, %s)
    """

    try:
        cursor.execute(
            query,
            (category_name, description)
        )

        connection.commit()

        print("Category added successfully.")

    except Exception as e:

        connection.rollback()
        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


def view_categories():

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    query = """
        SELECT category_id, category_name, description
        FROM categories
        ORDER BY category_id
    """

    try:
        cursor.execute(query)

        categories = cursor.fetchall()

        print("\nCATEGORY LIST")

        if not categories:

            print("No categories found.")

        else:

            for category in categories:

                print(
                    f"ID: {category[0]}, "
                    f"Name: {category[1]}, "
                    f"Description: {category[2]}"
                )

    except Exception as e:

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


def delete_category():

    print("\nDELETE CATEGORY")

    category_id = int(input("Enter category ID to delete: "))

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:

        # Check whether category exists
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

            print("Category not found.")
            return

        # Check whether books use this category
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM books
            WHERE category_id = %s
            """,
            (category_id,)
        )

        book_count = cursor.fetchone()[0]

        if book_count > 0:

            print("\nCannot delete this category.")
            print(
                f"{book_count} book(s) are using "
                f"this category."
            )
            print(
                "Please move the books to another "
                "category first."
            )

            return

        # Delete category
        cursor.execute(
            """
            DELETE FROM categories
            WHERE category_id = %s
            """,
            (category_id,)
        )

        connection.commit()

        print("Category deleted successfully.")

    except Exception as e:

        connection.rollback()
        print("Error:", e)

    finally:

        cursor.close()
        connection.close()
