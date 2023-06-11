class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def view(self):
        print(f"The book is \"{self.title}\" by author {self.author}")
        print(f"You can order this book by {self.price} dollars")
        print('\n')


book1 = Book("Harry Potter", "Joan Ruling", 10)
book2 = Book("Michael Kraiton", "Jurassic Park", 12)
book3 = Book("Strange Case of Dr Jekyll and Mr Hyde", "Robert Louis", 15)

book1.view()

book2.view()

book3.view()
