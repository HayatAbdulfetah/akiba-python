inventory = {}

# Display a formatted message
def show_message(message):
    print("\n" + "=" * 45)
    print(message)
    print("=" * 45)

# Display product details
def show_product(name, details):
    print(f"\nProduct Name : {name}")
    print(f"Price        : ${details['price']:.2f}")
    print(f"Stock        : {details['stock']} units")


# Add a new product
def add_product(name, price, stock):
    name = name.strip()

    if not name:
        show_message("ERROR: Product name cannot be empty.")
        return

    if name in inventory:
        show_message("ERROR: Product already exists.")
        return

    if price < 0:
        show_message("ERROR: Price cannot be negative.")
        return

    if stock < 0:
        show_message("ERROR: Stock cannot be negative.")
        return

    inventory[name] = {
        "price": price,
        "stock": stock
    }

    show_message("PRODUCT ADDED SUCCESSFULLY")
    show_product(name, inventory[name])

# Search for a product
def search_product(name):
    if name in inventory:
        show_message("PRODUCT FOUND")
        show_product(name, inventory[name])
        return inventory[name]

    show_message("ERROR: Product not found.")
    return None

# Update product price
def update_price(name, new_price):
    if name not in inventory:
        show_message("ERROR: Product not found.")
        return

    if new_price < 0:
        show_message("ERROR: Price cannot be negative.")
        return

    inventory[name]["price"] = new_price

    show_message("PRICE UPDATED SUCCESSFULLY")
    show_product(name, inventory[name])

# Increase stock
def increase_stock(name, quantity):
    if name not in inventory:
        show_message("ERROR: Product not found.")
        return

    if quantity <= 0:
        show_message("ERROR: Quantity must be greater than zero.")
        return

    inventory[name]["stock"] += quantity

    show_message("STOCK INCREASED SUCCESSFULLY")
    show_product(name, inventory[name])

# Sell a product
def sell_product(name, quantity):
    if name not in inventory:
        show_message("ERROR: Product not found.")
        return

    if quantity <= 0:
        show_message("ERROR: Quantity must be greater than zero.")
        return

    if quantity > inventory[name]["stock"]:
        show_message("ERROR: Not enough stock available.")
        print(f"Available stock: {inventory[name]['stock']} units")
        return

    inventory[name]["stock"] -= quantity

    show_message("SALE COMPLETED SUCCESSFULLY")
    print(f"Product sold : {name}")
    print(f"Quantity sold: {quantity} units")
    print(f"Remaining    : {inventory[name]['stock']} units")

# Calculate total inventory value
def total_inventory_value():
    total = 0

    for details in inventory.values():
        total += details["price"] * details["stock"]

    show_message("INVENTORY SUMMARY")
    print(f"Total Products        : {len(inventory)}")
    print(f"Total Inventory Value : ${total:.2f}")

# Generate low-stock report
def low_stock_report(threshold=5):
    if threshold < 0:
        show_message("ERROR: Threshold cannot be negative.")
        return

    show_message("LOW STOCK REPORT")
    print(f"Stock threshold: Fewer than {threshold} units\n")

    found = False

    for name, details in inventory.items():
        if details["stock"] < threshold:
            print(f"{name:<20} | {details['stock']} units remaining")
            found = True

    if not found:
        print("All products have sufficient stock.")

    print("-" * 45)


show_message("WELCOME TO INVENTORY STOCK CONTROLLER")

# Add products
add_product("Laptop", 500, 10)
add_product("Mouse", 20, 3)
add_product("Keyboard", 30, 8)

search_product("Laptop")
update_price("Laptop", 550)
increase_stock("Mouse", 5)
sell_product("Keyboard", 2)
total_inventory_value()
low_stock_report()
low_stock_report(10)
