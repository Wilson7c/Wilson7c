'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately

1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
There was a decrease in both bus usage and total ridership but an increase in rail usage. This could be explained by the
introduction of companies such as Uber as people would perfer such methods of transportation over public transit
'''

import csv
import matplotlib.pyplot as plt

plt.figure(1)

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)
print(data)

years = [int(x[0]) for x in data[20:]]
rail_usage = [int(x[3]) for x in data[20:]]
bus_usage = [int(x[1]) for x in data[20:]]
total_ridership = [int(bus_usage[x]) + int(rail_usage[x]) for x in range(len(bus_usage))]
print(rail_usage)
print(total_ridership)
print(bus_usage)
graph = plt.figure(1, tight_layout=True)

plt.plot(years, rail_usage, label = "Rail")
plt.plot(years, bus_usage, label = "Bus")
plt.plot(years, total_ridership, label = "Total")
plt.ylabel('Number of Riders')
plt.xlabel('Year')
plt.title('CTA Ridership 2008-2018: Bus, Rail, Total')
plt.legend()
plt.axis([2008, 2018, 0, 600000000])

plt.show()