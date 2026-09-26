

CREATE DATABASE library_management;

USE library_management;

SHOW TABLES;
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    age INT,
    gender VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CHECK (role IN ('Admin', 'Librarian', 'Member')),
    CHECK (age IS NULL OR age >= 5)
);
-- Categories table
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(255)
);
-- Books table
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    isbn VARCHAR(30) UNIQUE,
    publisher VARCHAR(100),
    publication_year YEAR,
    quantity INT NOT NULL DEFAULT 1,
    available_quantity INT NOT NULL DEFAULT 1,
    price DECIMAL(10,2),
    added_date DATE DEFAULT (CURRENT_DATE),

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id),

    CHECK (quantity >= 0),
    CHECK (available_quantity >= 0),
    CHECK (available_quantity <= quantity),
    CHECK (price >= 0)
);
-- book issue table
CREATE TABLE book_issues (
    issue_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    user_id INT NOT NULL,
    issue_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    due_date DATE NOT NULL,
    returned_date DATE,
    issue_status VARCHAR(20) DEFAULT 'Issued',

    FOREIGN KEY (book_id)
        REFERENCES books(book_id),

    FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    CHECK (issue_status IN ('Issued', 'Returned', 'Overdue'))
);

-- Book returns table
CREATE TABLE book_returns (
    return_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_id INT NOT NULL,
    return_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    return_condition VARCHAR(50),
    remarks VARCHAR(255),

    FOREIGN KEY (issue_id)
        REFERENCES book_issues(issue_id)
);

-- Fine table
CREATE TABLE fines (
    fine_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_id INT NOT NULL,
    user_id INT NOT NULL,
    fine_amount DECIMAL(10,2) NOT NULL,
    reason VARCHAR(255),
    fine_status VARCHAR(20) DEFAULT 'Unpaid',
    paid_date DATE,

    FOREIGN KEY (issue_id)
        REFERENCES book_issues(issue_id),

    FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    CHECK (fine_amount >= 0),
    CHECK (fine_status IN ('Paid', 'Unpaid'))
);
-- Audit and History table

CREATE TABLE library_audit (
    audit_id INT PRIMARY KEY AUTO_INCREMENT,
    table_name VARCHAR(50),
    record_id INT,
    action_type VARCHAR(30),
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255)
); 
-- users
INSERT INTO users
(full_name, username, password, role, email, phone, age, gender)
VALUES
('Admin', 'admin', 'admin123', 'Admin',
 'admin@library.com', '9000000001', 35, 'Male'),

('Librarian', 'librarian', 'lib123', 'Librarian',
 'librarian@library.com', '9000000002', 30, 'Female'),

('Student', 'student', 'stu123', 'Member',
 'student@library.com', '9000000003', 22, 'Female'),

('Rahul Kumar', 'rahul', 'rahul123', 'Member',
 'rahul@gmail.com', '9000000004', 24, 'Male'),

('Sneha Reddy', 'sneha', 'sneha123', 'Member',
 'sneha@gmail.com', '9000000005', 25, 'Female');
 SELECT * FROM users;
 -- catgories records
 INSERT INTO categories
(category_name, description)
VALUES
('Programming', 'Programming and software development books'),
('Database', 'Database and SQL books'),
('Science', 'Science and technology books'),
('Fiction', 'Fiction and story books'),
('Mathematics', 'Mathematics and problem solving books');
SELECT * FROM categories;
INSERT INTO books
(book_name, author, category_id, isbn, publisher,
 publication_year, quantity, available_quantity, price)
VALUES

('Python Programming',
 'Guido van Rossum',
 1,
 'ISBN001',
 'Tech Publications',
 2023,
 5,
 5,
 650.00),

('Java Programming',
 'James Gosling',
 1,
 'ISBN002',
 'Programming Press',
 2022,
 3,
 3,
 700.00),

('SQL Fundamentals',
 'John Smith',
 2,
 'ISBN003',
 'Database Publications',
 2024,
 4,
 4,
 550.00),

('MySQL Complete Guide',
 'Robert James',
 2,
 'ISBN004',
 'Tech Publications',
 2023,
 2,
 2,
 600.00),

('Physics Fundamentals',
 'David Hall',
 3,
 'ISBN005',
 'Science Publications',
 2021,
 3,
 3,
 450.00),

('The Secret Garden',
 'Frances Hodgson Burnett',
 4,
 'ISBN006',
 'Classic Books',
 2020,
 2,
 2,
 350.00),

('Data Structures',
 'Mark Allen',
 1,
 'ISBN007',
 'Tech Publications',
 2024,
 4,
 4,
 800.00);
 SELECT * FROM books;
 -- insert book issue
 INSERT INTO book_issues
