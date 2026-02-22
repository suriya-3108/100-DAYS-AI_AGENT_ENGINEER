"""Task 4 — Delete a User (Challenging)
🎯 Objective:

Delete a user by name.

Hint:
Read all data
Store in list
Rewrite file excluding that record"""


user_name = input("enter your name: ")

arr = []

try:
    with open('data.txt','r') as f:
        content = f.read()
        res = content.split('\n')
        for result in res:
            if f"name:{user_name}"in res:
                continue
            arr.append(result)
            
except FileNotFoundError:
    print("file not found")
    
file = open('data.txt','w')

file.writelines(arr)

file.close()

