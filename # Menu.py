# Define the menu
menu = {
    "Snacks": {
        "Doritos": 1.99,
        "Cookie": 1.25,
        "Fritos": 1.25,
        "Lays": 1.25,
        "Ruffle": 1.25,
        "Cheetos": 1.50
    },
    "Meals": {
        "Sushi": 9.99,
        "Burrito": 12.99,
        "Burger": 10.99,
        "Steak and Cheese": 15.99,
        "Orange Chicken": {
            "With Rice": 12.99,
            "With Fried Rice": 15.99
        },
        "Vietnamese Food": {
            "Pho": 12.99,
            "Bun Bo Hue": 14.99,
            "Com Tam": 14.99,
            "Egg Rolls": 5.99
        }
    },
    "Drinks": {
        "Cola": {
            "Small": 1.99,
            "Medium": 2.99,
            "Large": 3.99
        },
        "Sweet Tea": {
            "Small": 1.99,
            "Medium": 2.99,
            "Large": 3.99
        },
        "Coffee": {
            "Small": 2.99,
            "Medium": 3.99,
            "Large": 4.99
        },
        "Tea": {
            "Green Tea": {
                "Small": 2.99,
                "Medium": 3.99,
                "Large": 4.99
            },
            "Black Tea": {
                "Small": 2.99,
                "Medium": 3.99,
                "Large": 4.99
            },
            "Milk Tea": {
                "Small": 2.99,
                "Medium": 3.99,
                "Large": 4.99
            }
        },
        "Orange Juice": 3.99
    },
    "Dessert": {
        "Chocolate Cake": 3.99,
        "Cheese Cake": 4.99,
        "Macaron": 2.99,
        "Cup Cake": 3.99
    }
}

# Function to display menu items
def display_menu(menu_category):
    print("item # | Item Name                   | Price ")
    print("-------|-----------------------------|-------")
    items = menu[menu_category]
    for i, (item, price) in enumerate(items.items(), start=1):
        if isinstance(price, dict):
            print(f"{i}: {item}")
            for sub_item, sub_price in price.items():
                if isinstance(sub_price, dict):  # Handle nested dictionaries
                    print(f"    {sub_item}:")
                    for sub_sub_item, sub_sub_price in sub_price.items():
                        print(f"      {sub_sub_item.ljust(25)} | ${sub_sub_price:.2f}")
                else:
                    print(f"    {sub_item.ljust(25)} | ${sub_price:.2f}")
        else:
            print(f"{i}: {item.ljust(28)} | ${price:.2f}")


# Main ordering loop
print("Welcome to my Vu Pham Shop.")
place_order = True
order = []

while place_order: 
    print("From which menu category would you like to order?")
    for i, category in enumerate(menu.keys()):
        print(f"{i+1}: {category}")
    menu_category_num = input("Type menu number: ")

    # Input validation
    if menu_category_num.isdigit():
        menu_category_num = int(menu_category_num)
        if 1 <= menu_category_num <= len(menu):
            menu_category_name = list(menu.keys())[menu_category_num - 1]
            print(f"You selected {menu_category_name}.")
            display_menu(menu_category_name)
            
            # Selecting an item
            item_num = input("Type item number or 'done' to go back to menu: ")
            if item_num.isdigit():
                item_num = int(item_num)
                items = menu[menu_category_name]
                if 1 <= item_num <= len(items):
                    item_name, item_price = list(items.items())[item_num - 1]
                    if isinstance(item_price, dict):
                        print(f"You selected {item_name}. Please choose an option:")
                        for i, (option, price) in enumerate(item_price.items(), start=1):
                            print(f"{i}: {option} - ${price:.2f}")
                        option_num = input("Type option number: ")
                        if option_num.isdigit():
                            option_num = int(option_num)
                            if 1 <= option_num <= len(item_price):
                                option_name, option_price = list(item_price.items())[option_num - 1]
                                print(f"You selected {option_name} for ${option_price:.2f}.")

                                # Ask the customer for the quantity of the menu item
                                quantity = input(f"How many {option_name} would you like to order? (Default is 1): ")
                                
                                # Check if the quantity is a number, default to 1 if not
                                if quantity.isdigit():
                                    quantity = int(quantity)
                                else:
                                    quantity = 1

                                order.append((item_name + " " + option_name, option_price, quantity))
                            else:
                                print("Invalid option number. Please select a valid option.")
                        else:
                            print("Invalid input. Please enter a valid option number.")
                    else:
                        print(f"You selected {item_name} for ${item_price:.2f}.")

                        # Ask the customer for the quantity of the menu item
                        quantity = input(f"How many {item_name} would you like to order? (Default is 1): ")
                        
                        # Check if the quantity is a number, default to 1 if not
                        if quantity.isdigit():
                            quantity = int(quantity)
                        else:
                            quantity = 1

                        order.append((item_name, item_price, quantity))
                else:
                    print("Invalid item number. Please select a valid item.")
            elif item_num.lower() == 'done':
                continue
            else:
                print("Invalid input. Please enter a valid item number or 'done'.")
        else:
            print("Invalid menu number. Please select a valid menu category.")
    else:
        print("Invalid input. Please enter a valid menu number.")

    # Check if the user wants to place another order
    another_order = input("Would you like to add more items to your order? (y/n): ")
    if another_order.lower() != 'y':
        place_order = False

# Display order summary
if order:
    print("\nOrder Summary:")
    total = sum(item[1] * item[2] for item in order)
    for item_name, item_price, quantity in order:
        print(f"{item_name.ljust(20)} - ${item_price:.2f} - Quantity: {quantity}")
    print(f"Total: ${total:.2f}")
    print("Please proceed to payment.")
else:
    print("No items were ordered. Have a great day!")

print("Thank you for visiting! Have a great day!")
