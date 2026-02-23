"""Level 1 — Basic Try/Except Practice
Task 1: Safe Division Program

Create a program that:
Takes two numbers from user
Divides them

Handles:
ZeroDivisionError
ValueError
Always prints "Program finished" using finally

Goal: Practice try, except, finally"""

try:
    num1 = int(input("Enter number-1: "))
    num2 = int(input("Enter number-2: "))
    div = num1/num2
     
except ValueError as e:
    print(e)

except ZeroDivisionError as f:
    print(f)

else:
    print(f"the divided values is:{div}")
    
finally:
    print("Program Finished")