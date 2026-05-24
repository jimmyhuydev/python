# Dictionary food_quantity_pairs contains three key-value pairs, 
# each representing a food name and the quantity purchased. 
# Output the quantity corresponding to key_name.

food_quantity_pairs = {"wraps": 44, "coffees": 75, "carrots": 50}

key_name = input()

print(key_name, "is:")
print(food_quantity_pairs[key_name])