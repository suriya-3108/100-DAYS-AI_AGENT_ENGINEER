contact_details = {}

def contact_manager():
    print("""=== CONTACT MANAGER ===
    1. Add contact
    2. View all contacts
    3. Search contact
    4. Delete contact
    5. Exit""")
    while True:
        option = int(input("choose: "))
    
        match (option):
            case 1:
                name = input("Enter your name: ")
                phone_number = int(input("Enter your Phno: "))
                contact_details["name"] = name
                contact_details["phone_number"] = phone_number
                print(f" ✓ {name} Successfully Added!!!\n")
            
            case 2:
                print("YOUR CONTACTS:")
                for name , phone_number in contact_details.items():
                    print(f"{name}:{phone_number}\n")
                
            case 3:
                NAME = input("Enter your name: ")
                if contact_details.get("name") == NAME:
                    print(f"✓ Found: {contact_details['name']} -> {contact_details['phone_number']}\n")
                    
            case 4:
                user_name = input("Enter your name: ")
                if contact_details.get("name") == user_name:
                    contact_details.clear()
                    print(f"{user_name} deleted Sucessfully!!!\n")
        
            case 5:
                break
        
            case _:
                print("Enter a valid number!!!\n")
 
           
contact_manager()