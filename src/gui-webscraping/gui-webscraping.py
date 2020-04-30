""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Practical: 9 - GUI/Web scraping
Author: Javid Yousaf
Student id: 201385963
Date: 01/05/2020

Description: Testing a basic GUI as outlined in the lectures and practical
"""

import tkinter

# This code will open a GUI window with a dropdown menu with option to run the model
# In this case the run_model() function just prints to the console window.
def run_model():
    print("model run has started!")

# Showing menu elements
root = tkinter.Tk()
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)

# Add experimental code to display a button that also runs the model when clicked.
frame = tkinter.Frame(root)
frame.pack()

button = tkinter.Button(frame,
                        text="Run Model",
                        fg="green",
                        command=run_model)
button.pack()

model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run_model)

tkinter.mainloop()
