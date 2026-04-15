# OOPS - Library Management System

class Book:

    book_counter = 1000 # class variable

    # static method
    @staticmethod
    def generate_book_id():
        Book.book_counter += 1
        return Book.book_counter
    
    # constructor - magic/dunder method
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = Book.generate_book_id()

        # encapsulate
        self.__available = True

    # instance method
    def borrow_book(self):
        if self.__available:
            self.__available = False
            print(f"{self.title} borrowed successfully.")
        else:
            print("Book is currently unavailable.")

    def return_book(self):
        self.__available = True
        print(f"{self.title} returned successfully.")

    # magic/dunder method
    def __str__(self):
        status = "Available" if self.__available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} >> ({status})"
    

# Child class1: Printed Books
class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info} | Pages: {self.pages}"
    

# Child class2: Ebook
class EBook(Book):

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info} | File Size: {self.file_size}MB"
        

# Library System
    
library = []

def add_book():
    print("\nAdd Book")
    title = input("Enter title: ")
    author = input("Enter author: ")
    book_type = input("Type (1: Printed, 2: Ebook): ")

    if book_type == "1":
        pages = int(input("Enter number of pages in the book: "))
        book = PrintedBook(title, author, pages)
    elif book_type == "2":
        size = float(input("Enter file size(MB): "))
        book = EBook(title, author, size)
    else:
        print("Invalid book type.")
        return
    library.append(book)
    print("Book added successfully!\n")

def view_books():
    print("\nLibrary Inventory:")

    if len(library) == 0:
        print("No books in library.")
        return
    
    for book in library:
        print(book) # calls __str__()
    print()

def borrow_book():
    book_id = int(input("Enter book-id to borrow: "))

    for book in library:
        if book.book_id == book_id:
            book.borrow_book()
            return
    print("Book not found.\n")

def return_book():
    book_id = int(input("Enter book-id to return: "))

    for book in library:
        if book.book_id == book_id:
            book.return_book()
            return
    print("Book not found.\n")

def menu():
    while True:

        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow A Book")
        print("4. Return A Book")
        print("5. Exit")

        choice = input("Choose an option(1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting Library System")
            break
        else:
            print("Invalid Option")

menu()