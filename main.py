# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# suma = 0
# temp_list = data["temp"].tolist()
# for temp in temp_list:
#     suma += temp
# av_temp = round(suma / len(temp_list), 2)
# suma2 = sum(temp_list)
# print(av_temp)
#
# data["temp"].mean()
# print(data["temp"].mean())
#
# # Get data in columns
# data["temp"].max()
# print(data["temp"].max())
#
# # Get data in row
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"])
# monday = data[data.day == "Monday"]
# print((monday.temp*9/5)+32)
#
# # Converting dictionary to new excel file
# # data = pandas.DataFrame(data_dictionary)
# # data.to_csv("new_file.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_color = data["Primary Fur Color"]
# print(data_color)
data_gray = data_color[data_color == "Gray"]
# print(data_gray)
data_gray.to_csv("gray")
gray_squirrels = data_gray.count()
print(gray_squirrels)  # or len()
data_black = data_color[data_color == "Black"]
black_squirrels = data_black.count()
print(black_squirrels)
data_cinnamon = data_color[data_color == "Cinnamon"]
cinnamon_squirrels = data_cinnamon.count()
print(cinnamon_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
