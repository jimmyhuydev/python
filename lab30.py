# Each list item is the number of kids in a family.
num_kids = [1, 1, 2, 2, 1, 4, 3, 1]

total = 0
for num in num_kids:
    total += num

average = total / len(num_kids)