(book_id, user_id, issue_date, due_date, issue_status)
VALUES
(1, 3, '2026-09-01', '2026-09-15', 'Returned'),

(2, 4, '2026-09-05', '2026-09-19', 'Issued'),

(3, 5, '2026-09-10', '2026-09-24', 'Issued'),

(4, 3, '2026-08-15', '2026-08-29', 'Overdue'),

(5, 4, '2026-09-12', '2026-09-26', 'Issued');
select * from book_issues;
-- insert book returns
INSERT INTO book_returns
(issue_id, return_date, return_condition, remarks)
VALUES
(1, '2026-09-14', 'Good', 'Returned before due date'),

(4, '2026-09-03', 'Good', 'Returned after due date');
select * from book_returns;
--  insert fines
INSERT INTO fines
(issue_id, user_id, fine_amount, reason, fine_status, paid_date)
VALUES
(4, 3, 50.00, 'Late return', 'Unpaid', NULL),

(1, 3, 0.00, 'No fine', 'Paid', '2026-09-14');
select*from fines;
-- Display all users

SELECT *
FROM users;


-- Display all books

SELECT *
FROM books;


-- Display all categories

SELECT *
FROM categories;


-- Display all issues

SELECT *
FROM book_issues;


-- Display all returns

SELECT *
FROM book_returns;


-- Display all fines

SELECT *
FROM fines;
-- display only book names and authors
SELECT
    book_name,
    author
FROM books;
-- Display available books
SELECT
    book_name,
    author,
    available_quantity
FROM books
WHERE available_quantity > 0;
-- display the book name and author name
SELECT
    book_name,
    author,
    price
FROM books;
-- display all books whose price is greater than 600
SELECT *
FROM books
WHERE price > 600;
-- display all books whose price is greater than 600 and which are currently available
SELECT *
FROM books
WHERE price > 600
AND available_quantity > 0;
-- between
-- display all books whose price is between 500 and 800
SELECT *
FROM books
WHERE price BETWEEN 500 AND 800;
-- using in
-- display all users whose role is either admin or librarian
SELECT *
FROM users
WHERE role IN ('admin', 'librarian');
-- Like
-- Books starting with P

SELECT *
FROM books
WHERE book_name LIKE 'P%';


-- Books containing "SQL"

SELECT *
FROM books
WHERE book_name LIKE '%SQL%';

-- Authors ending with "i"
SELECT *
FROM books
WHERE author LIKE '%i';
-- DISTINCT

-- display the unique author names from the books table without
SELECT DISTINCT author
FROM books;
-- count
-- find the total number of books in the books table
SELECT COUNT(*) AS total_books
FROM books;
-- SUM
-- calulate the total number of book copies available in the library
SELECT SUM(quantity) AS total_book_copies
FROM books;
-- find the minimum and maximum book prices
SELECT
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM books;
-- find the number of books available in each category
SELECT
    category_id,
    COUNT(*) AS total_books
FROM books
GROUP BY category_id;
-- calculate the total number of book copies for each category
SELECT
    category_id,
    SUM(quantity) AS total_copies
FROM books
GROUP BY category_id;
-- display the book ID, book name, author, category name, and price by joining the books and categories tables
SELECT
    b.book_id,
    b.book_name,
    b.author,
    c.category_name,
    b.price
FROM books b
INNER JOIN categories c
ON b.category_id = c.category_id;
-- display all categories and their books, including categories
SELECT
    c.category_name,
    b.book_name
FROM categories c
LEFT JOIN books b
ON c.category_id = b.category_id;
-- mutiple table
SELECT
    u.full_name,
    b.book_name,
    bi.issue_date,
    bi.due_date,
    bi.issue_status
FROM book_issues bi

JOIN users u
ON bi.user_id = u.user_id

JOIN books b
ON bi.book_id = b.book_id;
-- users who have borrowed at least  one book
SELECT
    u.full_name
FROM users u
WHERE EXISTS
(
    SELECT 1
    FROM book_issues bi
    WHERE bi.user_id = u.user_id
);
-- Books starting with P

SELECT *
FROM books
WHERE book_name LIKE 'P%';


-- Books containing "SQL"

SELECT *
FROM books
WHERE book_name LIKE '%SQL%';


-- Authors ending with "i"

SELECT *
FROM books
WHERE author LIKE '%i';
-- Lowest price first

SELECT *
FROM books
ORDER BY price ASC;


-- Highest price first

SELECT *
FROM books
ORDER BY price DESC;
-- combine the member and book and issue
SELECT
    u.full_name,
    b.book_name,
    bi.issue_date,
    bi.due_date,
    bi.issue_status
