# Tuple is immutuable, can not be changed.

white_house_coordinates = (38.8977, 77.0366)
print(f"Coordinates: {white_house_coordinates}")
print(f"Tuple length: {len(white_house_coordinates)}")

# Access tuples via index
print(f"\nLatitude: {white_house_coordinates[0]} north")
print(f"Longitude: {white_house_coordinates[1]} west\n")

# Error. Tuples are immutable
white_house_coordinates[1] = 50


