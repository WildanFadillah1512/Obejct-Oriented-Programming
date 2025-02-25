class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, isbn):
        self.books[isbn] = {"title": title, "author": author, "available": True}
        print(f"Book '{title}' added successfully!")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nList of Books:")
            for isbn, details in self.books.items():
                status = "Available" if details["available"] else "Borrowed"
                print(f"ISBN: {isbn} | Title: {details['title']} | Author: {details['author']} | Status: {status}")

    def borrow_book(self, isbn):
        if isbn in self.books:
            if self.books[isbn]["available"]:
                self.books[isbn]["available"] = False
                print(f"Book '{self.books[isbn]['title']}' borrowed successfully!")
            else:
                print("Sorry, this book is currently borrowed.")
        else:
            print("Book not found!")

    def return_book(self, isbn):
        if isbn in self.books:
            if not self.books[isbn]["available"]:
                self.books[isbn]["available"] = True
                print(f"Book '{self.books[isbn]['title']}' returned successfully!")
            else:
                print("This book was not borrowed.")
        else:
            print("Book not found!")

# Main Program with Menu
def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. List Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            library.list_books()

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "3":
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)

        elif choice == "4":
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)

        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()