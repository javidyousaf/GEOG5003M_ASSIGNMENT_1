""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 6 - I/O
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020
"""

import csv
import matplotlib.pyplot

environment = []

# Use the csv import to parse the text file as it is comma seperated
with open("assets/in.txt") as f:
    # values converted to floats
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

        '''
        This also works with the following code as each row is a rowlist anyway so this is neater.
            for row in reader:
                environment.append(row)
        '''

# Plot the environment data
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
