# Shopping Cart System

cart = []


def add_item():
    print("\nAdd Item To Cart")

    name = input("Enter product name: ")
    price = float(input("Enter the product price: "))

    item = (name, price) # tuple
    cart.append(item)

    print(f"{name} added to cart!\n")

def view_cart():
    print("\nView Your Cart:")

    if len(cart) == 0:
        print("Cart is actually empty!!")
        return
    
    for ind, item in enumerate(cart, start=1):
        name, price = item
        print(f"{ind}. {name} - Rs.{price}/-")

    print()


def remove_item():
    view_cart()

    if len(cart) == 0:
        return
    
    choice = int(input("Enter item number to remove: "))

    if 1<=choice<=len(cart):
        removed = cart.pop(choice-1)
        print(f"{removed[0]} removed from your cart.\n")
    else:
        print("Invalid choice.\n")

def calculate_total():
    total = 0

    for item in cart:
        total += item[1]

    print(f"\nTotal Bill: Rs.{total}/-")

def most_expensive_item():
    if len(cart) == 0:
        print("\nCar is empty.\n")
        return
    
    expensive = cart[0]

    for item in cart:
        if item[1] > expensive[1]:
            expensive = item

    print(f"\nMost Expensive Item: {expensive[0]} - Rs.{expensive[1]}\n")


def menu():
    while True:
        print("===== Shopping Cart =====")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Total Bill")
        print("5. Most Expensive Item")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice=="1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            most_expensive_item()
        elif choice == "6":
            print("Thank You for shopping with us!!")
            break
        else:
            print("Invalid option.\n")

menu()