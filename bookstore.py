import sqlite3
db = sqlite3.connect('data/books_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT,
                   	author TEXT, qty INTERGER)
''')
db.commit()

cursor = db.cursor()
id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

id2 = 3002
title2 = "Harry Potter and the Philosopher's Stone"
author2 = 'J K Rowling'
qty2 = 40

id3 = 3003
title3 = 'The Lion, the Witch and the Wardrobe'
author3 = 'C. S. Lewis'
qty3 = 25

id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkien'
qty4 = 37

id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5 = 12

# Insert book 1
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id1, title1, author1, qty1))
print('First book inserted')

# Insert book 2
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id2, title2, author2, qty2))
print('second book inserted')

# Insert book 3
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id3, title3, author3, qty3))
print('third book inserted')


# Insert book 4
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id4, title4, author4, qty4))
print('forth book inserted')


# Insert book 5
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id5, title5, author5, qty5))
print('Fifth book inserted')


db.commit()

# Defining a function to retrieve book data from the database


def get_book(id):

    cursor = db.cursor()
    query = "SELECT * FROM books WHERE id = ?"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
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
    print(f'id {id}, title {title}, author {author}, qty {qty} has been added to book store ')


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



def main():

    print("Welcome to the eBookstore!")

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
        print("Book added to the database")

# Update the details of an existing book in the database

    elif choice == "2":
        id = input("Enter book id: ")
        book = get_book(id)
        if book:
            title = input("Enter new book title: ")
            author = input("Enter new book author: ")
            update_book(id, title, author)
            print("Book details updated in the database")

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

    if __name__ == "__main__":
        main()
        THANKS



