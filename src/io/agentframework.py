""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 6 - I/O
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020
Description: 
"""

import random


class Agent:
    def __init__(self, environment):
        self._y = random.randint(0, 99)
        self._x = random.randint(0, 99)
        self.environment = environment
        self.store = 0  # We'll come to this in a second.

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
