from database import get_connection


def view_history():

    print("\nLIBRARY HISTORY ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

    
        # ISSUED BOOKS
        
        print("\n ISSUED BOOKS ")

        query = """
            SELECT
                bi.issue_id,
                u.full_name,
                b.book_name,
                bi.issue_date,
                bi.due_date,
                bi.issue_status
            FROM book_issues bi
            JOIN users u
                ON bi.user_id = u.user_id
            JOIN books b
                ON bi.book_id = b.book_id
            ORDER BY bi.issue_id
        """

        cursor.execute(query)

        issued_books = cursor.fetchall()

        if issued_books:
            for row in issued_books:
                print(
                    "Issue ID:", row[0],
                    "| User:", row[1],
                    "| Book:", row[2],
                    "| Issue Date:", row[3],
                    "| Due Date:", row[4],
                    "| Status:", row[5]
                )
        else:
            print("No issued books found.")

        
        # RETURNED BOOKS
        
        print("\nRETURNED BOOKS ")

        query = """
            SELECT
                br.return_id,
                u.full_name,
                b.book_name,
                br.return_date,
                br.return_condition,
                br.remarks
            FROM book_returns br
            JOIN book_issues bi
                ON br.issue_id = bi.issue_id
            JOIN users u
                ON bi.user_id = u.user_id
            JOIN books b
                ON bi.book_id = b.book_id
            ORDER BY br.return_id
        """

        cursor.execute(query)

        returned_books = cursor.fetchall()

        if returned_books:
            for row in returned_books:
                print(
                    "Return ID:", row[0],
                    "| User:", row[1],
                    "| Book:", row[2],
                    "| Return Date:", row[3],
                    "| Condition:", row[4],
                    "| Remarks:", row[5]
                )
        else:
            print("No returned books found.")

    except Exception as e:
        print("Error displaying history:", e)

    finally:
        cursor.close()
        connection.close()
