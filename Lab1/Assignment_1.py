menu = {
    "coffee": 50,
    "tea": 30,
    "sandwich": 40,
    "cappuccino": 80,
    "latte": 90,
    "burger": 120,
    "pizza": 150,
    "french fries": 70,
    "muffin": 60,
    "cold coffee": 100
}

customerName = input("Enter your name: ")

itemsCount = {}

print("Menu:", menu)

ask = input("Do you want to enter item? yes/no: ").lower()

while ask == "yes" or ask == "y":

    item = input("Enter item name: ").lower()

    if item not in menu:
        print("Item not available in the menu.")
        continue

    quantity = float(input("Enter the item quantity: "))

    if not quantity.is_integer():
        print("Wrong Input: Quantity must be a whole number.")
        continue

    quantity = int(quantity)

    itemsCount[item] = quantity

    ask = input("Do you want to enter another item? yes/no: ").lower()

    if ask == "yes" or ask == "y":
        print("Menu:", menu)
    elif ask == "no" or ask == "n":
        break
    else:
        print("Invalid input")
        break

totalCosts = 0

print("\nCustomer:", customerName)

for items in itemsCount:
    quantity = itemsCount[items]
    price = menu[items]
    itemCost = quantity * price

    totalCosts = totalCosts + itemCost

    print(f"Customer {customerName} is buying {quantity} {items}. "
          f"Price: {price:.2f} rupees, Item total: {itemCost:.2f} rupees")

print(f"Total cost: {totalCosts:.2f} rupees")
