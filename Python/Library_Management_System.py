'''
Write a library class with no_of_books_ and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesn't persist the books after the program is stopped!
'''
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    
    def addBooks(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books")

l1 = Library()
l1.addBooks("Harry Potter")
l1.addBooks("Harry Potter1")
l1.showInfo()