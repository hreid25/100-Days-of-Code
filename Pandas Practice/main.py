import csv
import pandas as pd
import numpy as np

# with open('weather_data.csv') as fh:
#     data = csv.reader(fh)
#     lst_obj = [row.strip().split(',') for row in fh]
#     temperatures = []
#     for row in lst_obj[1:]:
#         temperatures.append(int(row[1]))

data = pd.read_csv('weather_data.csv')
print(data["temp"])