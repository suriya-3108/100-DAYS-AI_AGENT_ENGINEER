"""Task 4: Custom Error Message Validator
Ask user to enter age.
Rules:

Age must be number
Age must be > 0
Age must be < 120

If invalid:
Raise your own ValueError using raise

Goal:
Learn to raise exceptions manually"""

class Agelessthanzero(Exception):
    pass

class Agegreaterthan(Exception):
    pass

try:
    age = int(input("Enter age: "))
    
    if age <= 0:
        raise Agelessthanzero("Age must be greater than zero")
    elif age > 120:
        raise Agegreaterthan("Age must be lesser than 120")
    
except Agelessthanzero as e:
    print(e)
    
except Agegreaterthan as f:
    print(f)
    
finally:
    print("program runned successfully!!!")
    
    