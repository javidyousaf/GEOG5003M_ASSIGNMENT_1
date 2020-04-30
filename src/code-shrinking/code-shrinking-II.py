""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 3 - Code shrinking II
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020

Description: 
"""

import random
import operator
import matplotlib.pyplot

# Function to get a random integer from 0 - 99 using the randint function
# an alternative way would be int(random.random() * 100)


def getRndNumber():
    return random.randint(0, 99)


# An empty agents list to store all the initial x & y coordinate.
agents = []

# Variable to store the number of agents required.
num_of_agents = 10

# Variable to store the number of iterations required.
num_of_iterations = 100

# Loop thorough that amount of times and populate the agents list.
for i in range(num_of_agents):
    agents.append([getRndNumber(), getRndNumber()])


for j in range(num_of_iterations):
    # Use a loop to iterate through all the agents and move twice:
    for i in range(num_of_agents):

        # 1st move
        if random.random() < 0.5:
            # added torus - explanation below.
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        # 2nd move
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# Set up the axes for the plot - only need to do this once and not in the loop.
# this doesnt make the graph big enough to show all the cordinate when they are moved.
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# Loop through all the agents and create the points
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])

matplotlib.pyplot.show()

'''
The code in the part 3 Boundary Effects give an out of range error because because we
are trying to reference an index in the data list that is greater than 99 i.e. [j + 1]
or less than 0 i.e. [i - 1] and this is out of range and don't exist.
'''

'''
Torus
We have introduced the modulus (%) operator to the move code above. In this case it simply
sets the value to 0 if the move calculation exceeds 99 i.e. [99 + 1] % 100 is 1 eg print (100 % 100) outputs 0.
sets the value to 99 if the move calculation get below 0 i.e. [0 - 1] % 100 is 99 eg. print (-1 % 100) outputs 99.

Another solution to account for this could be to adjust the graph coordinates.
For example if the agent coordinate is [99, 99] then the move steps could change the y or x to 101.
same applies to the lowest values whcih could go below 0 to -2.
matplotlib.pyplot.ylim(-2, 101)
matplotlib.pyplot.xlim(-2, 101)
'''
