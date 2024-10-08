contacts = []

def add_contact():
    name = input("\nEnter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("\nEnter name or phone number to search: ")
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]

    if results:
        print("\nSearch Results:")
        for contact in results:
            print(
                f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print(f"\nNo contacts found matching '{query}'.")

def update_contact():
    search_contact()
    name_to_update = input("\nEnter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name_to_update.lower():
            print(f"\nUpdating contact '{contact['name']}'")
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print(f"\nContact '{contact['name']}' updated successfully!\n")
            return
    print(f"\nContact '{name_to_update}' not found.")

def delete_contact():
    view_contacts()
    name_to_delete = input("\nEnter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name_to_delete.lower():
            contacts.remove(contact)
            print(f"\nContact '{name_to_delete}' deleted successfully!")
            return
    print(f"\nContact '{name_to_delete}' not found.")

def display_menu():
    print("\n---- Contact Management System ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option: ")

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
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
