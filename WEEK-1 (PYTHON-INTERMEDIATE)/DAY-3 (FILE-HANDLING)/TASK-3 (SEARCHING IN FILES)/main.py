"""Task 3 — Search in File
🎯 Objective:

Search for a user by name.
Ask user to enter name
Search inside file
If found → print that full record
If not → print "User not found" """

user_name = input("Enter yor name: ")
try:
    
    with open ('data.txt', 'r') as f:
        content = f.read()

    if user_name in content:
        print(content)
    else:
        print("user not found!")

except FileNotFoundError:
    print("File doesnt exist!!!")

