#Using math function
import math
# Type your code here
x = float(input())
y = float(input())
z = float(input())
your_value1 = math.pow(math.fabs(x),z)
your_value2 = math.pow(x,math.pow(y,z))
your_value3 = math.fabs(x - y)
your_value4 = math.sqrt(math.pow(x,z))
print(f"{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}")
