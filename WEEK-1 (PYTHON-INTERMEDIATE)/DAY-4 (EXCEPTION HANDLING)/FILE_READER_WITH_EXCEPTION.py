"""Task 3: File Reader with Exception Handling

Create a program that:
Asks user for a filename
Opens and reads the file

Handles:
FileNotFoundError
PermissionError
Any other exception using generic Exception as e

Goal:
Practice file handling + exceptions together
Use else block properly"""

try:
    file_name = input("enter a file name: ")
    
    with open(file_name,'r') as file:
        content = file.read()
    
except FileNotFoundError as e:
    print(e)

except PermissionError as p:
    print(p)
    
except Exception as s:
    print("Something unexpected happened:", s)

else:
    print(f"The file content is:{content}")

finally:
    print("operation done successfully!!!")