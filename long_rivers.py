rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

# Task 1: print out river names

for river in rivers:
    print(river["name"])

# Task 2: total length of rivers

total = 0

for river in rivers:
    total += river["length"]
print(str(total) + " mi")

# Ext 1: rivers that begin with M

for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])

# Ext 2: river lengths in km (1 mi = 1.6 km)

for river in rivers:
    river_km = river["length"] * 1.6
    print(river["name"] + ": " + str(river_km) + " km")