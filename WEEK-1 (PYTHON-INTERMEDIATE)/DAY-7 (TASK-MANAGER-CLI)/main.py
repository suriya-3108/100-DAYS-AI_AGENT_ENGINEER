obj = []

def task_add():
    
    id = int(input("Enter id: "))
    title = input("Enter the title: ")
    description = input("Enter ther description: ")
    status = input("Enter the status: ")
    priority = input("Enter the task priority: ")

    obj.append({'id':id, 'title':title, 'description': description, 'status': status, 'priority': priority})
    print("Task added successfully!!!")
    print('\n',obj,'\n')

def task_view():
    for each in obj:
        print("---------------------")
        print(each.get('id'))
        print(each.get('title'))
        print(each.get('status'))
        print(each.get('priority'))
        print("---------------------")

def update_task():
    user_title = input("enter the title which has to be update: ")

    for each in obj:
        if each['title'] == user_title:

        
            each['id'] = int(input("Enter new id: "))
            each['title'] = input("Enter new title: ")
            each['description'] = input("Enter new description: ")
            each['status'] = input("Enter new status: ")
            each['priority'] = input("Enter new priority: ")
            print("task updated")
            break
    else:
        print("the task not crearted!!!")
    
def delete_title():
        
    user_title = input("Enter title to delete: ")
        
    for each in obj:
        if each['title'] == user_title:
            obj.remove(each)
            print("the task deleted successfuly!!!")
            break
    else:
        print("no task presented")

def status_changer():
    user_title = input("Enter title to change status: ")

    for each in obj:
        if each['title'] == user_title:
            each['status'] = 'completed'
            print("task staus is changed")
            break
    else:
        print("no task is presented")
    

def search_by_title():
    print("\n searching....")
    user_title = input("Enter title to search: ")

    for each in obj:
        if each['title'] == user_title:
            print(each.get('id'))
            print(each.get('title'))
            print(each.get('status'))
            print(each.get('priority'))
            break
    else:
        print("no found!!!")
        
while True:
    n = int(input("select one number you fool: ")) 
  
    match(n):
        case 1:
            task_add()
        case 2:
            task_view()
        case 3:
            update_task()
        case 4:
            delete_title()
        case 5:
            status_changer()
        case 6:
            search_by_title()
        case _:
            break

