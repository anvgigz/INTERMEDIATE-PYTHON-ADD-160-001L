import os
import pickle

class AddressBook:
    def __init__(self, filename='address_book.pkl'):
        self.filename = filename
        self.entries = self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return {}

    def save(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.entries, f)
        print("Changes saved.")

    def add_user(self, first_name, last_name, phone, email):
        key = f"{first_name.lower()}_{last_name.lower()}"
        self.entries[key] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email
        }
        print(f"User {first_name} {last_name} added.")
        self.save()

    def search_user(self, first_name, last_name):
        key = f"{first_name.lower()}_{last_name.lower()}"
        user = self.entries.get(key)
        if user:
            print(f"Found: {user}")
        else:
            print("User not found.")

    def change_user(self, first_name, last_name, new_first, new_last, new_phone, new_email):
        key = f"{first_name.lower()}_{last_name.lower()}"
        if key in self.entries:
            new_key = f"{new_first.lower()}_{new_last.lower()}"
            self.entries[new_key] = {
                "first_name": new_first,
                "last_name": new_last,
                "phone": new_phone,
                "email": new_email
            }
            del self.entries[key]
            print(f"User {first_name} {last_name} updated.")
            self.save()
        else:
            print("User not found.")

    def delete_user(self, first_name, last_name):
        key = f"{first_name.lower()}_{last_name.lower()}"
        if key in self.entries:
            del self.entries[key]
            print(f"User {first_name} {last_name} deleted.")
            self.save()
        else:
            print("User not found.")
            
            
