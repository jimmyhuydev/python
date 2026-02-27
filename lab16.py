import random
random.seed(5)

keep_bidding = "y"
next_bid = 0

while keep_bidding != "n":
    next_bid = next_bid + random.randint(1,10)
    print(f"I'll bid ${next_bid}!")
    print("Continue bidding (y/n)", end = " ")
    keep_bidding  = input()


