#Musical note frequencies
# Type your code here. 
import math

f0 = float(input())
r = math.pow(2,1 / 12)
n = 0
your_value = f0 * math.pow(r,n)
print(f"{your_value:.2f} Hz")

n = 1
your_value = f0 * math.pow(r,n)
print(f"{your_value:.2f} Hz")

n = 2
your_value = f0 * math.pow(r,n)
print(f"{your_value:.2f} Hz")

n = 3
your_value = f0 * math.pow(r,n)
print(f"{your_value:.2f} Hz")
