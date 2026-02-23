"""
Bonus Advanced Practice
Task 5: Retry Logic

Create a program that:

Gives user 3 attempts to enter correct password
If failed 3 times → raise Exception and exit

This is used in authentication systems."""

class Passwordmmismatch(Exception):
    pass

password = '12345'
attempt = 3

while attempt > 0:
    user_pass = input("Enter password: ")
    
    if user_pass == password:
        print("Login sucess!!!")
        break
    else:
        attempt -= 1
        print(f"your balance attempt to try {attempt}")
    
if attempt == 0:
    raise Passwordmmismatch("enter valid password!!!")
    