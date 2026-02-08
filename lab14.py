#Convert to dollars
nickels = float(input())
dimes = float(input())
quarters = float(input())

dollars = (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
print(f"Amount: ${dollars:.2f}")
