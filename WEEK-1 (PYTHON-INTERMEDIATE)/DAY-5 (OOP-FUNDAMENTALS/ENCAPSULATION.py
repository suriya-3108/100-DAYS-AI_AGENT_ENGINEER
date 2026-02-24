"""Question 3 — Encapsulation (Private Variables)
Create a class Employee.
Requirements:

Private attribute: __salary
Public attributes: name, role
Method get_salary() → return salary
Method increase_salary(amount) → increase salary safely

Try:

Accessing salary directly (should not work properly)
Accessing using method"""

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.__salary = salary 
    
    def get_salary(self):
        return self.__salary
    
    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print("Salary increased successfully.")
        else:
            print("Increase amount must be positive.")
        
    