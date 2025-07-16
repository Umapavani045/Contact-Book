import sqlite3
from os import system

# Create or connect to database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create contacts table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        name TEXT PRIMARY KEY,
        address TEXT,
        phone TEXT,
        email TEXT
    )
''')
conn.commit()

def new_contact():
    while True:
        print("\nPlease enter the following details:")
        name = input("> Name: ")
        address = input("> Address: ")
        phone = input("> Phone number: ")
        email = input("> Email address: ")

        try:
            cursor.execute('INSERT INTO contacts VALUES (?, ?, ?, ?)', (name, address, phone, email))
            conn.commit()
            print("\nContact details saved successfully ✓")
        except sqlite3.IntegrityError:
            print("\nA contact with this name already exists.")

        if input("Do you want to add another contact (y/n) ?: ").lower() != 'y':
            break

def view_details():
    cursor.execute('SELECT name FROM contacts')
    rows = cursor.fetchall()
    if not rows:
        print("You don't have any contacts saved! Consider adding a few new contacts.")
        return

    while True:
        print("-------- Your Contacts --------")
        for row in rows:
            print(f"> {row[0]}")

        name_info = input("\nEnter the name of the Contact whose details you wish to view: ")

        cursor.execute('SELECT * FROM contacts WHERE name = ?', (name_info,))
        contact = cursor.fetchone()
        if contact:
            print(f"\n---- Contact Details for {contact[0]} ----")
            print(f"> Address: {contact[1]}")
            print(f"> Phone: {contact[2]}")
            print(f"> Email: {contact[3]}")
        else:
            print("\nThe Contact name entered does not exist")

        if input("Do you wish to view your contacts again (y/n) ?: ").lower() != 'y':
            break

def edit_contact():
    cursor.execute('SELECT name FROM contacts')
    rows = cursor.fetchall()
    if not rows:
        print("You don't have any contacts saved! Consider adding a few new contacts.")
        return

    while True:
        print("\n-------- Your Contacts --------")
        for row in rows:
            print(f"> {row[0]}")

        name_edit = input("\nEnter the name of the Contact you want to edit: ")
        cursor.execute('SELECT * FROM contacts WHERE name = ?', (name_edit,))
        contact = cursor.fetchone()
        if contact:
            print("\nPlease write the attribute you want to change, and the new data in the below format:\n<attribute>|<new_value>")
            print("\nAttributes you can edit:\n|--address--|\n|---phone---|\n|---email---|")
            user_edit = input().split('|')
            attr, new_value = user_edit[0], user_edit[1]

            if attr in ['address', 'phone', 'email']:
                cursor.execute(f'UPDATE contacts SET {attr} = ? WHERE name = ?', (new_value, name_edit))
                conn.commit()
                print("\nContact details updated successfully ✓")
            else:
                print("\nInvalid attribute.")
        else:
            print("\nThe Contact name entered does not exist.")

        if input("Do you want to edit another contact (y/n) ?: ").lower() != 'y':
            break

def del_contact():
    cursor.execute('SELECT name FROM contacts')
    rows = cursor.fetchall()
    if not rows:
        print("You don't have any contacts saved! Consider adding a few new contacts.")
        return

    while True:
        print("\n-------- Your Contacts --------")
        for row in rows:
            print(f"> {row[0]}")

        name_del = input("\nEnter the name of the Contact to delete\n[Or type 'DEL_ALL' to delete all contacts]: ")

        if name_del == 'DEL_ALL':
            confirm = input('Type "CONFIRM" to delete all contacts: ')
            if confirm == 'CONFIRM':
                cursor.execute('DELETE FROM contacts')
                conn.commit()
                print("All contacts deleted successfully ✓")
            else:
                print("Contacts were not deleted.")
        else:
            cursor.execute('DELETE FROM contacts WHERE name = ?', (name_del,))
            if cursor.rowcount:
                conn.commit()
                print("Contact deleted ✓")
            else:
                print("The Contact name entered does not exist.")

        if input("Do you want to delete another contact (y/n) ?: ").lower() != 'y':
            break

def contactBook():
    while True:
        system('cls')  # For Windows; use 'clear' on Linux/macOS
        print("------------ Contact Book ------------")
        print("Enter:\n[0] Add New Contact\n[1] View Contacts\n[2] Edit Contact\n[3] Delete Contact")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                new_contact()
            elif choice == 1:
                view_details()
            elif choice == 2:
                edit_contact()
            elif choice == 3:
                del_contact()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

        if input("\nDo you want to open your Contact Book again (y/n) ?: ").lower() != 'y':
            break

contactBook()

# Close DB connection when done
conn.close()
