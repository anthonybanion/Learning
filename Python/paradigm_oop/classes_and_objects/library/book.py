"""
This module defines a Book class that represents a book in a library.
It includes methods for creating a book instance, displaying its details,
and static and class methods for getting book details and creating a book from a string.
 
File: book.py
Author: Anthony Bañon
Created: 2025-06-05
Last Updated: 2025-06-05
"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
    
    @staticmethod  # Static method to get book details
    def get_details(book):
        return f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}"
    
    @classmethod  # Class method to create a Book instance from a string
    def from_string(cls, book_string):
        title, author, isbn = book_string.split(',')
        return cls(title.strip(), author.strip(), isbn.strip())

# Example usage
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", "1234567890")
    print(book1)  # Output: '1984' by George Orwell (ISBN: 1234567890)
    
    book2 = Book.from_string("To Kill a Mockingbird, Harper Lee, 0987654321")
    print(book2)  # Output: 'To Kill a Mockingbird' by Harper Lee (ISBN: 0987654321)
    
    print(Book.get_details(book1))  # Output: Title: 1984, Author: George Orwell, ISBN: 1234567890
    print(Book.get_details(book2))  # Output: Title: To Kill a Mockingbird, Author: Harper Lee, ISBN: 0987654321