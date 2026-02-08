#Cooking measurement converter
# a gallon contain 16 cups
lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))

# FIXME (1): Finish reading other items into variables, then output the three ingredients
water_cups = float(input("Enter amount of water (in cups):\n"))
nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))


# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
serving = int(input("How many servings does this make?\n"))
print()
print(f"Lemonade ingredients - yields {serving:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{nectar_cups:.2f} cup(s) agave nectar")

# FIXME (3): Convert and output the ingredients from (2) to gallons
print()
serving2 = int(input("How many servings would you like to make?\n"))
print()
print(f"Lemonade ingredients - yields {serving2:.2f} servings")
factor = serving2 / serving

print(f"{(lemon_juice_cups * factor):.2f} cup(s) lemon juice")
print(f"{(water_cups * factor):.2f} cup(s) water")
print(f"{(nectar_cups * factor):.2f} cup(s) agave nectar")

print()
print(f"Lemonade ingredients - yields {serving2:.2f} servings")
print(f"{((lemon_juice_cups * factor) / 16):.2f} gallon(s) lemon juice")
print(f"{((water_cups * factor) / 16):.2f} gallon(s) water")
print(f"{((nectar_cups * factor) / 16):.2f} gallon(s) agave nectar")
