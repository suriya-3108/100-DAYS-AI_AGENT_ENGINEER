"""Question 4 — Class Variable vs Instance Variable

Create a class Company.

Requirements:
Class variable: company_name = "TechCorp"
Instance variables: employee_name
Method display_details()

Create 3 employees and:
Print company name using class
Print company name using object
Change company name and observe behavior

Understand:
👉 Difference between class and instance variable"""

class Company:
    company_name = "Techcorp"
    
    def __init__(self,employee_name):
            self.employee_name = employee_name
    
    def display_detail(self):
        print(f"the emloyee is: {self.employee_name}")
        print(f"the company name is: {Company.company_name}")

com = Company('suriya')

print(f"the company is : {Company.company_name}")

print(f"the company name by object {com.company_name} ")

com.company_name = "arun & co"

print(com.company_name)

Company.company_name = "suriya & Co"

print(Company.company_name)