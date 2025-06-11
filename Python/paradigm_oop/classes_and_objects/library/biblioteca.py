#Brief:
#Date: 13/11/2024
#Version: 1.0

"""
Statement:
Define a book class with attributes like title, author, and ISBN
Define a library class with attribute names and a list of books
Implement methods in the library to:
-Add books to the collection
-Display the list of available books
-Create Books instances and add them to a library instance 
"""

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def __str__(self):
        return f"📖 {self.__title} by {self.__author} (ISBN: {self.__isbn})"

    def show_details(self):
        return (f"📘 Book Details:\n"
                f"  • Title : {self.__title}\n"
                f"  • Author: {self.__author}\n"
                f"  • ISBN  : {self.__isbn}")


class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def __str__(self):
        return f"🏛️ Library: {self.__name}"

    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
            print(f"✅ Book added: {book}")
        else:
            print("❌ Only Book instances can be added.")

    def show_books(self):
        if not self.__books:
            print("📭 No books in the library.")
            return
        print(f"\n📚 Book Collection in '{self.__name}':\n")
        for index, book in enumerate(self.__books, 1):
            print(f"{index}. {book}")


# --- Example Usage ---
book1 = Book("The Little Prince", "Antoine de Saint-Exupéry", "978-987-612-000-0")
book2 = Book("The Tunnel", "Ernesto Sabato", "978-950-731-731-0")
book3 = Book("Love in the Time of Cholera", "Gabriel García Márquez", "978-950-731-731-0")

library = Library("National Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()
