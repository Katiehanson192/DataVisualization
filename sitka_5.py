#HW file: 
    #automatic indexes
    #use header row to determine indexes for min and max values of Sitka and Death Valley
    #station name to automatically generate graph title
    #2 subplots in 1 visual side by side



import csv
from datetime import datetime
open_file = open('death_valley_2018_simple.csv', 'r')
open_file1 = open('sitka_weather_2018_simple.csv', 'r')

death_vally = csv.reader(open_file, delimiter = ",")
sitka = csv.reader(open_file1, delimiter = ",")

header_row_dv = next(death_vally)
header_row_sk= next(sitka)

print(header_row_dv)
print(header_row_sk)

tmin_sk = header_row_sk.index("TMIN")
tmax_sk = header_row_sk.index("TMAX")
tmin_dv = header_row_dv.index("TMIN")
tmax_dv = header_row_dv.index("TMAX")
title_sk = header_row_sk.index("NAME")
title_dv = header_row_dv.index("NAME")

print()

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
        high1 = int(value[tmax_sk])
        low1 = int(value[tmin_sk])
        heading = value[title_sk]

    except ValueError: #say don't break if you run into a value error
        print(f"Missing data for  {current_date}") #this will print the line(s) causing the valueError data
                                                

    else:
        highs_sk.append(high1) #use .append to add to a list
        lows_sk.append(low1) # 3)
        dates_sk.append(current_date)
    #print(heading)

#values for death vally
for value in death_vally:

    try:  #if it passes through this, it goes to the else statement block
        current_date = datetime.strptime(value[2], "%Y-%m-%d")
        high = int(value[tmax_dv])
        low = int(value[tmin_dv])
        heading1 = value[title_dv]


    except ValueError: #say don't break if you run into a value error
        print(f"Missing data for  {current_date}") #this will print the line(s) causing the valueError data
                                                

    else:
        highs_dv.append(high) #use .append to add to a list
        lows_dv.append(low) # 3)
        dates_dv.append(current_date)
    print(heading1)

##Need to fix and look at graphs!
#Need to make title be automatically filled
title_sk = header_row_sk.index("NAME")
title_dv = header_row_sk.index("NAME")

indices = {}
for index, column_header in enumerate(header_row_sk):
    indices[column_header] = index
    print(indices) #shows index location and value of that location

#create graph
#to create multiple plots: make subplots
import matplotlib.pyplot as plt

fig = plt.figure() #figure = multiple plots 


#creating sub plots
plt.subplot(2,1,1)
plt.plot(dates_sk,highs_sk, c ="red")
plt.plot(dates_sk,lows_sk, c ="blue")
plt.title(heading)
plt.fill_between(dates_sk, highs_sk, lows_sk, facecolor = 'purple', alpha = 0.1)


plt.subplot(2,1,2)
plt.plot(dates_dv,highs_dv, c ="red")
plt.plot(dates_dv,lows_dv, c ="blue")
plt.title(heading1)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor = 'purple', alpha = 0.1)

plt.suptitle("Highs and Lows of Sitka, AK and Death Vally, CA") #main title

plt.show()
