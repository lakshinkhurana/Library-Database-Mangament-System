Library Management System
Overview
The Library Management System is a Python application designed to manage and track users and books in a library. It provides functionalities for adding users, managing books, issuing and returning books, and updating records. The application interacts with a MySQL database to perform CRUD (Create, Read, Update, Delete) operations.

Features
Add Users: Register new users with a unique User ID, name, and contact number.
Add Books: Add new books to the library's collection, including details such as Book ID, title, author, genre, and quantity.
Issue Books: Track book issuance to users, including recording issue and return dates.
Return Books: Handle book returns and update the library's inventory.
Display Records: View lists of all users and books in the library.
Update Records: Modify user contact information and book quantities.
Data Generation: Generate random user and book data for testing purposes.
Setup
Install Dependencies: Ensure you have the required Python libraries installed. You can install them using pip:

bash
Copy code
pip install mysql-connector-python faker
Database Setup:

Create a MySQL database named mydb.
Ensure the following tables are created in the mydb database:
Users with columns UserID, Name, and Contact.
Books with columns BookID, Title, Author, Genre, and Quantity.
Issued_Books with columns IssueID, BookID, UserID, IssueDate, and ReturnDate.
Configuration:

Update the database connection parameters in the script (host, user, password, database, and port) to match your MySQL server configuration.
Running the Application:

Execute the script to start the library management system:
bash
Copy code
python your_script_name.py
Usage
Add User: Add a new user by providing the User ID, name, and contact number.
Add Book: Add a new book by specifying the Book ID, title, author, genre, and quantity.
Issue Book: Issue a book to a user by entering the Issue ID, Book ID, and User ID. Specify the issue and return dates.
Return Book: Return a book by providing the Issue ID and confirming the book's return.
Display All Users: View a list of all registered users.
Display All Books: View a list of all books in the library.
Update User: Update the contact information of a user by specifying the User ID.
Update Book: Update the quantity of a book by providing the Book ID.
Data Generation
To generate random data for users and books, use the generate_random_users and generate_random_books functions in the script. This can be useful for testing and populating the database with sample data.

Contributing
Feel free to fork the repository, make improvements, and submit pull requests. Your contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Faker for generating realistic fake data.
MySQL Connector/Python for connecting to the MySQL database.
