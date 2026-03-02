num_input = int(input())

input_list = []
for i in range(num_input):
    input_list.append(int(input()))

for i in range(len(input_list)):
    if input_list[i] >= 45:
        print("Sample " + str(i) + " is abnormal")
    else:
        print("Sample " + str(i) + " is normal")

