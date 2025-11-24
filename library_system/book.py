# Assignment: 03 - Library Inventory System
# Author: [Your Name]
# Date: 2025-11-22
# Description: Defines the Book class with borrow and return functionality.

import json

class Book:
    """
    Represents a book in the library inventory.
    """
    def __init__(self, title, author, isbn, available=True):
        """
        Initializes a new Book instance.

        :param title: The title of the book (str).
        :param author: The author of the book (str).
        :param isbn: The International Standard Book Number (str).
        :param available: Availability status (bool, default True).
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        """Marks the book as not available (borrowed)."""
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """Marks the book as available (returned)."""
        if not self.available:
            self.available = True
            return True
        return False

    def to_dict(self):
        """Converts the Book object to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'available': self.available
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Book object from a dictionary."""
        return cls(data['title'], data['author'], data['isbn'], data['available'])

    def __str__(self):
        """String representation of the Book object."""
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - Status: {status}"

# Class-level analytic for tracking total books created
Book.total_books_created = 0
