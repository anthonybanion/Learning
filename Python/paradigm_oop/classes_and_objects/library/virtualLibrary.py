#Brief: Sistema de Gestión de Biblioteca Digital
#Date: 25/11/2021
#Version: 2.0


"""
Statement:
 This system allows you to manage a digital library,
 including registering books, users, and managing loans.
 Users can borrow books for a specified period of time and
 return them. The library offers functions for adding books,
 listing available books, registering users, and displaying active loans.
"""
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Person(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def show_info(self):
        pass

    def get_name(self):
        return self.__name


class Author(Person):
    def __init__(self, name):
        super().__init__(name)
        self._books_written = []

    def show_info(self):
        return f"Author: {self.get_name()}"

    def write_book(self, book):
        self._books_written.append(book)

    def get_books(self):
        return self._books_written


class User(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self._email = email
        self._borrowed_books = []

    def show_info(self):
        return f"User: {self.get_name()}, Email: {self._email}"

    def borrow_book(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)

    def get_borrowed_books(self):
        return self._borrowed_books


class Book:
    def __init__(self, title, author, page_count):
        self.__title = title
        self.__author = author
        self.__page_count = page_count
        self.__is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.__is_borrowed else "Available"
        return f"{self.__title} - {self.__author.get_name()} - {self.__page_count} pages - {status}"

    def mark_as_borrowed(self):
        self.__is_borrowed = True

    def mark_as_returned(self):
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def is_borrowed(self):
        return self.__is_borrowed

    def get_author(self):
        return self.__author


class Loan:
    def __init__(self, user, book, borrow_date, return_date):
        self._user = user
        self._book = book
        self.__borrow_date = borrow_date
        self.__return_date = return_date

    def show_info(self):
        return (f'Loan of "{self._book.get_title()}" to {self._user.get_name()} - '
                f'Borrowed on: {self.__borrow_date.strftime("%Y-%m-%d")}, '
                f'Due by: {self.__return_date.strftime("%Y-%m-%d")}')


class BookCatalog:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def search_by_title(self, title):
        return [book for book in self._books if title.lower() in book.get_title().lower()]

    def list_books(self):
        return "\n".join(str(book) for book in self._books)


class UserManager:
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def search_by_name(self, name):
        return [user for user in self._users if name.lower() in user.get_name().lower()]

    def list_users(self):
        return "\n".join(user.show_info() for user in self._users)


class Library:
    def __init__(self):
        self.catalog = BookCatalog()
        self.user_manager = UserManager()
        self._loans = []

    def register_book(self, book):
        self.catalog.add_book(book)

    def register_user(self, user):
        self.user_manager.add_user(user)

    def make_loan(self, user, book, borrow_date, return_date):
        if book not in self.catalog._books:
            raise ValueError("Book not found in catalog.")
        if book.is_borrowed():
            raise ValueError("Book is currently borrowed.")
        book.mark_as_borrowed()
        user.borrow_book(book)
        loan = Loan(user, book, borrow_date, return_date)
        self._loans.append(loan)

    def return_book(self, user, book):
        for loan in self._loans:
            if loan._book == book and loan._user == user:
                book.mark_as_returned()
                user.return_book(book)
                self._loans.remove(loan)
                return
        raise ValueError("Loan not found.")

    def list_loans(self):
        return "\n".join(loan.show_info() for loan in self._loans)


# --- Main Script ---

library = Library()

# Authors
author1 = Author("Antoine de Saint-Exupéry")
author2 = Author("Gabriel García Márquez")

# Books
book1 = Book("The Little Prince", author1, 96)
book2 = Book("One Hundred Years of Solitude", author2, 417)

author1.write_book(book1)
author2.write_book(book2)

# Register books
library.register_book(book1)
library.register_book(book2)

# Users
user1 = User("John Smith", "john.smith@example.com")
user2 = User("Mario", "mario@gmail.com")

library.register_user(user1)
library.register_user(user2)

# Make loan
today = datetime.now()
due_date = today + timedelta(days=7)

library.make_loan(user1, library.catalog.search_by_title("The Little Prince")[0], today, due_date)

try:
    library.make_loan(user2, library.catalog.search_by_title("The Little Prince")[0], today, due_date)
except ValueError as e:
    print(f"Error: {e}")

# Display
print("Books in the catalog:")
print(library.catalog.list_books())

print("\nActive loans:")
print(library.list_loans())

# Uncomment to test return
# library.return_book(user1, book1)

print("\nUpdated book status:")
print(library.catalog.list_books())

