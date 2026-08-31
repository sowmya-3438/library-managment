# Library Management System

## Project Overview

The Library Management System is a Python-based console application used to manage library activities such as users, books, categories, book issuing, returning books, fines, searching books, and viewing history.

The system is divided into three main roles:

* **Admin**
* **Librarian**
* **Member**

Each role has different permissions and features.

---

## Features

### Admin

The Admin is responsible for managing the overall library system.

* Add users
* View users
* Delete users
* Manage books
* Manage book categories
* View reports
* View issue and return history

### Librarian

The Librarian manages daily library operations.

* Add and manage books
* Issue books
* Return books
* Manage fines
* Search books
* View library history

### Member

The Member can access books and manage their own borrowing activities.

* Search books
* View available books
* Borrow books
* Return books
* View personal borrowing history

---

## Project Structure

```text
LibraryManagementSystem/
│
├── main.py
├── login.py
├── database.py
│
├── admin/
│   ├── __init__.py
│   ├── admin_menu.py
│   ├── user_management.py
│   ├── book_management.py
│   ├── category_management.py
│   ├── reports.py
│   └── history.py
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
└── member/
    ├── __init__.py
    ├── member_menu.py
    ├── search_books.py
    ├── view_books.py
    ├── borrow_book.py
    ├── return_book.py
    └── history.py
```

---

## Description of Files

### Main Files

**`main.py`**

This is the starting point of the application. It runs the library management system and connects the login and role-based menus.

**`login.py`**

Handles user login and checks the user's role before providing access to the appropriate menu.

**`database.py`**

Stores and manages the main library data such as users, books, categories, issued books, returned books, and other records.

---

## Admin Modules

### `admin_menu.py`

Displays the Admin menu and allows the Admin to select different operations.

### `user_management.py`

Used to:

* Add users
* View users
* Delete users

### `book_management.py`

Used to manage library books.

### `category_management.py`

Used to add, view, update, or manage book categories.

### `reports.py`

Displays library-related reports and information.

### `history.py`

Displays issue and return history for the library.

---

## Librarian Modules

### `librarian_menu.py`

Displays the Librarian menu.

### `book_management.py`

Allows the Librarian to manage books.

### `issue_book.py`

Handles issuing books to members.

### `return_book.py`

Handles returning books and updating their availability.

### `fine_management.py`

Manages fines related to overdue or returned books.

### `search_books.py`

Allows the Librarian to search for books.

### `history.py`

Displays book issue and return history.

---

## Member Modules

### `member_menu.py`

Displays the Member menu.

### `search_books.py`

Allows members to search for books.

### `view_books.py`

Displays available books.

### `borrow_book.py`

Allows members to borrow available books.

### `return_book.py`

Allows members to return borrowed books.

### `history.py`

Displays the member's borrowing and returning history.

---

## Role-Based Access

| Role      | Main Responsibilities                          |
| --------- | ---------------------------------------------- |
| Admin     | Users, books, categories, reports, history     |
| Librarian | Books, issue, return, fines, search, history   |
| Member    | Search, view, borrow, return, personal history |

---

## Application Flow

```text
Start Application
       |
       v
    Login
       |
       v
 Check Username & Password
       |
       v
    Check Role
       |
   ┌───┼───────────┐
   |   |           |
   v   v           v
 Admin Librarian  Member
   |     |          |
   v     v          v
Admin  Librarian  Member
Menu    Menu       Menu
```

---

## How to Run the Project

### Step 1: Open the Project

Open the `LibraryManagementSystem` folder in VS Code or any Python IDE.

### Step 2: Check Python Installation

Open the terminal and run:

```bash
python --version
```

If Python is installed, its version will be displayed.

### Step 3: Run the Application

From the project folder, run:

```bash
python main.py
```

The application will start and display the login screen.

---

## Example

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Login
2. Exit

Enter your choice:
```

After successful login, the system identifies the user's role and displays the corresponding menu.

Example:

```text
===== ADMIN MENU =====

1. User Management
2. Book Management
3. Category Management
4. Reports
5. History
6. Logout
```

---

## Technologies Used

* **Python**
* Python Modules
* Functions
* Classes
* Lists
* Dictionaries
* Conditional Statements
* Loops
* Exception Handling
* Modular Programming

---

## Key Concepts Used

### Modular Programming

The project is divided into multiple Python files based on functionality. This makes the project easier to understand, maintain, and debug.

### Role-Based Access

Different users get different permissions based on their role.

### Data Management

The system maintains information about users, books, issued books, returned books, categories, and fines.

### Functions

Functions are used to perform individual operations such as adding users, searching books, issuing books, and returning books.

### Classes

Classes such as `User` or `Book` can be used to represent library objects and their properties.

---

## Advantages

* Easy to use
* Simple console-based interface
* Role-based access
* Organized project structure
* Easy to maintain and modify
* Reduces manual library management work
* Provides book issue and return tracking
* Maintains borrowing history

---

## Future Enhancements

The project can be improved by adding:

* MySQL or SQLite database
* Graphical User Interface
* Password encryption
* Email notifications
* Automatic fine calculation
* Book reservation
* Due-date reminders
* Advanced search and filtering
* Admin dashboard
* Member registration
* Book availability notifications

---

## Conclusion

The Library Management System is a modular Python project that helps manage common library operations. By separating Admin, Librarian, and Member functionalities into different modules, the application is easier to manage and understand.

This project also demonstrates practical use of Python programming concepts such as functions, modules, classes, lists, dictionaries, conditional statements, loops, and role-based access.

---

### Project

**Library Management System**

### Language

**Python**