FROM book_issues bi

JOIN users u
ON bi.user_id = u.user_id

JOIN books b
ON bi.book_id = b.book_id;
-- book return report
SELECT
    u.full_name,
    b.book_name,
    bi.issue_date,
    bi.due_date,
    bi.issue_status
FROM book_issues bi

JOIN users u
ON bi.user_id = u.user_id

JOIN books b
ON bi.book_id = b.book_id;
-- Fine report
SELECT
    u.full_name,
    b.book_name,
    bi.issue_date,
    bi.due_date,
    bi.issue_status
FROM book_issues bi

JOIN users u
ON bi.user_id = u.user_id

JOIN books b
ON bi.book_id = b.book_id;
-- books more expensive than average price
SELECT
    book_name,
    price
FROM books
WHERE price >
(
    SELECT AVG(price)
    FROM books
);
-- second highest price
SELECT MAX(price) AS second_highest_price
FROM books
WHERE price <
(
    SELECT MAX(price)
    FROM books
);
-- member older than average age
SELECT
    full_name,
    age
FROM users
WHERE role = 'member'
AND age >
(
    SELECT AVG(age)
    FROM users
    WHERE role = 'member'
);
-- users who have borrowed books
SELECT
    full_name
FROM users
WHERE user_id IN
(
    SELECT user_id
    FROM book_issues
);
-- books that have been issued
SELECT
    book_name
FROM books
WHERE book_id IN
(
    SELECT book_id
    FROM book_issues
);
-- NOT EXISTS
SELECT
    book_name
FROM books
WHERE book_id IN
(
    SELECT book_id
    FROM book_issues
);
-- correlated subquery
SELECT
    b.book_name,
    b.price,
    b.category_id
FROM books b
WHERE b.price >
(
    SELECT AVG(b2.price)
    FROM books b2
    WHERE b2.category_id = b.category_id
);
-- case statement
SELECT
    book_name,
    price,

    CASE
        WHEN price >= 800 THEN 'Expensive'
        WHEN price >= 500 THEN 'Medium'
        ELSE 'Low'
    END AS price_category

FROM books;
-- case for book availability
SELECT
    book_name,
    quantity,
    available_quantity,

    CASE
        WHEN available_quantity = 0 THEN 'Not Available'
        WHEN available_quantity < quantity THEN 'Partially Available'
        ELSE 'Fully Available'
    END AS availability_status

FROM books;
-- Date Functions
SELECT
    issue_id,
    issue_date,
    YEAR(issue_date) AS issue_year,
    MONTH(issue_date) AS issue_month,
    DAY(issue_date) AS issue_day
FROM book_issues;
-- string functions
SELECT
    UPPER(book_name) AS book_name_upper,
    LOWER(author) AS author_lower
FROM books;
-- length
SELECT
    book_name,
    LENGTH(book_name) AS name_length
FROM books;
-- date functions
SELECT
    issue_id,
    issue_date,
    YEAR(issue_date) AS issue_year,
    MONTH(issue_date) AS issue_month,
    DAY(issue_date) AS issue_day
FROM book_issues;
-- Date Difference
SELECT
    issue_id,
    issue_date,
    due_date,
    DATEDIFF(due_date, issue_date) AS borrowing_days
FROM book_issues;
-- current Date
SELECT
    CURDATE() AS today;
-- find overdue books
SELECT
    u.full_name,
    b.book_name,
    bi.due_date,
    DATEDIFF(CURDATE(), bi.due_date) AS overdue_days
FROM book_issues bi

JOIN users u
ON bi.user_id = u.user_id

JOIN books b
ON bi.book_id = b.book_id

WHERE bi.due_date < CURDATE()
AND bi.issue_status <> 'Returned';
-- update
UPDATE books
SET price = 750
WHERE book_id = 1;
-- update multiple columns
UPDATE books
SET
    quantity = 6,
    available_quantity = 6
WHERE book_id = 1;
-- view-book catalog
CREATE VIEW book_catalog AS

SELECT
    b.book_id,
    b.book_name,
    b.author,
    c.category_name,
    b.quantity,
    b.available_quantity,
    b.price
FROM books b

JOIN categories c
ON b.category_id = c.category_id;
SELECT *
FROM book_catalog;
-- View - BORROWING History
CREATE VIEW borrowing_history AS

SELECT
    bi.issue_id,
    u.full_name AS member_name,
    b.book_name,
    c.category_name,
    bi.issue_date,
    bi.due_date,
    bi.issue_status
FROM book_issues bi

