patient1 = input()
body_temperature1 = float(input())
patient2 = input()
body_temperature2 = float(input())

temperature_records = {}

""" Your code goes here """
temperature_records = {patient1:body_temperature1, patient2:body_temperature2}
temperature_records[patient1] = body_temperature1 
temperature_records[patient2] = body_temperature2

print(f"{patient1}: {temperature_records[patient1]}")
print(f"{patient2}: {temperature_records[patient2]}")