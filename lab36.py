cities = {
    'London': 438,
    'Montreal': 584,
    'Nairobi': 5259,
    'Toronto': 3435,
    'Paris': 982,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)
