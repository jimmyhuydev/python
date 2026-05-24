#fizzbuzz program
# If a number is divisible by 3, print fizz
# if a number is divisible by 5, print buzz
# if a number is divisible by both, print fizzbuzz

for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        print(num)
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
else:
    print(f"done @{num}")
