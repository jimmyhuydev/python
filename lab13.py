#Food receipt
item_name = input("Enter food item name:\n")

# FIXME (1): Finish reading item price and quantity, then output a receipt
item_price = float(input("Enter item price:\n"))
item_quantity = int(input("Enter item quantity:\n"))

# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
print("\nRECEIPT")
total = item_quantity * item_price
print(f"{item_quantity} {item_name} @ ${item_price:.2f} = ${total:.2f}")
print(f"Total cost: ${total:.2f}\n\n")

# FIXME (3): Add a gratuity and total with tip to the second receipt
item_name2 = input("Enter second food item name:\n")
item_price2 = float(input("Enter item price:\n"))
item_quantity2 = int(input("Enter item quantity:\n"))

print("\nRECEIPT")
price1 = item_quantity * item_price
price2 = item_quantity2 * item_price2
total = price1 + price2
print(f"{item_quantity} {item_name} @ ${item_price:.2f} = ${price1:.2f}")
print(f"{item_quantity2} {item_name2} @ ${item_price2:.2f} = ${price2:.2f}")
print(f"Total cost: ${total:.2f}\n")

gratuity = 15 * total / 100
total_final = total + gratuity
print(f"15% gratuity: ${gratuity:.2f}")
print(f"Total with tip: ${total_final:.2f}")
