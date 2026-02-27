curr_age = int(input())

while (curr_age < 15 or curr_age > 70):
    if curr_age < 15:
        print("20% discount")
    else:
         print("10% discount")
    curr_age = int(input())

print("No discount")

