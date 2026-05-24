# Dictionary name_score_pairs contains two key-value pairs, 
# each representing a student's name and score on a test. 
# Delete the pair associated with key_name from name_score_pairs.

name_score_pairs = {"Meg": 15, "Kai": 67}

key_name = input()

""" Your code goes here """
del name_score_pairs[key_name]
print("Remaining pairs:")
print(name_score_pairs)