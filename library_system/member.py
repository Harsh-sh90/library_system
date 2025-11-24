# Assignment: 03 - Library Inventory System
# Author: [Your Name]
# Date: 2025-11-22
# Description: Defines the Member class with book tracking functionality.

class Member:
    """
    Represents a member registered with the library.
    """
    def __init__(self, name, member_id, borrowed_books=None):
        """
        Initializes a new Member instance.

        :param name: The member's name (str).
        :param member_id: The unique member ID (str).
        :param borrowed_books: List of ISBNs of books currently borrowed (list of str).
        """
        self.name = name
        self.member_id = member_id
        # borrowed_books stores a list of ISBN strings
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def borrow_book(self, isbn):
        """Adds an ISBN to the member's borrowed list."""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
            return True
        return False

    def return_book(self, isbn):
        """Removes an ISBN from the member's borrowed list."""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

    def list_books(self):
        """Returns the list of ISBNs currently borrowed by the member."""
        return self.borrowed_books

    def to_dict(self):
        """Converts the Member object to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'member_id': self.member_id,
            'borrowed_books': self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Member object from a dictionary."""
        return cls(data['name'], data['member_id'], data['borrowed_books'])

    def __str__(self):
        """String representation of the Member object."""
        return f"Member: {self.name} (ID: {self.member_id}), Borrowed: {len(self.borrowed_books)} books"

# Class-level analytic for tracking total members created
Member.total_members_created = 0