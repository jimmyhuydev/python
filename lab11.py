#variables input and types
user_int = int(input("Enter integer (32 - 126):\n"))
user_float = float(input("Enter float:\n"))
user_character = input("Enter character:\n")[0]
user_string = str(input("Enter string:\n"))
# TODO (1): Finish reading other items into variables, then output the four values on a single line separated by a space
print(user_int,user_float,user_character,user_string)
# TODO (2): Output the four values in reverse
print(user_string,user_character,user_float,user_int)
# TODO (3): Convert the integer to a character, and output that character
x = chr(user_int)
print(user_int,"converted to a character is",x)
