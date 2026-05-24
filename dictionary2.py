# Dictionary age_dict contains three key-value pairs. 
# Read a string from input, representing a key found in age_dict. 
# Then, assign the value associated with the key read with the current value plus 3.

age_dict = {"Pat": 75, "Ada": 15, "Ava": 44}
print("Original:")
print(age_dict)

""" Your code goes here """
s = input()
age_dict[s] = age_dict[s] + 3
print("Updated:")
print(age_dict)