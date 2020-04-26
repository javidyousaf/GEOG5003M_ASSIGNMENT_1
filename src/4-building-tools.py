"""
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 4 - Building tools
Author: Javid Yousaf
Student id: 201385963
Date: 02/03/2020
"""

import random
import operator
import matplotlib.pyplot
import math
import time


# function uses pythagoras to calculate the distance between 2 agents
def distance_between(agent_a, agent_b):
    return (((agent_a[0] - agent_b[0])**2) + ((agent_a[1] - agent_b[1])**2))**0.5
    # An alternative way or writing this function would be using the math import.
    # return math.sqrt(math.pow(agent_a[0] - agent_b[0], 2) + (math.pow(agent_a[1] - agent_b[1], 2)))


num_of_agents = 100
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


# This gets the distance between the first and second agents in the agents list

answer = distance_between(agents[0], agents[1])
print(answer)

# check distance between every agent against ever other agent:

# time.clock() no longer works as it has been deprecated see: https://stackoverflow.com/questions/58569361/attributeerror-module-time-has-no-attribute-clock-in-python-3-8.
# As I am using python 3.8.2 I will use:
start = time.perf_counter()

minimum_distance = 0
maximum_distance = 0

for i in range(num_of_agents):
    for j in range(num_of_agents):
        answer = distance_between(agents[i], agents[j])
        print(answer)

end = time.perf_counter()

# Print execution time for calculating distances between all agents
print("time = " + str(end - start))


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
matplotlib.pyplot.show()
