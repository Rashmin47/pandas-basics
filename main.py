# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
import csv

with open("weather_data.csv", newline="") as data_file:
	data = list(csv.reader(data_file))

for row in data:
	print(row)