import random

# create a greeting
print("Welcome to hangman!")

# creat your word list
words = ["hacker", "checking", "random"]

# randomly choose a word from the list you have created
secret_word = random.choice(words)

# Add the print statement tell the user they get 5 guesses
print("You get 5 gueses")

# for each of the letter in the secrect_word, print "_"
display_word = []

# ask the user to guess a letter
for letter in secret_word:
    display_word += "-"

print(display_word)

# loop through each of the letters in the chosen words
# if the letter is in the word, replace "-" with the letter
# it should look like this "-","a","c","_","_"
# using the while loop so the game can continue going
game_over = False
num = 0         # add the variable num to count the number of guess

while not game_over:
    guess = input("Guess the letter: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guess_lelf = 5 - num
        print(f"You have {guess_lelf} left.")
        if num >= 5:
            print("You LOSE")
            game_over = True
    print(display_word)

    if "-" not in display_word:
        print("You WIN")
        game_over = True
