# Assignment: 03 - Library Inventory System
# Author: Harsh Sharma
# Date: 2025-11-22
# Description: Main script for the interactive library console application (Task 6).

from library import Library
import uuid

def display_menu():
    print("\n=============================================")
    print("      LIBRARY INVENTORY SYSTEM MENU")
    print("=============================================")
    print("1. Add New Book")
    print("2. Register New Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report (Analytics)")
    print("6. Exit")
    print("---------------------------------------------")

def add_book_menu(library):
    print("\n--- Add New Book ---")
    title = input("Enter book Title: ")
    author = input("Enter book Author: ")
    isbn = input("Enter book ISBN (e.g., 123456): ") 
    library.add_book(title, author, isbn)

def register_member_menu(library):
    print("\n--- Register New Member ---")
    name = input("Enter member Name: ")
    member_id = str(uuid.uuid4())[:8] 
    library.register_member(name, member_id)

def borrow_book_menu(library):
    print("\n--- Borrow Book ---")
    member_id = input("Enter Member ID: ")
    isbn = input("Enter Book ISBN: ")
    library.lend_book(member_id, isbn)

def return_book_menu(library):
    print("\n--- Return Book ---")
    member_id = input("Enter Member ID: ")
    isbn = input("Enter Book ISBN: ")
    library.take_return(member_id, isbn)


def main():
    print("=" * 50)
    print("        WELCOME TO KRM LIBRARY SYSTEM")
    print("=" * 50)

    library = Library()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_book_menu(library)
        elif choice == '2':
            register_member_menu(library)
        elif choice == '3':
            borrow_book_menu(library)
        elif choice == '4':
            return_book_menu(library)
        elif choice == '5':
            library.generate_report()
        elif choice == '6':
            print("\nThank you for using the Library System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()