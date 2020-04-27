""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 7 - Communicating
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020
"""

import random
import operator
import matplotlib.pyplot
import csv
import agentframework

# create environment
environment = []
agents = []
neighbourhood = 20
num_of_iterations = 100
num_of_agents = 10


# Create the environments list
with open("assets/in.txt") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


# Create the agents list with the environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


# Plot the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()
