customer_list = ["Kit", "Ian", "Ned", "Ira", "Eve"]

new_customer = input()
customer_list[0] = new_customer

print(f"List has {len(customer_list)} elements:")

for value in reversed(customer_list):
     print(f"({value})", end="")

print()
