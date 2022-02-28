#using the datetime module
#adding dates to x axis for the month of July

import csv
from datetime import datetime
open_file = open('sitka_weather_07-2018_simple.csv', 'r')

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header) #shows index location and value of that location


#how to make a list of values 
#adding dates

highs = []
dates = []

#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')#telling python how the date is formatted for second arguement   
   
                                                   #date format is CASE SENSITIVE

for value in csv_file:
    highs.append(int(value[5])) #use .append to add to a list
   
    current_date = datetime.strptime(value[2], "%Y-%m-%d")
    dates.append(current_date)
print(highs)
print(dates)


#create graph
#to create multiple plots: make subplots
import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c = 'red')  #formatting for plots

plt.title("Daily high Temperatures , July 2018", fontsize=16)
plt.xlabel("Month of July")
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)



fig.autofmt_xdate() #slants x-axis to make more readable

plt.show()





