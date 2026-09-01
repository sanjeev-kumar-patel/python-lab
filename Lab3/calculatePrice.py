def calculate_price(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price


price = float(input("Enter the original price: "))

choice = input("Do you want to enter a discount percentage? (yes/no): ")

if choice.lower() == "yes":
    discount = float(input("Enter the discount percentage: "))
    print("Final price:", calculate_price(price, discount))
else:
    print("Final price:", calculate_price(price))