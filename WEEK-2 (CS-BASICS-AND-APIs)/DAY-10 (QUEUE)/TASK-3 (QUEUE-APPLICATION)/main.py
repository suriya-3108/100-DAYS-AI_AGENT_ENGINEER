from collections import deque

queue = deque()

# User entering the job's name and pages
def enter_value():
    name = input("Enter the job's name: ")
    pages = int(input("Enter pages: "))
    
    queue.append({'NAME': name, 'PAGE': pages, 'PROCESS': None})
    print("The task added successfully!!!")
    
# Display to the user 
def display():
    for each in queue:
            print(f"The job's name: {each['NAME']} The total pages is: {each['PAGE']}")

# Add process whether pending / Completed
def process():
    name = input("Enter job's name: ")
    for each in queue:
        if name == each['NAME']:
            procedure = input("Enter pending/completed: ")
            each['PROCESS'] = procedure
    print("you process updated!!!")
    

# check the completed process task
def complete():
    for each in list(queue):
        if each['PROCESS'] == 'completed':
            res = each
            queue.remove(each)
    print(f"The completed task is : {res}")
    return

print("""-----------------
      1. Add job's  name
      2. Change the process
      3. To remove the completed task
      4. Display the queue
      5. Exit 
      --------------------""")

while True:
    n = int(input("enter a number: ")) 
    match(n):
        case 1:
            enter_value()
        case 2:
            process()
        case 3:
            complete()
        case 4:
            display()
        case 5:
            break
        case _:
            print("Enter valid number???")
        