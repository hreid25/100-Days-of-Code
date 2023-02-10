import csv
import pandas as pd
import numpy as np
from math import isnan

# with open('weather_data.csv') as fh:
#     data = csv.reader(fh)
#     lst_obj = [row.strip().split(',') for row in fh]
#     temperatures = []
#     for row in lst_obj[1:]:
#         temperatures.append(int(row[1]))

# data = pd.read_csv('weather_data.csv')
# temperatures = data["temp"].to_list()

# # print(data[data["day"] == "Monday"])
# # print(data[data["temp"] == data["temp"].max()])

# def convert_to_f(celsius):
#     fahrenheit = (celsius * (9/5) + 32)
#     return fahrenheit

# monday = data[data.day == "Monday"]
# celsius = int(monday.temp)
# fahrenheit = convert_to_f(celsius)
# print(fahrenheit)

# # Create dataframe from scratch
# data_dict = {
#     "students" : ['Amy','John','Stuart'],
#     "scores" : [22,88,95]
# }

# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
# print(sum(temperatures))

# sum_temp = sum(temperatures)
# avg = sum_temp / len(temperatures)

# print(avg)
# for temp in temperatures:

# Figure out how many gray, cinnamon and black squirrels in total exist based on Primary Fur column
# from the dataset. Create a CSV output.

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv')
# print(data)

def grab_color_count(color):
    color_count = len(data[data['Primary Fur Color'] == color])
    return color_count

gray_sql = grab_color_count("Gray")
black_sql =grab_color_count("Black")
cinn_sql = grab_color_count("Cinnamon")

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Counts": [gray_sql, black_sql, cinn_sql]
}

print(data_dict)

df_clr_counts = pd.DataFrame(data_dict)
df_clr_counts.to_csv('squirrel_color_counts.csv')



# counts.to_csv("new_data.csv")