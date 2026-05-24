#fizzbuzz program
# If a number is divisible by 3, print fizz
# if a number is divisible by 5, print buzz
# if a number is divisible by both, print fizzbuzz

choice = int(input("Choose a number:"))
def function(choice):
    for num in range(1,choice):
        if num % 3 == 0 and num % 5 == 0:
            print(f"fizzbuzz is {num}")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz")
    else:
        print(f"done @{num}")

print("The program is running...")
function(choice)