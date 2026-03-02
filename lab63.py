result = 0
n = 3
while n > -5:
    print(n, end=" ")
    result -= 3
    if result < -11:
        print("$")
        break
    n -= 1
else:
    print(f"\ {result}")
print("done")

