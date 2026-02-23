"""Task 2: Multiple Exception Handling

Ask user to enter:
A number
An index position

Use:
numbers = [10, 20, 30, 40]

Handle:
ValueError (if input is not number)
IndexError (invalid index)

Goal: Handle multiple exceptions properly"""

try:
    index_input = int(input("Enter index: "))
    
    numbers = [10, 20, 30, 40]
    
    print(f"Value at index {index_input} is {numbers[index_input]}")

except ValueError:
    print("Please enter a valid integer!")

except IndexError:
    print("Index out of range!")

finally:
    print("Program executed successfully!!!")
    