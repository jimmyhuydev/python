threshold = int(input())

for a in range(0, 4):
    print(a + 1, end=": ")

    for b in range(0, 2):
        if a > threshold:
            print("_,", end="")
            continue

        print(b, end=",")

    print()

