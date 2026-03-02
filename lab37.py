destination_list = ["Iowa", "Massachusetts", "Alaska", "Virginia"]

new_destination = input()
destination_list[1] = new_destination

print(f"List has {len(destination_list)} elements:")

for destination in destination_list:
    print(f"{destination} picked")
