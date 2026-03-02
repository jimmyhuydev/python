student_dict = {
    "Pat": "P11",
    "Eli": "T13",
    "Rob": "Q2",
    "Ian": "M20",
    "Kay": "H5"
}

student_name = input()
seat_code = input()
student_dict[student_name] = seat_code

for student in student_dict:
    print(f"{student}'s seat: {student_dict[student]}")
