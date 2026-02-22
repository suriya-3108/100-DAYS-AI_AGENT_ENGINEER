"""
Task 2 — File Reading
🎯 Objective:

Read and display file content.

📝 Instructions:

Open users.txt
Print entire content properly
Handle error if file doesn’t exist (use try-except)
"""
try:
    with open('data.txt','r') as f:
    
        content = f.read()
    
        print(content)
except FileNotFoundError:
    print("File  not exist to read the content")