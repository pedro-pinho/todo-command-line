import csv

with open("../files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")
found = False
for row in data[1:]:
    if row[0].lower() == city.lower():
        print(row[1])
        found = True

if not found:
    print("Sorry, we don't have that information")
