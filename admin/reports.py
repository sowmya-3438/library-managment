from database import get_connection


def view_reports():

    print("\nLIBRARY REPORTS ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:

        
        # 1. TOTAL USERS
        

        cursor.execute("""
            SELECT COUNT(*)
            FROM users
        """)

        total_users = cursor.fetchone()[0]


        
        # 2. TOTAL BOOKS
        

        cursor.execute("""
            SELECT COUNT(*)
            FROM books
        """)

        total_books = cursor.fetchone()[0]



        # 3. TOTAL BOOK COPIES
        

        cursor.execute("""
            SELECT COALESCE(SUM(quantity), 0)
            FROM books
        """)

        total_copies = cursor.fetchone()[0]


        
        # 4. TOTAL ISSUED BOOKS
        

        cursor.execute("""
            SELECT COUNT(*)
            FROM book_issues
        """)

        total_issued = cursor.fetchone()[0]


        
        # 5. CURRENTLY ISSUED BOOKS
        

        cursor.execute("""
            SELECT COUNT(*)
            FROM book_issues
            WHERE issue_status = 'Issued'
        """)

        currently_issued = cursor.fetchone()[0]


        
        # 6. TOTAL RETURNED BOOKS
    

        cursor.execute("""
            SELECT COUNT(*)
            FROM book_returns
        """)

        total_returns = cursor.fetchone()[0]


        
        # 7. TOTAL FINES


        cursor.execute("""
            SELECT COALESCE(SUM(fine_amount), 0)
            FROM fines
        """)

        total_fine_amount = cursor.fetchone()[0]


        
        # 8. UNPAID FINES


        cursor.execute("""
            SELECT COALESCE(SUM(fine_amount), 0)
            FROM fines
            WHERE fine_status = 'Unpaid'
        """)

        unpaid_fines = cursor.fetchone()[0]


        # DISPLAY REPORT
        

        
        print(" \n LIBRARY REPORTS")
        

        print("Total Users              :", total_users)
        print("Total Different Books    :", total_books)
        print("Total Book Copies        :", total_copies)
        print("Total Book Issues        :", total_issued)
        print("Currently Issued Books   :", currently_issued)
        print("Total Book Returns       :", total_returns)
        print("Total Fine Amount        :", total_fine_amount)
        print("Unpaid Fine Amount       :", unpaid_fines)

        

    except Exception as e:

        connection.rollback()

        print("Error generating report:", e)

    finally:

        cursor.close()
        connection.close()
