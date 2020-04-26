""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 2 - Code shrinking I
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020
"""

import random
import operator
import matplotlib.pyplot

# function to get a random integer from 0 - 99 using the randint function
# an alternative way would be int(random.random() * 100)
def getRndNumber():
    return random.randint(0, 99)

# create an empty agents list to store all the initial x & y coordinate.
agents = []

# append y0 & x0 values to the string.
agents.append([getRndNumber(), getRndNumber()])

# append y1 & x1 values to the string
agents.append([getRndNumber(), getRndNumber()])

# The 2D 'agents' list will have this format when printed: [[y0, x0],[y1, x1]]
print(agents)

# This will list the coordinate set with largest 'y' value i.e. the first argument in each pair of coodinates.
print(max(agents))

# To test this we can put defined values in to the agents list for example:
agents = [[0, 5], [1, 6]]
print(max(agents))  # will print [1, 6].

agents = [[0, 5], [0, 8]]
# will print [0, 8] as the 'y's are the same so it will compare 'x's.
print(max(agents))

# We want to compare the furthest east i.e. 'x' values so need to access
# the second value in each pair by passing a parameter in the max function

# Reset agents string and get random values again:
agents = []
agents.append([getRndNumber(), getRndNumber()])
agents.append([getRndNumber(), getRndNumber()])
print(agents)

print(max(agents, key=operator.itemgetter(1))) # itemgetter(1) gets the second item (i.e at index 1) in each coordinate pair

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

# Colour the furthest east coordinate red.
furthestEast = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(furthestEast[1], furthestEast[0], color='red')

matplotlib.pyplot.show()