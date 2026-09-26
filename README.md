# Library Management System

A Python and MySQL based Library Management System designed to manage books, categories, users, librarians, members, borrowing, returning, fines, history, and reports.

## Features

* Admin management
* User management
* Book management
* Category management
* Librarian management
* Member management
* Book issue and return
* Fine management
* Library history
* Reports
* MySQL database integration

## Technologies Used

* Python
* MySQL
* MySQL Connector/Python
* Git & GitHub

## Project Structure

```text
LibraryManagementSystem/
│
├── admin/
│   ├── __init__.py
│   ├── admin_menu.py
│   ├── book_management.py
│   ├── category_management.py
│   ├── history.py
│   ├── reports.py
│   └── user_management.py
│
├── librarian/
│   ├── __init__.py
│   ├── librarian_menu.py
│   ├── book_management.py
│   ├── issue_book.py
│   ├── return_book.py
│   ├── fine_management.py
│   ├── search_books.py
│   └── history.py
│
├── member/
│   ├── __init__.py
│   ├── member_menu.py
│   ├── search_books.py
│   ├── view_books.py
│   ├── borrow_book.py
│   ├── return_book.py
│   └── history.py
│
├── database.py
├── LIBRARY MANAGEMENT QUERY'S.sql
├── README.md
└── .gitignore
```

## MySQL Database Setup

This project uses **MySQL** as the database.

The complete database queries are available in:

```text
LIBRARY MANAGEMENT QUERY'S.sql
```

The SQL file contains the database creation, table creation, relationships, sample data, queries, views, and other database operations required for the project.

### 1. Install MySQL

Install MySQL Server and MySQL Workbench on your system.

Make sure the MySQL server is running before starting the application.

### 2. Create the Database

Open **MySQL Workbench** and run:

```sql
CREATE DATABASE library_management;

USE library_management;
```

### 3. Create Tables

The SQL file contains the required tables for the Library Management System.

Main tables include:

```text
users
categories
books
librarians
members
issue_books
return_books
fines
history
```

The exact table definitions and relationships are available in:

```text
LIBRARY MANAGEMENT QUERY'S.sql
```

### 4. Run the SQL File

Open:

```text
LIBRARY MANAGEMENT QUERY'S.sql
```

in MySQL Workbench and execute the complete script.

You can also execute individual queries from the file as required.

### 5. Verify the Database

After executing the SQL file, check the database using:

```sql
SHOW DATABASES;

USE library_management;

SHOW TABLES;
```

To check table structure:

```sql
DESC users;
DESC categories;
DESC books;
```

To view records:

```sql
SELECT * FROM users;
SELECT * FROM categories;
SELECT * FROM books;
```

## Important MySQL Queries

### View All Books

```sql
SELECT * FROM books;
```

### View All Categories

```sql
SELECT * FROM categories;
```

### Search Books

```sql
SELECT *
FROM books
WHERE title LIKE '%Python%';
```

### View Available Books

```sql
SELECT *
FROM books
WHERE available_quantity > 0;
```

### Count Books

```sql
SELECT COUNT(*) AS total_books
FROM books;
```

### Books by Category

```sql
SELECT c.category_name, COUNT(b.book_id) AS total_books
FROM categories c
LEFT JOIN books b
ON c.category_id = b.category_id
GROUP BY c.category_id, c.category_name;
```

### Issue Book Details

```sql
SELECT *
FROM issue_books;
```

### Return Book Details

```sql
SELECT *
FROM return_books;
```

### View Fine Details

```sql
SELECT *
FROM fines;
```

### View Library History

```sql
SELECT *
FROM history;
```

## Database Connection

The Python application connects to MySQL through `database.py`.

Example:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="library_management"
    )
```

Replace:

```text
your_password
```

with your MySQL password.

Do not upload your actual MySQL password to GitHub.

## Install Python Dependency

Install MySQL Connector/Python using:

```bash
pip install mysql-connector-python
```

## Run the Project

After configuring the MySQL database, run the main Python file:

```bash
python main.py
```

Follow the menu options to access the Admin, Librarian, and Member modules.

## Admin Module

The Admin module provides functionality for:

* Managing users
* Managing books
* Managing categories
* Viewing history
* Generating reports

## Librarian Module

The Librarian module provides functionality for:

* Managing books
* Issuing books
* Returning books
* Managing fines
* Searching books
* Viewing history

## Member Module

The Member module provides functionality for:

* Searching books
* Viewing available books
* Borrowing books
* Returning books
* Viewing borrowing history

## GitHub

The project can be maintained and version-controlled using Git and GitHub.

Basic commands:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Security

* Do not store MySQL passwords in source code when sharing the project publicly.
* Do not upload `.env` files containing passwords.
* Add sensitive files to `.gitignore`.
* Use parameterized SQL queries when accepting user input.

## Future Enhancements

* Web-based interface using Flask or Django
* Email notifications
* Online book reservation
* Advanced search
* Dashboard and analytics
* Role-based authentication
* PDF report generation
* Book availability notifications