JOIN users u
ON bi.user_id = u.user_id

JOIN books b
ON bi.book_id = b.book_id

JOIN categories c
ON b.category_id = c.category_id;
SELECT *
FROM borrowing_history;
-- Stored Procedure- Books BY CATEGORY
DELIMITER //

CREATE PROCEDURE GetBooksByCategory(
    IN category_name_input VARCHAR(100)
)

BEGIN

    SELECT
        b.book_id,
        b.book_name,
        b.author,
        c.category_name,
        b.price,
        b.available_quantity

    FROM books b

    JOIN categories c
    ON b.category_id = c.category_id

    WHERE c.category_name = category_name_input;

END //

DELIMITER ;
-- MEMBER HISTORY
DELIMITER //

CREATE PROCEDURE GetBooksByCategory(
    IN category_name_input VARCHAR(100)
)

BEGIN

    SELECT
        b.book_id,
        b.book_name,
        b.author,
        c.category_name,
        b.price,
        b.available_quantity

    FROM books b

    JOIN categories c
    ON b.category_id = c.category_id

    WHERE c.category_name = category_name_input;

END //

DELIMITER ;
-- TRIGGER
-- AUDIT AFTER INSERT
DELIMITER //

CREATE TRIGGER after_book_insert

AFTER INSERT ON books

FOR EACH ROW

BEGIN

    INSERT INTO library_audit
    (
        table_name,
        record_id,
        action_type
    )

    VALUES
    (
        'books',
        NEW.book_id,
        'INSERT'
    );

END //

DELIMITER ;
-- TRANSACTION
-- ISSUE A BOOK
START TRANSACTION;

INSERT INTO book_issues
(
    book_id,
    user_id,
    issue_date,
    due_date,
    issue_status
)
VALUES
(
    1,
    6,
    CURDATE(),
    DATE_ADD(CURDATE(), INTERVAL 14 DAY),
    'Issued'
);

UPDATE books
SET available_quantity = available_quantity - 1
WHERE book_id = 1
AND available_quantity > 0;

COMMIT;
-- TRANSACTION WITH ROLLBACK
START TRANSACTION;

UPDATE books
SET available_quantity = available_quantity - 1
WHERE book_id = 2;

INSERT INTO book_issues
(
    book_id,
    user_id,
    issue_date,
    due_date
)
VALUES
(
    2,
    5,
    CURDATE(),
    DATE_ADD(CURDATE(), INTERVAL 14 DAY)
);

ROLLBACK;
-- SAVEPOINT
START TRANSACTION;

UPDATE books
SET price = price + 50
WHERE category_id = 1;

SAVEPOINT price_update;

UPDATE books
SET price = price + 100
WHERE category_id = 2;

ROLLBACK TO price_update;

COMMIT;
-- INDEXES
CREATE INDEX idx_book_name
ON books(book_name);

CREATE INDEX idx_book_author
ON books(author);

CREATE INDEX idx_issue_date
ON book_issues(issue_date);

CREATE INDEX idx_user_username
ON users(username);


-- CHECK THE INDEXES
SHOW INDEX FROM books;

SHOW INDEX FROM book_issues;

SHOW INDEX FROM users;

SHOW INDEX FROM fines;

-- MOST BORROWED BOOKS
SELECT
    b.book_name,
    COUNT(bi.issue_id) AS times_borrowed
FROM books b

JOIN book_issues bi
ON b.book_id = bi.book_id

GROUP BY
    b.book_id,
    b.book_name

ORDER BY times_borrowed DESC;
-- MOST ACTIVE MEMBERS
SELECT
    u.full_name,
    COUNT(bi.issue_id) AS books_borrowed
FROM users u

JOIN book_issues bi
ON u.user_id = bi.user_id

WHERE u.role = 'member'

GROUP BY
    u.user_id,
    u.full_name

ORDER BY books_borrowed DESC;
-- AVAILABLE BOOK REPORT
SELECT
    b.book_id,
    b.book_name,
    b.author,
    c.category_name,
    b.available_quantity
FROM books b

JOIN categories c
ON b.category_id = c.category_id

WHERE b.available_quantity > 0

ORDER BY b.book_name;
-- OVERDUE BOOK REPORT
SELECT
    u.full_name AS member,
    b.book_name,
    bi.due_date,
    DATEDIFF(CURDATE(), bi.due_date) AS overdue_days
FROM book_issues bi

JOIN users u
ON bi.user_id = u.user_id

JOIN books b
ON bi.book_id = b.book_id

WHERE bi.issue_status = 'Overdue'
OR
(
    bi.due_date < CURDATE()
    AND bi.issue_status <> 'Returned'
);