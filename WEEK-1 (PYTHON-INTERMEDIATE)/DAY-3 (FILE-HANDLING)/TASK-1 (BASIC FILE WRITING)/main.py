"""
Task 1 — Basic File Writing
🎯 Objective:

Create a file and write user data into it.

📝 Instructions:

Ask user for:
Name
Age
City

Store the data in a file called users.txt
Format inside file like this:
"""

user_name = input("Enter your name: ")

user_age = input("Enter your age: ")

user_city = input("Enter your city: ")

# Creating a file and appending the data given by user

with open('data.txt','a') as f:
    
    f.write(f"USER'S NAME: {user_name}\n")
    f.write(f"USER'S AGE: {user_age}\n")
    f.write(f"USER'S CITY: {user_city}\n")




