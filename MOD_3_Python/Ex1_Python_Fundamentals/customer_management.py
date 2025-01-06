class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


# Customer records as a list
customers = []

def add_customer(name, email, phone):
    if not name or not email or not phone:
        return "Error: All fields are required."
    customers.append(Customer(name, email, phone))
    return "Customer added successfully!"

def view_customers():
    if not customers:
        return "No customers available."
    return "\n".join([customer.display() for customer in customers])
