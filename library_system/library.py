# Assignment: 03 - Library Inventory System
# Author: [Your Name]
# Date: 2025-11-22
# Description: Defines the Library class for managing books, members, and file persistence.

import json
import os
from book import Book
from member import Member

class Library:
    """
    Manages the collection of books and members, and handles persistence.
    """
    BOOK_FILE = "books_data.json"
    MEMBER_FILE = "members_data.json"

    def __init__(self):
        """Initializes the library and attempts to load data from files."""
        # Stores Book objects keyed by ISBN
        self.books = {} 
        # Stores Member objects keyed by member_id
        self.members = {} 
        self._load_data()

    def _load_data(self):
        """Task 4: Loads book and member data from JSON files."""
        print("--- Loading data...")
        
        # Load Books
        if os.path.exists(self.BOOK_FILE):
            try:
                with open(self.BOOK_FILE, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        book = Book.from_dict(item)
                        self.books[book.isbn] = book
                    print(f"Loaded {len(self.books)} books successfully.")
            except Exception as e:
                print(f"Warning: Could not load book data (File: {self.BOOK_FILE}). Starting with empty book list. Error: {e}")
        else:
            print("Book data file not found. Starting with empty book list.")
            
        # Load Members
        if os.path.exists(self.MEMBER_FILE):
            try:
                with open(self.MEMBER_FILE, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        member = Member.from_dict(item)
                        self.members[member.member_id] = member
                    print(f"Loaded {len(self.members)} members successfully.")
            except Exception as e:
                print(f"Warning: Could not load member data (File: {self.MEMBER_FILE}). Starting with empty member list. Error: {e}")
        else:
            print("Member data file not found. Starting with empty member list.")
        print("--------------------")

    def _save_data(self):
        """Task 4: Saves book and member data to JSON files."""
        
        # Save Books
        book_data = [book.to_dict() for book in self.books.values()]
        try:
            with open(self.BOOK_FILE, 'w') as f:
                json.dump(book_data, f, indent=4)
            # print(f"Saved {len(book_data)} books to {self.BOOK_FILE}.")
        except Exception as e:
            print(f"Error saving book data: {e}")

        # Save Members
        member_data = [member.to_dict() for member in self.members.values()]
        try:
            with open(self.MEMBER_FILE, 'w') as f:
                json.dump(member_data, f, indent=4)
            # print(f"Saved {len(member_data)} members to {self.MEMBER_FILE}.")
        except Exception as e:
            print(f"Error saving member data: {e}")

    # --- Task 3: Core Library Operations ---

    def add_book(self, title, author, isbn):
        """Adds a new book to the library inventory."""
        if isbn in self.books:
            print(f"Error: Book with ISBN {isbn} already exists.")
            return False
            
        new_book = Book(title, author, isbn)
        self.books[isbn] = new_book
        Book.total_books_created += 1 # Update class-level analytic
        self._save_data()
        print(f"Success: Added book '{title}' (ISBN: {isbn}).")
        return True

    def register_member(self, name, member_id):
        """Registers a new member with the library."""
        if member_id in self.members:
            print(f"Error: Member with ID {member_id} already registered.")
            return False

        new_member = Member(name, member_id)
        self.members[member_id] = new_member
        Member.total_members_created += 1 # Update class-level analytic
        self._save_data()
        print(f"Success: Registered member '{name}' (ID: {member_id}).")
        return True

    def lend_book(self, member_id, isbn):
        """Lends a book to a member."""
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            print(f"Error: Member ID {member_id} not found.")
            return False
        if not book:
            print(f"Error: Book ISBN {isbn} not found.")
            return False
        if not book.available:
            print(f"Error: Book '{book.title}' is currently unavailable.")
            return False

        # Perform the transaction on both objects
        if book.borrow() and member.borrow_book(isbn):
            self._save_data()
            print(f"Success: '{book.title}' lent to {member.name}.")
            return True
        else:
            # Should not happen if previous checks pass, but for safety
            print("Transaction failed due to internal error.")
            return False

    def take_return(self, member_id, isbn):
        """Handles the return of a book by a member."""
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member:
            print(f"Error: Member ID {member_id} not found.")
            return False
        if not book:
            print(f"Error: Book ISBN {isbn} not found.")
            return False
        if isbn not in member.borrowed_books:
            print(f"Error: Book '{book.title}' was not recorded as borrowed by {member.name}.")
            return False

        # Perform the transaction on both objects
        if book.return_book() and member.return_book(isbn):
            self._save_data()
            print(f"Success: '{book.title}' returned by {member.name}.")
            return True
        else:
            # Should not happen if previous checks pass, but for safety
            print("Return transaction failed due to internal error.")
            return False

    # --- Task 5: Class-Level Analytics (Mini Report) ---

    def generate_report(self):
        """Generates and displays the library status report."""
        
        # 1. Number of books currently borrowed (Analytic chosen from Task 5)
        borrowed_count = sum(1 for book in self.books.values() if not book.available)
        
        # 2. Total number of active members (All members are considered active)
        active_members_count = len(self.members)
        
        # 3. Most borrowed book (Simple analysis)
        borrow_counts = {}
        for member in self.members.values():
            for isbn in member.borrowed_books:
                borrow_counts[isbn] = borrow_counts.get(isbn, 0) + 1

        most_borrowed_isbn = max(borrow_counts, key=borrow_counts.get) if borrow_counts else None
        
        report = "\n=============================================\n"
        report += "          LIBRARY ANALYTICS REPORT\n"
        report += "=============================================\n"
        report += f"Total Books in Inventory: {len(self.books)}\n"
        report += f"Total Registered Members: {active_members_count}\n"
        report += "---------------------------------------------\n"
        report += f"Number of Books Currently Borrowed: {borrowed_count}\n"
        
        if most_borrowed_isbn:
            book_title = self.books[most_borrowed_isbn].title if most_borrowed_isbn in self.books else "Unknown Title"
            report += f"Most Borrowed Book (Currently): '{book_title}' (Borrowed {borrow_counts[most_borrowed_isbn]} times)\n"
        else:
            report += "Most Borrowed Book (Currently): N/A (No books are currently borrowed)\n"

        report += "=============================================\n"
        print(report)