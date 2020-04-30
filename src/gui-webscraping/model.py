""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 9 - GUI/Web scraping
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020

Description: Modified the Agent/Model interaction so that it animates using the matplotlib.animation library.
"""
import matplotlib
matplotlib.use('TkAgg')

import operator
import random
import csv
import agentframework
import tkinter
import matplotlib.pyplot
import matplotlib.animation


'''
import requests
import bs4
I couldn't get the above imports to work so didn't complete the web scraping exercise fully. 
I tried various solution but wasn't succesfull. The issue is possibly related to the 
Microsoft python extension for VS Code - I used this environment for all other development.

'''
# create environment
environment = []
agents = []
neighbourhood = 20
num_of_iterations = 100
num_of_agents = 10
canvas = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

# function to execute the model - this is called for the GUI menu and the button
def run_model():
    animation = matplotlib.animation.FuncAnimation(
        fig, update, frames=gen_function, repeat=False)
    canvas.draw()


root = tkinter.Tk()
root.wm_title("Model")

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

# Add extra code to show a button which will also run the model when clicked
frame = tkinter.Frame(root)
frame.pack()

button = tkinter.Button(frame, text="Run Model", fg="green", command=run_model)
button.pack()
# **************************************************************************

model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run_model)

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

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


# The update function is called when the animation runs to update the agents 
# by invoking move() and eat() methods of the Agent class.
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


tkinter.mainloop()
