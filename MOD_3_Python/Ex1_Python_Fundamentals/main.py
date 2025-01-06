from book_management import add_book, view_books, search_book
from customer_management import add_customer, view_customers
from sales_management import sell_book, view_sales

def main():
    while True:
        print("\nWelcome to BookMart!")
        print("1. Book Management")
        print("2. Customer Management")
        print("3. Sales Management")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBook Management")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                price = input("Enter book price: ")
                quantity = input("Enter book quantity: ")
                print(add_book(title, author, price, quantity))

            elif sub_choice == "2":
                print("\nAvailable Books:")
                print(view_books())

            elif sub_choice == "3":
                query = input("Enter book title or author to search: ")
                print("\nSearch Results:")
                print(search_book(query))

            else:
                print("Invalid choice.")

        elif choice == "2":
            print("\nCustomer Management")
            print("1. Add Customer")
            print("2. View Customers")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                phone = input("Enter customer phone: ")
                print(add_customer(name, email, phone))

            elif sub_choice == "2":
                print("\nCustomer List:")
                print(view_customers())

            else:
                print("Invalid choice.")

        elif choice == "3":
            print("\nSales Management")
            print("1. Sell Book")
            print("2. View Sales Records")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                customer_name = input("Enter customer name: ")
                book_title = input("Enter book title: ")
                quantity = input("Enter quantity: ")
                print(sell_book(customer_name, book_title, quantity))

            elif sub_choice == "2":
                print("\nSales Records:")
                print(view_sales())

            else:
                print("Invalid choice.")

        elif choice == "4":
            print("Exiting BookMart. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
