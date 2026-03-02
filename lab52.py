letter1 = "g"
while letter1 < "i":
    letter2 = "s"
    while letter2 <= "u":
        print(f"{letter1}{letter2}")
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

