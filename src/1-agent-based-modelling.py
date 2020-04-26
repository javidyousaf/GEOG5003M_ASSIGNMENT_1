""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 1 - Agent Based Modelling
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020
"""

import random

# function to get a random integer from 0 - 99 using the randint function
# an alternative way would be int(random.random() * 100)
def getRndNumber():
    return random.randint(0, 99)


# set all the initial x & y coordinate to random values
x0 = random.randint(0, 99)
y0 = random.randint(0, 99)
x1 = getRndNumber() # using the getRndNumber() function defined above.
y1 = getRndNumber() # using the getRndNumber() function defined above.

if getRndNumber() < 50:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1

if getRndNumber() < 50:
    y1 += 1
    x1 += 1
else:
    y1 -= 1
    x1 -= 1

# calculate distance using Pythagoras
yDiff = (y0 - y1)
yDiffsq = yDiff ** 2  # alternatively use math.pow(x,2) to sqare number
xDiff = (x0 - x1)
xDiffsq = xDiff ** 2
sum = yDiffsq + xDiffsq
answer = sum**0.5  # alternatively use math.sqrt(x) to get the square root
print(answer)

