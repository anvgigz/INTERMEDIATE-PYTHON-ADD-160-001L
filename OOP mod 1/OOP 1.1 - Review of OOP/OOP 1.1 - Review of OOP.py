#book class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #method to display book details
    def display_details(self):
        print(f"title: {self.title}, author: {self.author}. pages: {self.pages}")

    #method to check if book is long
    def is_long_book(self):
        if self.pages > 100:
            print("TRUE")
            return True
        else:
            print("FALSE")
            return False

#create book instances
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Automate the Boring Stuff with Python", "Al Sweigart", 504)
book3 = Book("Python tools for data science", "Jake VanderPlas", 550)
book4 = Book("Go Dog Go", "P.D. Eastman", 72)

#testing methods
book1.display_details()
book2.display_details()
book3.display_details()
book4.display_details()

#testing methods
book1.is_long_book()
book2.is_long_book()
book3.is_long_book()
book4.is_long_book()

