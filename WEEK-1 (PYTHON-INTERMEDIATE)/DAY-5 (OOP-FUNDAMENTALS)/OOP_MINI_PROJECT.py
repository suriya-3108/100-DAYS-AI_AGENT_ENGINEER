"""Question 5 — OOP Mini Project — Library System
Create a class Book.

Attributes:
title
author
available (default True)

Methods:
borrow_book()
return_book()
display_status()

Rules:
Cannot borrow if already borrowed
Cannot return if already available"""

class Book:
    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available
    
    def borrow_book(self):
        if self.available:
            print(f"you can borrow the {self.title} book , written by {self.author}")
            self.available = not self.available
        else:
            print(f"you can't borrow the book , because its not available!!!")
    def return_book(self):
        if self.available:
            print(f"you cant return it!")
        else:
            print("thanks for returning the book!!!")
            self.available = not self.available
    
    def display_status(self):
        print(f"BOOK_NAME: {self.title}")
        print(f"BOOK_AUTHOR: {self.author}")
        print(f"AVAILABLE: {self.available}")

user = Book('agni siragugal', 'DR.A.P.J ABDUL KALAM SIR')
    
user.display_status()

user.borrow_book()

user.return_book()