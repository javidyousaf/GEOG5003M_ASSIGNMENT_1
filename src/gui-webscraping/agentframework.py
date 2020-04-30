""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 9 - GUI/Web scraping
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020

Description: Standard Agent code that has been developed throughout the practicals
"""

import random
import math


class Agent:
    def __init__(self, environment, agents):
        self._y = random.randint(0, 99)
        self._x = random.randint(0, 99)
        self.environment = environment
        self.agents = agents
        self.store = 0

    # Getters and Setters for x and y property
    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

    def share_with_neighbours(self, neighbourhood):
        # shuffle the agents list before processing
        random.shuffle(self.agents)
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave
                agent.store = ave
                # print("sharing " + str(dist) + " " + str(ave))

    # Calculate distance between agents using pythagoras and the math library import
    def distance_between(self, agent):
        return math.sqrt(math.pow(self._x - agent._x, 2) + (math.pow(self._y - agent._y, 2)))
