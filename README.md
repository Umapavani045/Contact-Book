📒 Contact Book (Python + SQLite)
A simple command-line Contact Book built in Python that stores your contacts in an SQLite database.
This app helps you manage contacts easily: add, view, edit, and delete — all saved safely in a local .db file.

✨ Features
✅ Add new contacts with name, address, phone, and email
✅ View saved contacts and their full details
✅ Edit contact details (address, phone, or email)
✅ Delete single contacts or remove all contacts at once
✅ Data is stored persistently in a local contacts.db file using SQLite

🛠 How to Run
Make sure Python is installed
Recommended: Python 3.7 or newer

Save the code
Copy the code into a file named, e.g., contact_book_sqlite.py.

Run the script
Open terminal (or command prompt) and run:

bash
Copy
Edit
python contact_book_sqlite.py
The first time you run it, it will automatically create a database file named contacts.db.

📌 Usage Guide
When you run the program, you'll see:

sql
Copy
Edit
------------ Contact Book ------------
Enter:
[0] Add New Contact
[1] View Contacts
[2] Edit Contact
[3] Delete Contact
Enter the number corresponding to your action.
Follow prompts to add or edit details.
You can repeat actions until you choose to exit.

Example
Adding a contact:

markdown
Copy
Edit
> Name: Alia
> Address: Wonderla
> Phone number: 123456789
> Email address: alia@example.com

Contact details saved successfully ✓
->>After this the added new contacts get saved to sql data base and  separate file in the folder is created which stores the data base data of contact book
