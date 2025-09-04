

def conference_signup(*participants, **Phone_Email):
    if participants:
        names = ", ".join(participants)
        Phone = Phone_Email.get("Phone", "No phone provided")
        Email = Phone_Email.get("Email", "No email provided")
        print(f"""Contact Info\nName:{names}\nPhone:{Phone}\nEmail:{Email}
--------------------------------------------------------------------------""")
    else:
        print("No participants have signed up yet.")

conference_signup("John Doe", Phone="555-1234", Email="john@example.com")
conference_signup("Bob", Phone="987-345-1234", Email="bob@example.com")
conference_signup("Charlie", Email="Charlie@example.com")



