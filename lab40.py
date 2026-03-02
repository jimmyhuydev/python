"""Program that calculates savings and interest"""

initial_savings = 10000
interest_rate = 0.05

years = int(input("Enter years: "))
print()

savings = initial_savings

# FIXME: Change the following line to use a different version of range()
for i in range(years): 
    print(f" Savings in year {i}: ${savings:.2f}")
    savings = savings + (savings * interest_rate)
