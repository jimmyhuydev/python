stop = -9
total = 0
for number in [5, 3, 2, 2, 6, 5]:
    print(number, end=" ")
    total -= number
    if total <= stop:
        print("*")
        break
else:
    print(f"| {total}")
print("done")

