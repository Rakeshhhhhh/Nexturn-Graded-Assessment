from book_management import books
from customer_management import customers


class Transaction:
    def __init__(self, customer_name, book_title, quantity_sold):
        self.customer_name = customer_name
        self.book_title = book_title
        self.quantity_sold = quantity_sold

    def display(self):
        return f"Customer: {self.customer_name}, Book: {self.book_title}, Quantity Sold: {self.quantity_sold}"
    

# Sales records as a list
sales = []

def sell_book(customer_name, book_title, quantity_sold):
    try:
        found = False
        for cust in customers:
            if customer_name.lower() == cust.name.lower():
                found = True
                break
        if not found:
            return "Error: Customer doesn't exist in Bookmart."

        quantity_sold = int(quantity_sold)
        if quantity_sold <= 0:
            raise ValueError("Quantity must be a positive number.")

        # Find the book
        for book in books:
            if book.title.lower() == book_title.lower():
                if book.quantity >= quantity_sold:
                    book.quantity -= quantity_sold
                    sales.append(Transaction(customer_name, book_title, quantity_sold))
                    return f"Sale successful! Remaining quantity: {book.quantity}"
                else:
                    return f"Error: Only {book.quantity} copies available. Sale cannot be completed."

        return "Error: Book not found."

    except ValueError as e:
        return f"Error: {e}"

def view_sales():
    if not sales:
        return "No sales records available."
    return "\n".join([sale.display() for sale in sales])
