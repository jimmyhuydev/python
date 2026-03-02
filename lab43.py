first_val = int(input())
last_val = int(input())
total_vals = 0
data_count = 0

for curr_value in range(first_val, last_val + 1):
    print(f"Including: {curr_value}")
    total_vals += curr_value
    data_count += 1

print(f"Sum of sequence: {total_vals}")
print(f"Values counted: {data_count}")
