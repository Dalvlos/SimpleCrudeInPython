#CREATE
#READ
#UPDATE
#DELETE
1
contacts = []

def create_contact(name, phone):
    contact = {'name' : name, 'phone': phone}
    contacts.append(contact)
    print(f'{name} has been added to your contact list!')

def read_contacts():
    if not contacts:
        print('Contact list is empity')
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f'{idx}. Name: {contact['name']}, Phone Number: {contact['phone']}')

def update_contact(index, name=None, phone=None):
    if 0<= index < len(contacts):
        if name:
            contacts[index]['name'] = name
        if phone:
            contacts[index]['phone'] = phone
        print(f'Contact {index + 1} updated successfully.')
    else:
        print('Invalid index.')

def delete_contact(index):
    if 0 <= index <len(contacts):
        removed_contact = contacts.pop(index)
        print(f'{removed_contact['name']} was removed.')
    else:
        print('Invalid index')

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Add contact")
        print("2. Contact list")
        print("3. Contact Update")
        print("4. Contact Delete")
        print("5. Exit")

        choice = input("Choose one of the options: ")
        if choice == '1':
            name = input('Name: ')
            phone = input('Telphone: ')
            create_contact(name, phone)

        elif choice == '2':
            read_contacts()

        elif choice == '3':
            index = int(input('Contact index to update:')) -1
            if 0 <= index < len(contacts):
                name = input('New name: ')
                phone = input('New Tel/Cel: ')
                update_contact(index, name or None, phone or None)
        
        elif choice == '4':
            index = int(input('Contact index  to delete: ')) -1
            delete_contact(index)
        
        elif choice == '5':
            break
        
        else:
            print('invalid option.')

menu()