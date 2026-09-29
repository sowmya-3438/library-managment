# Library Management System

A menu-driven library management application built with Python and MySQL. Users log in with a username and password, and the application opens a menu based on their role: **Admin**, **Librarian**, or **Member**.

## Features

- Role-based login and menus
- Manage library users, books, and categories
- Search and view books and availability
- Issue, borrow, and return books
- View borrowing and return history
- View reports and manage fines

Available operations depend on the signed-in user's role and the menu modules in the project.

## Technology

- Python 3
- MySQL
- `mysql-connector-python`

## Project layout

```text
library managment system/
├── main.py                 # Application entry point and role routing
├── login.py                # Authenticates a user against MySQL
├── database.py             # Creates MySQL connections
├── test_connection.py      # Checks the configured MySQL connection
├── admin/                  # Admin menu and user, book, category, report, history modules
├── librarian/              # Librarian menu and book, issue, return, fine, search, history modules
└── member/                 # Member menu and borrow, return, search, view, history modules
```

The SQL setup and example queries are in the separate file `LIBRARY MANAGEMENT QUERY'S.sql`.

## Requirements

1. Install Python 3 and MySQL Server.
2. Install the MySQL connector:

   ```bash
   python -m pip install mysql-connector-python
   ```

3. Create and populate the database by running `LIBRARY MANAGEMENT QUERY'S.sql` in a MySQL client such as MySQL Workbench. The script creates the `library_management` database, tables, sample users/books/loan records, and example SQL objects and queries.
4. Ensure the database connection details in `database.py` match your local MySQL setup. The current configuration is:

   ```python
   host="localhost"
   user="root"
   password="root"
   database="library_management"
   ```

   Change the host, username, password, or database name if your MySQL configuration differs.

## Run

Open a terminal in the project directory and check the database connection:

```bash
python test_connection.py
```

If the connection succeeds, start the application:

```bash
python main.py
```

Choose **Login**, then enter a username and password that exist in the `users` table. The application checks the user's role and routes to the matching menu. Choose **Exit** to close the program.

## Sample accounts

The supplied SQL setup inserts these example accounts. These passwords are stored as plain text by the current application, so use them only for local demonstration and change them before using the system with real accounts.

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| Librarian | `librarian` | `lib123` |
| Member | `student` | `stu123` |
| Member | `rahul` | `rahul123` |
| Member | `sneha` | `sneha123` |

## Database tables

The SQL setup defines tables for users, categories, books, book issues, returns, fines, and audit history. It also includes sample views, a stored procedure, a trigger, indexes, and query examples for catalog searches, availability, borrowing, overdue items, and reports.

## Notes

- Run the SQL setup before starting the Python application; `database.py` connects to an existing database and does not create tables.
- The SQL script contains setup, sample data, and practice queries. Review it before running against a database with data you need to keep.
- Login currently compares the submitted password directly with the `password` column. Password hashing and secure secret configuration are not implemented in the supplied code.
