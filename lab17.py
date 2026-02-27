num_successes = 0

while num_successes < 2:

    curr_velocity = int(input())
    if curr_velocity > 0:
        num_successes += 1
        print(curr_velocity)

