""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 6 - I/O
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020
Description: 
"""

import random
import operator
import matplotlib.pyplot
import csv
import agentframework

# create environment
environment = []
agents = []
num_of_iterations = 100
num_of_agents = 10


# Create the environments list by reading data from a text file.
# Used the csv import to parse the text file as it is comma seperated.
with open("assets/in.txt") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


# Create the agents list with the environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()


# Plot the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()
