daily_revenues = [
    2350.25,  # Monday
    1800.50,  # Tuesday
    1795.00,  # Wednesday
    2050.25,  # Thursday
    1985.75,  # Friday
    2005.00,  # Saturday
    1890.50   # Sunday
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print(f"Weekly revenue: ${total:.2f}")
print(f"Daily average revenue: ${average:.2f}")
