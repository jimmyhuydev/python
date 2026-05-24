# Dictionary word_translator contains ten key-value pairs. 
# Read strings word1 and word2 from input. 
# Strings word1 represents a two-digit number and word2 
# represents a one-digit number. Use word_translator to access 
# the numerical equivalent value of the two words. 
# Then, output the two-digit number represented by the two words together.

word_translator = {
	"twenty": 20, "one": 1, "two": 2, "three": 3,
	"four": 4, "five": 5, "six": 6, "seven": 7,
	"eight": 8, "nine": 9
}

""" Your code goes here """
word1 = input()
word2 = input()
total = word_translator[word1] + word_translator[word2]
print(total)