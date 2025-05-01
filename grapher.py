from tkinter import *
from tkinter import ttk
import numpy as np
from turtle import *
import math
from turtlegraph import Plotter


# import required libraries

class CreateEquation:
    def __init__(self, functype, function, colour):
        self.functype = functype
        self.function = function
        self.colour = colour
    # create a class responsible for creating objects representing functions to be graphed passing all attributes of
    # every function, so they can be passed to the turtle graphing file to draw


class Grapher:
    def __init__(self, root):
        self.grapherWindow = Toplevel(root)
        self.grapherWindow.title("Graphing Calculator")
        self.grapherWindow.geometry("300x250")
        # create a class passing root variable in initialise function to create a toplevel window of the main menu
        # window, name "Graphing Calculator", background colour black and window size 300 by 250
        self.colour_rotation = ["black", "blue", "red", "green"]
        # define a "colour rotation" array, to cycle through, so each function is potted with a different colour
        self.colour_index = -1
        # set the index for the colour rotation to -1
        self.equations = []
        # initialise the equations array to add any inputted equations to
        self.equation_type = ttk.Combobox(self.grapherWindow, width=15, state="readonly")
        # create a "combobox", essentially a drop-down list box
        # for selecting the type of equation to use for the graph
        # I made it read only so only chosen values are valid
        self.equation_type.grid(column=0, row=0, padx=5)
        self.equation_type["values"] = ("y=",
                                        "x="
                                        )
        # place this combobox on the grid and give it two possible values
        self.equation_type.set("y=")
        # as the window initialises, give the combobox the default value "y="
        self.equation_entry = Entry(self.grapherWindow, width=30)
        self.equation_entry.grid(row=1, column=0, padx=5, pady=5)
        # create a text box to enter algebraic expressions and place it below the combobox
        self.equation_list_frame = LabelFrame(self.grapherWindow, text="Equations", padx=5, pady=5)
        self.equation_list_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        # create a frame to store the dynamically created equations when the add button is pressed and place it
        # below the combobox and entry box
        self.add_button = Button(self.grapherWindow, text="+", command=self.add_equation)
        self.add_button.grid(row=1, column=1, padx=5)
        self.add_button.config(font=("Courier New", 15))
        # create an add button with an attached command to add the equation currently in the entry box to the list
        # of equations
        self.graph_button = Button(self.grapherWindow, text="Graph", command=self.plot_graph)
        self.graph_button.grid(row=3, column=0, columnspan=2, pady=5)
        # finally, create a button below the equation list frame with a command to draw the inputted functions

    def add_equation(self):
        equation_text = self.equation_entry.get()
        equation_type = self.equation_type.get()
        # get the equation text and type from the entry box and combobox respectively
        colour = self.colour_rotation[(self.colour_index + 1) % len(self.colour_rotation)]
        # set the assigned colour of the equation to the next colour available in the colour rotation using modular
        # arithmetic division function to cycle through it
        currentequation = CreateEquation(equation_type, equation_text, colour)
        # create an object for the equation using the currentequation class by passing parameters equation_type
        # equation_text and colour for easier accessing of the equations attributes when it is drawn
        self.colour_index += 1
        # increment the colour index by one
        self.equations.append(currentequation)
        # add this equation object to the equations array attribute to store for drawing

        equation_frame = Frame(self.equation_list_frame)
        equation_frame.grid(sticky="ew", padx=5, pady=2)
        # create another frame inside the equation grid frame to store both the label of the equation and the delete
        # button

        label = Label(equation_frame, text=f"{equation_type} {equation_text}", anchor="w", fg=colour)
        label.grid(row=0, column=0, padx=5, sticky="w")
        # create a label as part of the equation frame with its text as the equation type and equation text as inputted
        # by the user

        delete_button = Button(equation_frame, text="X", fg="red",
                               command=lambda: self.remove_equation(currentequation, equation_frame))
        delete_button.grid(row=0, column=1, padx=5)
        # create a delete button to go with the equation with a command to delete the given equation given the
        # equation object and its frame

        self.equation_entry.delete(0, "end")
        # finally, delete the text stored in the entry box currently

    def remove_equation(self, equation, frame):
        # this method is called when the delete button is pressed
        # given the frame and equation objects as parameters
        self.equations.remove(equation)
        # remove the equation object from the equations array attribute
        frame.destroy()
        # destroy the frame object using the tkinter destroy method

    def plot_graph(self):
        # this method is called when the graph button is pressed
        if not self.equations:
            # checking if the equations array attribute is empty
            return
            # if so, end the function here
        plotter = Plotter(self.equations, -10, 10, -10, 10)
        # otherwise, create an object of the class Plotter from the file turtlegraph.py
        plotter.plot()
        # call the plot method of the object we have just created to draw the graph
