from database import get_connection


def view_my_history(user_id):

    print("\n MY LIBRARY HISTORY ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        
        # BORROWING HISTORY
    

        query = """
            SELECT
                bi.issue_id,
                b.book_name,
                bi.issue_date,
                bi.due_date,
                bi.issue_status
            FROM book_issues bi
            JOIN books b
                ON bi.book_id = b.book_id
            WHERE bi.user_id = %s
            ORDER BY bi.issue_id DESC
        """

        cursor.execute(query, (user_id,))

        history = cursor.fetchall()

        if history:

            print("\nISSUED BOOKS")

            for row in history:

                print(
                    "Issue ID:", row[0],
                    "| Book:", row[1],
                    "| Issue Date:", row[2],
                    "| Due Date:", row[3],
                    "| Status:", row[4]
                )

        else:

            print("No borrowing history found.")

        
        # RETURN HISTORY
        

        query = """
            SELECT
                br.return_id,
                b.book_name,
                br.return_date,
                br.return_condition,
                br.remarks
            FROM book_returns br
            JOIN book_issues bi
                ON br.issue_id = bi.issue_id
            JOIN books b
                ON bi.book_id = b.book_id
            WHERE bi.user_id = %s
            ORDER BY br.return_id DESC
        """

        cursor.execute(query, (user_id,))

        returns = cursor.fetchall()

        if returns:

            print("\nRETURNED BOOKS")

            for row in returns:

                print(
                    "Return ID:", row[0],
                    "| Book:", row[1],
                    "| Return Date:", row[2],
                    "| Condition:", row[3],
                    "| Remarks:", row[4]
                )

        else:

            print("\nNo returned books found.")

    except Exception as e:

        print("Error displaying my history:", e)

    finally:

        cursor.close()
        connection.close()
