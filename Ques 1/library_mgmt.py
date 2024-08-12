import os
import datetime
BOOKS_FILE = "books.txt"
USERS_FILE = "users.txt"
TRANSACTIONS_FILE = "transactions.txt"

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write("\n".join(data))

def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + "\n")

def generate_id(filename, prefix):
    lines = read_file(filename)
    if not lines:
        return f"{prefix}1"
    last_id = lines[-1].split(",")[0]
    new_id = int(last_id[len(prefix):]) + 1
    return f"{prefix}{new_id}"

def add_book(title, author):
    book_id = generate_id(BOOKS_FILE, "B")
    book_entry = f"{book_id},{title},{author},available"
    append_to_file(BOOKS_FILE, book_entry)
    print(f"Book '{title}' added successfully with ID: {book_id}")

def register_user(name):
    user_id = generate_id(USERS_FILE, "U")
    user_entry = f"{user_id},{name}"
    append_to_file(USERS_FILE, user_entry)
    print(f"User '{name}' registered successfully with ID: {user_id}")

def borrow_book(user_id, book_id):
    books = read_file(BOOKS_FILE)
    users = read_file(USERS_FILE)
    if not any(user.split(",")[0] == user_id for user in users):
        print(f"User ID {user_id} not found.")
        return

    updated_books = []
    for book in books:
        b_id, title, author, status = book.split(",")
        if b_id == book_id:
            if status == "available":
                status = "borrowed"
                transaction_entry = f"{user_id},{book_id},{datetime.date.today()},"
                append_to_file(TRANSACTIONS_FILE, transaction_entry)
                print(f"Book '{title}' borrowed by User ID {user_id}")
            else:
                print(f"Book ID {book_id} is already borrowed.")
        updated_books.append(f"{b_id},{title},{author},{status}")
    
    write_file(BOOKS_FILE, updated_books)

def return_book(user_id, book_id):
    transactions = read_file(TRANSACTIONS_FILE)
    updated_transactions = []
    book_returned = False
    
    for transaction in transactions:
        u_id, b_id, borrow_date, return_date = transaction.split(",")
        if u_id == user_id and b_id == book_id and return_date == "":
            return_date = str(datetime.date.today())
            updated_transactions.append(f"{u_id},{b_id},{borrow_date},{return_date}")
            book_returned = True
        else:
            updated_transactions.append(transaction)
    
    if book_returned:
        books = read_file(BOOKS_FILE)
        updated_books = []
        for book in books:
            b_id, title, author, status = book.split(",")
            if b_id == book_id:
                status = "available"
            updated_books.append(f"{b_id},{title},{author},{status}")
        
        write_file(TRANSACTIONS_FILE, updated_transactions)
        write_file(BOOKS_FILE, updated_books)
        print(f"Book ID {book_id} returned by User ID {user_id}")
    else:
        print(f"No borrowing record found for User ID {user_id} and Book ID {book_id}")

def view_available_books():
    books = read_file(BOOKS_FILE)
    available_books = [book for book in books if "available" in book]
    if not available_books:
        print("No available books.")
    else:
        print("Available Books:")
        for book in available_books:
            print(book)

def view_registered_users():
    users = read_file(USERS_FILE)
    if not users:
        print("No registered users.")
    else:
        print("Registered Users:")
        for user in users:
            print(user)

def view_borrowed_books():
    transactions = read_file(TRANSACTIONS_FILE)
    borrowed_books = [transaction for transaction in transactions if transaction.split(",")[3] == ""]
    if not borrowed_books:
        print("No borrowed books.")
    else:
        print("Borrowed Books:")
        for transaction in borrowed_books:
            print(transaction)

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Register a User")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View Available Books")
        print("6. View Registered Users")
        print("7. View Borrowed Books")
        print("8. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == '2':
            name = input("Enter user name: ")
            register_user(name)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            borrow_book(user_id, book_id)
        elif choice == '4':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            return_book(user_id, book_id)
        elif choice == '5':
            view_available_books()
        elif choice == '6':
            view_registered_users()
        elif choice == '7':
            view_borrowed_books()
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
