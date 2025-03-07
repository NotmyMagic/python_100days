# with open("./part3/test/weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)

# import csv

# with open("./part3/test/weather_data.csv") as data_file:
#     weather = csv.reader(data_file)
#     temperatures = []
#     for row in weather:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("./part3/test/weather_data.csv")
# # print(type(data))
# # print(data["temp"])

# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data["temp"].to_list()
# # print(len(temp_list))

# # # print(data["temp"].mean())
# # # print(data["temp"].max())
# # print(data.condition)

# # print(data[data.temp == data.temp.max()])

# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9/5 + 32

# # print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Jesse"],
#     "scores": [76, 69, 92]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("./part3/test/new_data.csv")

data = pandas.read_csv("./part3/test/2018_CPS_Census.csv")
gray_squirrles = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrles = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrles = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrles)
print(red_squirrles)
print(black_squirrles)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrles, red_squirrles, black_squirrles]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./part3/test/squirrel_count.csv")