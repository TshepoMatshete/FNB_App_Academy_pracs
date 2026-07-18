# Store contacts as a list of dictionaries, each with keys: name, phone, email
# Implement an add_contact() function that appends a new dictionary to the list
# Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
# Implement a delete_contact(name) function that removes a contact by name
# Implement a view_all() function that displays all contacts in a formatted layout
# Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)

contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

def delete_contact(name):
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)

def view_all():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        
        
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter the name to search: ")
        contact = search_contact(name)
        if contact:
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter the name to delete: ")
        delete_contact(name)
        print(f"Deleted contact with name: {name}")
    elif choice == "4":
        view_all()
    elif choice == "5":
        break
    else:
        print("Invalid option, please try again.")