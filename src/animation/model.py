""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 8 - Animation/Behaviour
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020

Description: Modified the Agent/Model interaction so that it animates using the matplotlib.animation library.
"""

import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import csv
import agentframework

# create environment
environment = []
agents = []
neighbourhood = 20
num_of_iterations = 100
num_of_agents = 10

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

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


def update(frame_number):

    fig.clear()
    global carry_on

    # Modified to use the Agent class methods
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

    # Plot the agents
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)


def gen_function(b=[0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a = a + 1


# Run the animation - This essentially shows the agents 'eating' their way through the raster!
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

# This will execute the animation (with the agents eating away) until the the 'carry_on'
# variable is set to false i.e. < 0.
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()
