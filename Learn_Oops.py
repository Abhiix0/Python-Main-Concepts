# Create a class-based library system that handles books and eBooks using OOP principles including inheritance.
# Demonstrates: Classes, inheritance, methods, and object management

# Base Book class representing a physical or digital book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Book is available by default

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} - {status}")

# Library class manages a collection of books and provides operations
class Library:
    def __init__(self):
        self.books = []  # List to store Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book removed: {title}")
                return
        print("Book not found!")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed: {title}")
                return
        print("Book not available!")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You returned: {title}")
                return
        print("Return failed: Check title or availability.")

    def show_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                book.display_info()

# Inherited class: EBook (adds file size & download link)
class EBook(Book):
    def __init__(self, title, author, file_size, link):
        super().__init__(title, author)  # Inherit title, author, available
        self.file_size = file_size
        self.link = link

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"[E-Book] {self.title} ({self.file_size}MB) - {status}")
        print(f"Download: {self.link}")

# -----------------------
# Demo Section: Create library, add books, borrow/return, and display
lib = Library()

# Add physical books
lib.add_book(Book("Deep Work", "Cal Newport"))
lib.add_book(Book("The Pragmatic Programmer", "Andy Hunt"))

# Add an eBook
lib.add_book(EBook("AI Revolution", "Lex Fridman", 5, "https://example.com/ai"))

# Show all available books
lib.show_available_books()

# Borrow and return books
lib.borrow_book("Deep Work")
lib.borrow_book("AI Revolution")
lib.return_book("Deep Work")

# Show available books after transactions
lib.show_available_books()
