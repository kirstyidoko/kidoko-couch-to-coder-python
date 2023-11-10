import csv
from collections import namedtuple

cars = []

Car = namedtuple("Car", "Model Year Price_GBP Transmission Mileage Fuel_Type Tax_GBP mpg Engine_Size")

with open("vw.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)    # skips the header row
    for row in reader:
        new_car = Car(*row)
        cars.append(new_car)

# print(cars)

# Task 1.  What is the most expensive VW car listed?

most_expensive_car = cars[0]

for car in cars:
    if int(car.Price_GBP) > int(most_expensive_car.Price_GBP):
        most_expensive_car = car

print(most_expensive_car)

# Task 2.  Find all the VW Golf models. What is their average price?

# Step 1: make new Golf list
vw_golfs = []

for car in cars:
    if "Golf" in car.Model:
        vw_golfs.append(car)

# print(vw_golfs)

# Step 2: find total price of Golf cars
golf_total = 0

for vw_golf in vw_golfs:
    golf_total += int(vw_golf.Price_GBP)

# print(golf_total)

# Step 3: find average price
golf_avg = golf_total / len(vw_golfs)
rounded_golf_avg = round(golf_avg, 2)
print("The average price of a VW Golf is £" + str(rounded_golf_avg))

# Task 3.  What is the average mileage for VW Polo models registered in 2020?

# Step 1: make Polo 2020 list
vw_polos_2020 = []

for car in cars:
    if "Polo" in car.Model and "2020" in car.Year:
        vw_polos_2020.append(car)

# print(vw_polos_2020)

# Step 2: find total mileage of Polo 2020 cars
polo_2020_total = 0

for vw_polo_2020 in vw_polos_2020:
    polo_2020_total += int(vw_polo_2020.Mileage)

# print(polo_2020_total)

# Step 3: find average mileage
polo_2020_avg = polo_2020_total / len(vw_polos_2020)
rounded_polo_2020_avg = round(polo_2020_avg, 0)
print("The average mileage of a 2020 VW Polo is " + str(rounded_polo_2020_avg) + " mi")

# Ext 1. A pie chart showing the distribution between fuel types. (You can use the model column
    # to count occurences!)

import pandas as pd
import matplotlib.pyplot as plt

vw_cars = pd.read_csv("vw.csv")
print(vw_cars) # 15,156 entries

vw_cars = vw_cars.dropna() # removing entries w/ incomplete data
print(vw_cars) # 15,156 entries, no null values

vw_cars = vw_cars.drop_duplicates()
print(vw_cars) # 14,893 entries, duplicates removed

vw_fuel = vw_cars.groupby("fuelType")[["model"]].count().sort_values("model", 
    ascending=False).reset_index()

plt.pie(vw_fuel.model,
        labels=vw_fuel.fuelType,
        autopct="%1.1f%%")
plt.title("VW Cars by Fuel Type")
plt.axis('equal')
plt.show()

# Ext 2. A bar chart showing the average mileage for each model. (You need to research how
    # you can calculate average using pandas!)

avg_mileage_model = vw_cars.groupby("model")["mileage"].mean().reset_index()
# print(avg_mileage_model)

plt.bar(avg_mileage_model.model,
        avg_mileage_model.mileage, 
        color="blue",
        width=0.4,
        )
plt.ylabel("Average mileage (mi)")
plt.title("Average mileage per VW model")
plt.xticks(rotation=90)
plt.show()