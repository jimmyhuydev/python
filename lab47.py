c1 = "a"
while c1 < "b":
    c2 = "a"
    while c2 <= "c":
        print(f"{c1}{c2}", end=" ")
        c2 = chr(ord(c2) + 1)
    c1 = chr(ord(c1) + 1)
