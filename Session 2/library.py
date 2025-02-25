class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Default status buku: tersedia

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"Sorry, {self.title} is currently not available.")

    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned.")

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def show_available_books(self):
        print("\nAvailable Books:")
        available_books = [book for book in self.books if book.available]
        if available_books:
            for book in available_books:
                book.display_info()
        else:
            print("No books available.")

    def show_borrowed_books(self):
        print("\nBorrowed Books:")
        borrowed_books = [book for book in self.books if not book.available]
        if borrowed_books:
            for book in borrowed_books:
                book.display_info()
        else:
            print("No books are currently borrowed.")


library = Library()
book1 = Book("1984", "George Orwell", "978-0451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_available_books()

# Pinjam buku
book1.borrow_book()
library.show_available_books()
library.show_borrowed_books()

# Kembalikan buku
book1.return_book()
library.show_available_books()
library.show_borrowed_books()
