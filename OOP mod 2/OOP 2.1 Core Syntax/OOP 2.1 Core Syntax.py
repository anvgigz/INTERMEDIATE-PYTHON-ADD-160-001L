
#Class to allow for employee contact management
class AddressBook:
    """Class to represent an address book entry.

    Attributes:
    first_name: The first name of the employee.
    last_name: The last name of the employee.
    birthday: The birthday of the employee.
    email: The email address of the employee.
    street_address: The street address of the employee.
    city: The city where the employee lives.
    state: The state where the employee lives.
    zip: The ZIP code of the employee's address.
    phone: The phone number of the employee.

    Methods:
    Getter and setter methods created for all employee attributes
    string function to allow for pretty print of employee info
    representation function to allow for dev friendly string of employee info
    comparison function to allow for employee equality checks
    """

    def __init__(self, first_name, last_name, birthday, email, street_address, 
                 city, state, zip, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, value):
        self._birthday = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def street_address(self):
        return self._street_address
    
    @street_address.setter
    def street_address(self, value):
        self._street_address = value

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        self._city = value

    @property
    def state(self):
        return self._state
    
    state.setter
    def state(self, value):
        self._state = value

    @property
    def zip(self):
        return self._zip
    
    @zip.setter
    def zip(self, value):
        self._zip = value

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone = value
    


#custom str function to pretty print employee info
    def __str__(self):
        return f"""Here is the info for {self.first_name} {self.last_name}
birthday: {self.birthday}\nemail: {self.email}\nstreet_address:{self.street_address}
city: {self.city}\nstate: {self.state}\nzip: {self.zip}\nphone: {self.phone}  """

#custom repr function to provide a detailed string representation of the employee
    def __repr__(self):
        return (f"AddressBook({self.first_name!r}, {self.last_name!r}, {self.birthday!r} "
                f"{self.email!r}, {self.street_address!r}. {self.city!r}, "
                f"{self.state!r}, {self.zip!r}, {self.phone!r})")

#custom equality function to compare employees
    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return f"This employee has duplicate accounts"
        else: 
            return f"this employee has no duplicate accounts"

        

employee1 = AddressBook("John", "Doe", "1990-01-01", "john.doe@exampleemail.com",
                        "123 Elm St", "Somewhere", "CA", "90210", "333-4444-4444")

employee2 = AddressBook("Joe", "Snow", "1992-02-02", "joe.snow@example.com",
                        "456 Oak St", "Anywhere", "NY", "10001", "444-555-6666")

print(str(employee1))
print(repr(employee1))

print(employee1 == employee2)

print(employee1.first_name)

employee1.first_name = "Jane"
print(employee1.first_name)