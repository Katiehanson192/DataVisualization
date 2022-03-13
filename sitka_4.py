# 1) changing file to include all data for the year of 2018
#2) change title to - Daily low and high temperatures -2018
#3) extract low temps from the file and add to chart
#4) shade in the area between high and low


import csv
from datetime import datetime
#open_file = open('sitka_weather_07-2018_simple.csv', 'r')
open_file = open('death_valley_2018_simple.csv', 'r') # 

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print((header_row))



for index, column_header in enumerate(header_row):
    print(index, column_header) #shows index location and value of that location


#how to make a list of values 
#adding dates

highs = []
dates = []
lows = []

#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')#telling python how the date is formatted for second arguement   
   
                                                   #date format is CASE SENSITIVE

for value in csv_file:

    try:  #if it passes through this, it goes to the else statement block
        current_date = datetime.strptime(value[2], "%Y-%m-%d")
        high = int(value[4])
        low = int(value[5])

    except ValueError: #say don't break if you run into a value error
        print(f"Missing data for  {current_date}") #this will print the line(s) causing the valueError data
                                                

    else:
        highs.append(high) #use .append to add to a list
        lows.append(low) # 3)
        dates.append(current_date)


print(highs)
print(dates)
print(lows)


#create graph
#to create multiple plots: make subplots
import matplotlib.pyplot as plt

fig = plt.figure() #figure = multiple plots 

plt.plot(dates, highs, c = 'red')  #formatting for plots
plt.plot(dates,lows, c="blue") # 3) add lows to chart

plt.fill_between(dates, highs, lows, facecolor = 'purple', alpha = 0.1)  # 4)  ## reduce alpha = make shading more transparent (range goes from 0-1)

plt.title("Daily high Temperatures for the year 2018", fontsize=16) # 2)
plt.xlabel("Month of July")
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)



fig.autofmt_xdate() #slants x-axis to make more readable


plt.show()

