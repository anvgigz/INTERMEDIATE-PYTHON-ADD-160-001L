import shelve

from Account_Modifications import AddressBook



def menu():
    book = AddressBook()

    while True:
        print("\n--- Address Book Menu ---")
        print("1. Add New User")
        print("2. Search for Existing User")
        print("3. Change Existing User")
        print("4. Delete Existing User")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            fn = input("First Name: ")
            ln = input("Last Name: ")
            phone = input("Phone Number: ")
            email = input("Email Address: ")
            book.add_user(fn, ln, phone, email)

        elif choice == '2':
            fn = input("First Name to search: ")
            ln = input("Last Name to search: ")
            book.search_user(fn, ln)

        elif choice == '3':
            fn = input("Current First Name: ")
            ln = input("Current Last Name: ")
            new_fn = input("New First Name: ")
            new_ln = input("New Last Name: ")
            new_phone = input("New Phone Number: ")
            new_email = input("New Email Address: ")
            book.change_user(fn, ln, new_fn, new_ln, new_phone, new_email)

        elif choice == '4':
            fn = input("First Name to delete: ")
            ln = input("Last Name to delete: ")
            book.delete_user(fn, ln)

        elif choice == '5':
            print("Exiting Address Book.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    menu()
