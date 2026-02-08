#Divide input integers
user_num = int(input())
div_num = int(input())
output1 = user_num // div_num
output2 = output1 // div_num
output3 = output2 // div_num

print(output1,output2,output3)
#driving cost
gas_mileage = float(input())
cost_of_gas = float(input())
your_value1 = float(20 / gas_mileage *  cost_of_gas)
your_value2 = float(75 / gas_mileage * cost_of_gas)
your_value3 = float(500 / gas_mileage * cost_of_gas)

print(f"{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}")
