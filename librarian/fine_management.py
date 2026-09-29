from database import get_connection


def add_fine():
    print("\nADD FINE")

    issue_id = int(input("Enter issue ID: "))
    fine_amount = float(input("Enter fine amount: "))
    reason = input("Enter reason: ")

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:
        # Get user_id and book_id from book_issues
        check_query = """
            SELECT user_id, book_id
            FROM book_issues
            WHERE issue_id = %s
        """

        cursor.execute(check_query, (issue_id,))
        issue = cursor.fetchone()

        if issue is None:
            print("Issue ID not found.")
            return

        user_id = issue[0]
        book_id = issue[1]

        query = """
            INSERT INTO fines
            (
                issue_id,
                user_id,
                fine_amount,
                reason,
                fine_status,
                paid_date,
                fine_reason,
                book_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            issue_id,
            user_id,
            fine_amount,
            reason,
            "Unpaid",
            None,
            reason,
            book_id
        )

        cursor.execute(query, values)
        connection.commit()

        print("Fine added successfully.")

    except Exception as e:
        connection.rollback()
        print("Error adding fine:", e)

    finally:
        cursor.close()
        connection.close()


def view_fines():

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    query = """
        SELECT
            fine_id,
            issue_id,
            user_id,
            book_id,
            fine_amount,
            reason,
            fine_status,
            paid_date
        FROM fines
        ORDER BY fine_id DESC
    """

    try:
        cursor.execute(query)
        fines = cursor.fetchall()

        if not fines:
            print("\nNo fines found.")
            return

        print("\n" + "=" * 100)
        print("                         FINE DETAILS")
        print("=" * 100)

        print(
            f"{'Fine ID':<10}"
            f"{'Issue ID':<10}"
            f"{'User ID':<10}"
            f"{'Book ID':<10}"
            f"{'Amount':<12}"
            f"{'Reason':<20}"
            f"{'Status':<12}"
            f"{'Paid Date':<12}"
        )

        print("-" * 100)

        for fine in fines:
            print(
                f"{fine[0]:<10}"
                f"{fine[1]:<10}"
                f"{fine[2]:<10}"
                f"{fine[3]:<10}"
                f"{fine[4]:<12}"
                f"{str(fine[5] or ''):<20}"
                f"{str(fine[6] or ''):<12}"
                f"{str(fine[7] or ''):<12}"
            )

        print("=" * 100)

    except Exception as e:
        print("Error viewing fines:", e)

    finally:
        cursor.close()
        connection.close()
