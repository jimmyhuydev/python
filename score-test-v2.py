# Score Test 
"""
Score 90 and above: Grade A
Score 80 to 89: Grade B
Score 70 to 79: Grade C
Score 60 to 69: Grade D
Score below 60: Grade F

Update program to use nest statement
"""

score = int(input("Enter your test score:"))

if score >= 90:
    age = int(input("What is your age?"))
    if age < 10:
        print("Grade A+")
    else:
        print("Grade A")
elif score >= 80:
    age = int(input("What is your age?"))
    if age < 10:
        print("Grade B+")
    else:
        print("Grade B")    
elif score >= 70:
    age = int(input("What is your age?"))
    if age < 10:
        print("Grade C+")
    else:
        print("Grade C")
elif score >= 60:
    age = int(input("What is your age?"))
    if age < 10:
        print("Grade D+")
    else:
        print("Grade D")
else:
    print("Grade F. Next time study harder")
    