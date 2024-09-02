import mysql.connector
import datetime

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='19102005',
    database='library_db',
    charset = 'utf8',
    port='3306'
)
cursor = conn.cursor()

def number():
    contact=int(input('Enter Contact Number: '))
    if len(str(contact))==10 and contact%-1!=0:
        return contact
    else:
        print('Wrong Input! Try Again')
        number()
    
def user_entry():
    userID=int(input('Enter User ID:'))
    if userID%-1==0:
        raise ValueError('Wrong ID!',user_entry())
    username=input('Enter User Name: ')
    contact=number()
    cursor.execute(f"INSERT INTO Users (UserID,Name,Contact) VALUES({userID},'{username}',{contact})")

def book_entry():
    bookID=int(input('Enter Book ID:'))
    if bookID%-1==0:
        raise ValueError('Wrong Book ID')
    title=input('Enter Title: ')
    author=input('Enter Author: ')
    genre=input('Enter Genre: ')
    quantity=int(input('Enter Quantity: '))
    if quantity<0:
        raise ValueError('Quantity Cannot be less than 0')
    cursor.execute(f"INSERT INTO Books (BookID,Title,Author,Genre,Quantity) VALUES({bookID},'{title}','{author}','{genre}',{quantity})")

def input_date(param):
    while True:
        try:
            date_str = input(f"Enter {param} date (YYYY-MM-DD): ")
            parts = date_str.split('-')
            if len(parts) != 3:
                raise ValueError("Incorrect date format. Please use YYYY-MM-DD.")
            
            year, month, day = map(int, parts)
            
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")
            
            if day < 1 or day > 31:
                raise ValueError("Day must be between 1 and 31.")
            
            leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

            if month == 2:
                if day > 29:
                    raise ValueError("February cannot have more than 29 days.")
                if day == 29 and not leap_year:
                    raise ValueError(f"{year} is not a leap year, so February 29th is invalid.")

            date = datetime.date(year, month, day)
            return date
        
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

def issue_entry():
    issueID=int(input('Enter Issue ID:'))
    bookID=int(input('Enter Book ID: '))
    userID=int(input('Enter User ID: '))
    cursor.execute(f'SELECT * FROM BOOKS WHERE BookID={bookID}')
    result=cursor.fetchone()
    if result is None:
        raise ValueError('Book not found.')
    if result[4]>0:
        issueDate=input_date('issue')
        returnDate=input_date('return')
    cursor.execute(f"INSERT INTO Issued_Books (IssueID,BookID,UserID,IssueDate,ReturnDate) VALUES({issueID},{bookID},{userID},'{issueDate}','{returnDate}')")
    cursor.execute(f"UPDATE Books SET Quantity=Quantity-1 WHERE BookID={bookID}")
    conn.commit()
    print('Book issued succesfully.')

def return_book():
    issueID=int(input('Enter Issue ID:'))
    cursor.execute(f"SELECT * FROM Issued_Books WHERE IssueID={issueID}")
    result=cursor.fetchone()
    if result is None:
        raise ValueError('Book Not Found')
    for i in result:
        print(f"{i}\n")
    query=int(input('Is this your book?(0 or 1)'))
    if query==0:
        print("Trying Again.")
        return_book()
    if query==1:
         bookID = result[0]
         cursor.execute(f"DELETE FROM Issued_Books WHERE IssueID = {issueID}")
         cursor.execute(f"UPDATE Books SET Quantity = Quantity + 1 WHERE BookID = {bookID}")
         conn.commit()
         print("Book returned successfully.")
    else:
        raise ValueError('Wrong Input.')
    
def display_users():
    cursor.execute("SELECT * FROM Users")
    for row in cursor.fetchall():
        print(row)

def display_books():
    cursor.execute("SELECT * FROM Books")
    for row in cursor.fetchall():
        print(row)

def update_user():
    userID = int(input('Enter User ID to update: '))
    new_contact = number()
    cursor.execute(f"UPDATE Users SET Contact = {new_contact} WHERE UserID = {userID}")
    conn.commit()
    print("User information updated.")

def update_book():
    bookID = int(input('Enter Book ID to update: '))
    new_quantity = int(input('Enter new quantity: '))
    if new_quantity<0 or bookID<0:
        raise ValueError('Wrong Input.')
    cursor.execute(f"UPDATE Books SET Quantity = {new_quantity} WHERE BookID = {bookID}")
    conn.commit()
    print("Book information updated.")

def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add User")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display All Users")
        print("6. Display All Books")
        print("7. Update User")
        print("8. Update Book")
        print("9. Exit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            user_entry()
        elif choice == '2':
            book_entry()
        elif choice == '3':
            issue_entry()
        elif choice == '4':
            return_book()
        elif choice == '5':
            display_users()
        elif choice == '6':
            display_books()
        elif choice == '7':
            update_user()
        elif choice == '8':
            update_book()
        elif choice == '9':
            break
        else:
            print("Invalid choice! Please try again.")

menu()
