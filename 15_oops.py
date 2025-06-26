# Real-World Scenarios



# Library System

# Create a Book class with attributes like title, author, and available_copies.
# Add methods to lend a book, return a book, and check availability.

class Book:
    def __init__(self,title,author, available_copies):
        self.title= title
        self.author= author
        self.available_copies= available_copies



    def lend_book(self):
        if self.available_copies > 0:
            self.available_copies -=1
            print("You borrowed a Book ")

        else:
            print("Copies n ot available")



    def return_book(self):
        self.available_copies +=1
        print("You returned the Book")

    def checkAvailablity(self):
        return self.available_copies
    



book= Book("Love in the Air", "Mr Rajan Patel", 5)
book.lend_book()
book.return_book()
print(book.author)
print(book.checkAvailablity())
print(book.title)





