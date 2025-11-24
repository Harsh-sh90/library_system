Project Information
---------------------------
Name: Harsh Sharma 
Roll No:2501940054 
University Name: K.R. Mangalam University 
Date:24-11-2025 
Assignment:03 -  Python Object-Oriented Library Inventory System


  Summary
-----------
This project implements a Library Inventory System using Python and Object-Oriented Programming (OOP) principles. The system models real-world objects like Book and Member to manage a library's collection, track borrowing and returning operations, and store the system's data for persistence.
The assignment is part of the course Programming for Problem Solving Using Python (Course Code: ETCCPP171) for the MCA (AI & ML) program, Semester I. It focuses on applying OOP concepts, modular design, and file handling.


  Main Points and Implementation Details
------------------------------------------
- Objective: To design and implement classes, use attributes/methods, apply modular design, and achieve file persistence.
- Modular Structure: The project is organized into multiple Python files within a library_system folder:
- book.py: Defines the Book class.
- member.py: Defines the Member class.
- library.py: Defines the central Library class for management logic.
- main.py: Contains the program entry point and user interface.
- Core Functionality: The Library class supports:
    a.Adding books (add_book()).
    b.Registering members (register_member()).
    c.Lending books (lend_book()).
    d.Handling returns (take_return()).
-File Persistence (Task 4): Data for books and members is saved to and loaded from files (JSON or CSV format) to ensure data is preserved across program runs. Includes error handling for files.
-Analytics (Task 5): The system includes a class-level analytic feature (e.g., Most borrowed book, Total active members, or Number of books currently borrowed).
-Interactive Console (Bonus Task 6): An interactive menu in main.py allows users to perform operations like adding, registering, borrowing, returning, and viewing the report.
