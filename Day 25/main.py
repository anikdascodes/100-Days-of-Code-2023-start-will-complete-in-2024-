#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


# Create a datafreame from scratch

data_dict ={
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

