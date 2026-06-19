import json

# Sample data
books = [
    {"title": "Percy Jackson and the Lightning Thief", "author": "Rick Riordan", "price": 8.99},
    {"title": "The Hunger Games", "author": "Suzanne Collins", "price": 7.99},
    {"title": "Of Mice and Men", "author": "John Steinbeck", "price": 6.49},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 7.49},
    {"title": "Twilight", "author": "Stephenie Meyer", "price": 8.49},
    {"title": "Jack Reacher", "author": "Lee Child", "price": 9.99},
    {"title": "Star Wars", "author": "George Lucas (Various)", "price": 10.99},
    {"title": "Animal Farm", "author": "George Orwell", "price": 5.99}
]

foods = [
    {"item": "Chocolate Croissant", "price": 2.50},
    {"item": "Fruit Salad", "price": 3.00},
    {"item": "Chicken Satay Baguette", "price": 4.75},
    {"item": "Tuna Melt", "price": 4.50},
    {"item": "Classic Sub Sandwich", "price": 4.95},
    {"item": "Pain aux Raisins", "price": 2.75},
    {"item": "Chocolate Cookie", "price": 1.80}
]

drinks = [
    {"item": "Latte", "price": 2.80},
    {"item": "Iced Latte", "price": 3.20},
    {"item": "Flat White", "price": 2.90},
    {"item": "Mocha", "price": 3.10},
    {"item": "Espresso", "price": 2.00},
    {"item": "English Tea", "price": 1.90},
    {"item": "Hot Chocolate", "price": 2.95}
]

customers = []

# Functions to display items
def display_items(items, item_type):
    print(f"\n{item_type} Menu:")
    for i, item in enumerate(items, start=1):
        name = item.get('title') or item['item']
        print(f"{i}. {name} - £{item['price']:.2f}")

# Function to take customer order
def take_order():
    name = input("Enter your name: ")
    address = input("Enter your delivery address: ")
    order = {"name": name, "address": address, "books": [], "foods": [], "drinks": []}

    display_items(books, "Book")
    book_choice = input("Select book numbers separated by commas (or leave blank): ")
    if book_choice:
        order['books'] = [books[int(i)-1] for i in book_choice.split(',')]

    display_items(foods, "Food")
    food_choice = input("Select food numbers separated by commas (or leave blank): ")
    if food_choice:
        order['foods'] = [foods[int(i)-1] for i in food_choice.split(',')]

    display_items(drinks, "Drink")
    drink_choice = input("Select drink numbers separated by commas (or leave blank): ")
    if drink_choice:
        order['drinks'] = [drinks[int(i)-1] for i in drink_choice.split(',')]

    customers.append(order)
    print("\nOrder placed successfully! Your order will be with you soon!")

# Admin options
def admin_panel():
    password = input("Enter admin password: ")
    if password != "admin123":
        print("Access denied.")
        return

    while True:
        print("\nAdmin Panel:")
        print("1. View customer orders")
        print("2. Update books")
        print("3. Update food menu")
        print("4. Update drink menu")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            for customer in customers:
                print(json.dumps(customer, indent=2))
        elif choice == "2":
            display_items(books, "Book")
            title = input("Enter new book title: ")
            author = input("Enter author: ")
            price = float(input("Enter price: "))
            books.append({"title": title, "author": author, "price": price})
            print("Book added.")
        elif choice == "3":
            display_items(foods, "Food")
            item = input("Enter new food item: ")
            price = float(input("Enter price: "))
            foods.append({"item": item, "price": price})
            print("Food item added.")
        elif choice == "4":
            display_items(drinks, "Drink")
            item = input("Enter new drink item: ")
            price = float(input("Enter price: "))
            drinks.append({"item": item, "price": price})
            print("Drink item added.")
        elif choice == "5":
            break
        else:
            print("Invalid option.")

# Main program loop
def main():
    while True:
        print("\nWelcome to the Bookshop Cafe App!")
        print("1. Place an order")
        print("2. Employee/Admin login")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            take_order()
        elif option == "2":
            admin_panel()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
