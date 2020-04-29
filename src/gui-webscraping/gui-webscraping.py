""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 9 - GUI/Web scraping
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020

Description: Testing a basic GUI as outlined in the practical
"""

import matplotlib
matplotlib.use('TkAgg')

import tkinter

def run():
    pass

# Just showing menu elements
root = tkinter.Tk()
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # Wait for interactions.