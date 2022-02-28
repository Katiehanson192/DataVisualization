import csv
open_file = open('sitka_weather_07-2018_simple.csv', 'r')

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header) #shows index location and value of that location


#how to make a list of values 

highs = []

for value in csv_file:
    highs.append(int(value[5])) #use .append to add to a list
print(highs)

#create graph
#to create multiple plots: make subplots
import matplotlib.pyplot as plt

plt.plot(highs, c = 'red')  #formatting for plots

plt.title("Daily high Temperatures , July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
