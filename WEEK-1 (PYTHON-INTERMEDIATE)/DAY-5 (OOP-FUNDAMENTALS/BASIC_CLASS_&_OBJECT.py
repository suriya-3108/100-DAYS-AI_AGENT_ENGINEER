"""Question 1 — Basic Class & Object (Warm-up)
Create a class called Student.

Requirements:
Attributes: name, age, course
Create a method introduce() that prints:
Hi, I am <name>, <age> years old, studying <course>"""

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old, studying {self.course}")

s1 = Student('suriya','21','IT')
s2 = Student('arun', '20', 'IT')

s1.introduce()
s2.introduce()
    
    
        