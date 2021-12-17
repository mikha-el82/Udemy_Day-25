with open("weather.csv") as weather:
    daily_weather = weather.readlines()
print(daily_weather)

import csv
with open("weather.csv") as weather:
    data = csv.reader(weather)
    temperatures = []
    for row in data:
        # print(row)
        if row[1] != "temperature":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas
data = pandas.read_csv("weather.csv")
# Getting hold of a column
print(data.temperature)

temp_as_list = data.temperature.to_list()
print(temp_as_list)
average_temp = data.temperature.mean()
print(average_temp)

# Getting hold of a row
print(data[data.day == "Monday"])
print(data[data.temperature == data.temperature.max()])
print(data[data.temperature < 0])

# Getting the columnt value from a row
monday = data[data.day == "Monday"]
print("Monday temperature:")
print(monday.temperature)
print(data[data.day == "Monday"].temperature)

# Create DataFrame from scratch
data_dict = {
    "students": ["Amy", "Tim", "John"],
    "scores": [78, 90, 45]
}
scores = pandas.DataFrame(data_dict)
print(scores)
print("\n")

# Squirrels census: how many are Gray, Cinnamon, Black -> export to csv
squirrels_data = pandas.read_csv("squirrels.csv")
squirrels_colors = squirrels_data["Primary Fur Color"]
gray = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Black"])

colors_as_dict = {
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [gray, cinnamon, black]
}
squirrels = pandas.DataFrame(colors_as_dict)
print(squirrels)

squirrels.to_csv("squirrels_count.csv")
