# Contact Management System

contacts = {}

def add_contact():
    print("\nAdd New Contact")

    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone

    print(f"Contact '{name}' added successfully!!\n")


def view_contacts():
    print("\nAll contacts listed below: ")

    if len(contacts) == 0:
        print("No contacts found.\n")
        return
    
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

    print()


def search_contact():
    name = input("\nEnter contact name to search: ")

    if name in contacts:
        print(f"{name}'s Number: {contacts[name]}\n")
    else:
        print("Contact was not found.\n")


def update_contact():
    name = input("\nEnter contact name to update: ")

    if name in contacts:
        new_number = input("Enter new phone number: ")
        contacts[name] = new_number
        print("Contact updated suvvessfully!\n")
    else:
        print("Contact not found.\n")


def delete_contact():
    name = input("\nEnter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!!\n")
    else:
        print("Contact not found.\n")        


def menu():
    while True:
        print("===== Contact Book =====")
        print("1. Add Contacts")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update COntact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid option.\n")

menu()