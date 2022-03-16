#HW file: 
    #automatic indexes
    #use header row to determine indexes for min and max values of Sitka and Death Valley
    #station name to automatically generate graph title
    #2 subplots in 1 visual side by side



import csv
from datetime import datetime
open_file = open('death_valley_2018_simple.csv', 'r')
open_file1 = open('sitka_weather_07-2018_simple.csv', 'r')

death_vally = csv.reader(open_file, delimiter = ",")
sitka = csv.reader(open_file1, delimiter = ",")

header_row_dv = next(death_vally)
header_row_sk= next(sitka)

print(header_row_dv)

tmin_sk = header_row_sk.index("TMIN ")
tmax_sk = header_row_sk.index("TMAX")
tmin_dv = header_row_dv.index("TMIN")
tmax_dv = header_row_dv.index("TMAX")

'''
for index, column_header in enumerate(header_row_dv):
    print(index, column_header) #shows index location and value of that location

for index, column_header in enumerate(header_row_sk):
    print(index, column_header) #shows index location and value of that location
'''

#how to make a list of values 
#adding dates
dates_sk =[]
dates_dv = []
highs_sk = []
lows_sk = []
highs_dv = []
lows_dv = []


#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')#telling python how the date is formatted for second arguement   
   
                                                   #date format is CASE SENSITIVE
#values for sitka
for value in sitka:

    try:  #if it passes through this, it goes to the else statement block
        current_date = datetime.strptime(value[2], "%Y-%m-%d")
        high = int(value[tmax_sk])
        low = int(value[tmin_sk])

    except ValueError: #say don't break if you run into a value error
        print(f"Missing data for  {current_date}") #this will print the line(s) causing the valueError data
                                                

    else:
        highs_sk.append(high) #use .append to add to a list
        lows_sk.append(low) # 3)
        dates_sk.append(current_date)
#values for death vally
for value in death_vally:

    try:  #if it passes through this, it goes to the else statement block
        current_date = datetime.strptime(value[2], "%Y-%m-%d")
        high = int(value[tmax_dv])
        low = int(value[tmin_dv])

    except ValueError: #say don't break if you run into a value error
        print(f"Missing data for  {current_date}") #this will print the line(s) causing the valueError data
                                                

    else:
        highs_dv.append(high) #use .append to add to a list
        lows_dv.append(low) # 3)
        dates_dv.append(current_date)



#create graph
#to create multiple plots: make subplots
import matplotlib.pyplot as plt

fig = plt.figure() #figure = multiple plots 

plt.plot(dates_sk, highs_sk, c = 'red')  #formatting for plots
plt.plot(dates_sk,lows_sk, c="blue") # 3) add lows to chart

plt.fill_between(dates_sk, highs_sk, lows_sk, facecolor = 'purple', alpha = 0.1)  # 4)  ## reduce alpha = make shading more transparent (range goes from 0-1)

plt.title("Daily high Temperatures for the year 2018", fontsize=16) # 2)
plt.xlabel("Month of July")
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize=16)



fig.autofmt_xdate() #slants x-axis to make more readable

plt.show()  #1st graph


#creating sub plots
plt.subplot(4,1,1)
plt.plot(dates_sk,highs_sk, c ="red")
plt.plot(dates_dv,lows_sk, c ="blue")
plt.title("Highs")
plt.fill_between(dates_sk, highs_sk, lows_sk, facecolor = 'purple', alpha = 0.1)


plt.subplot(4,1,2)
plt.plot(dates_dv,highs_dv, c ="red")
plt.plot(dates_dv,lows_dv, c ="blue")
plt.title("Lows")
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor = 'purple', alpha = 0.1)

plt.suptitle("Highs and Lows of Sitka, Alasks 2018") #main title

plt.show()
