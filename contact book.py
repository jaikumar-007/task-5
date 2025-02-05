# Contact Management System

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
        return
    for contact in found_contacts:
        print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")

def update_contact():
    search_term = input("Enter name or phone number to update: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print(f"Current details: {contact}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print("Contact updated successfully!")
            return
    print("No contact found to update.")

def delete_contact():
    search_term = input("Enter name or phone number to delete: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("No contact found to delete.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
