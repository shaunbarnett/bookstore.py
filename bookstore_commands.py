import sqlite3
db = sqlite3.connect('data/books_db')
cursor = db.cursor()  # Get a cursor object

# Defining a function to retrieve book data from the database


def get_book(id):

    cursor = db.cursor()
    query = "SELECT * FROM books WHERE id = ?"
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    cursor.close()
    return result


# Defining a function to add a new book to the database

def add_book(id, title, author, qty):

    cursor = db.cursor()
    query = "INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)"
    values = (id, title, author, qty)
    cursor.execute(query, values)
    db.commit()
    cursor.close()


# Defining a function to update the details of an existing book in the database

def update_book(id, title, author):

    cursor = db.cursor()
    query = "UPDATE books SET title = ?, author = ? WHERE id = ?"
    values = (title, author, id)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    print(f'book has been updated to {title}')


# Defining a function to remove a book from the database

def remove_book(id):

    cursor = db.cursor()
    query = "DELETE FROM books WHERE id = ?"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    print('book deleted')

# main menu

def main():

    print("\nWelcome to the eBookstore!")

while True:

    print("1. Add book")
    print("2. Update book")
    print("3. Remove book")
    print("4. Search book")
    print("5. Exit")

    choice = input("Enter your choice: ")

# Add a new book to the database

    if choice == "1":
        id = input("Enter book id: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        qty = input("Enter book quantity: ")
        add_book(id, title, author, qty)
        print(f"\n{title} has been added to the database. thanks")

# Update the details of an existing book in the database

    elif choice == "2":
        id = input("Enter book id: ")
        book = get_book(id)
        if book:
            title = input("Enter new book title: ")
            author = input("Enter new book author: ")
            update_book(id, title, author)
            print("Book details updated in the database. thanks")
            quit()

        else:
            print("No book found with that id")

# Remove a book from the database

    elif choice == "3":
        id = input("Enter book id: ")
        book = get_book(id)
        if book:
            remove_book(id)
            print("Book removed from the database")
        else:
            print("No book found with that id")

# Search for a book in the database

    elif choice == "4":
        id = input("Enter book id: ")
        book = get_book(id)
        if book:
            print(f"Book found: {book}")
        else:
            print("No book found with that id")

# Exit the program

    elif choice == "5":
        print("Goodbye!")
        break

# Handle invalid choices

    else:
        print("Invalid choice. Please try again.")
