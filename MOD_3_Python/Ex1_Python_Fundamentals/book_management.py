class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, Quantity: {self.quantity}"


# Book inventory as a list
books = []

def add_book(title, author, price, quantity):
    try:
        price = float(price)
        quantity = int(quantity)
        if price <= 0 or quantity <= 0:
            raise ValueError("Price and quantity must be positive numbers.")
        books.append(Book(title, author, price, quantity))
        return "Book added successfully!"
    except ValueError as e:
        return f"Error: {e}"

def view_books():
    if not books:
        return "No books available."
    return "\n".join([book.display() for book in books])

def search_book(query):
    results = [book.display() for book in books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
    return "\n".join(results) if results else "There is no book named " + query
