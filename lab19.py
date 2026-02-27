input_word = input()
sum_counts = 0

while input_word != "Completed":
    clothing_stock = int(input())
    sum_counts += clothing_stock
    print(input_word)
    input_word = input()

print(f"{sum_counts} counts")
