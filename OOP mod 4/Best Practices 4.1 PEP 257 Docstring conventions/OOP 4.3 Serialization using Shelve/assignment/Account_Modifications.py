
import shelve

class AddressBook:
    def __init__(self, filename='address_book.db'):
        self.filename = filename

    def add_user(self, first_name, last_name, phone, email):
        key = f"{first_name.lower()}_{last_name.lower()}"
        with shelve.open(self.filename, writeback=True) as db:
            db[key] = {
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "email": email
            }
            print(f"User {first_name} {last_name} added.")


    def search_user(self, first_name, last_name):
        key = f"{first_name.lower()}_{last_name.lower()}"
        with shelve.open(self.filename) as db:
            user = db.get(key)
            if user:
                print(f"Found: {user}")
            else:
                print("User not found.")


    def change_user(self, first_name, last_name, new_first, new_last, new_phone, new_email):
        old_key = f"{first_name.lower()}_{last_name.lower()}"
        new_key = f"{new_first.lower()}_{new_last.lower()}"
        with shelve.open(self.filename, writeback=True) as db:
            if old_key in db:
                db[new_key] = {
                    "first_name": new_first,
                    "last_name": new_last,
                    "phone": new_phone,
                    "email": new_email
                }
                del db[old_key]
                print(f"User {first_name} {last_name} updated.")
            else:
                print("User not found.")


    def delete_user(self, first_name, last_name):
        key = f"{first_name.lower()}_{last_name.lower()}"
        with shelve.open(self.filename, writeback=True) as db:
            if key in db:
                del db[key]
                print(f"User {first_name} {last_name} deleted.")
            else:
                print("User not found.")

