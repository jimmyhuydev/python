start_sequence = int(input())
end_sequence = int(input())

print("Numbers in sequence:", end=" ")

for curr_value in range(start_sequence, end_sequence + 1, 2):
    print(curr_value, end=" ")
print()
