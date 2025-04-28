from tkinter import *
from tkinter import ttk
import numpy as np


# import required libraries

class SimultaneousSolver:
    def __init__(self, root):
        self.simultaneousSolverWindow = Toplevel(root)
        self.simultaneousSolverWindow.title("Simultaneous Equation Solver")
        # create a class passing root variable in initialise function to create a toplevel window of the main menu
        # window, name "Simultaneous Equation Solver"
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        # create an object attribute array containing the first twelve letters of the alphabet
        self.unknowns = ["x", "y", "z"]
        # create an object attribute array containing the three possible unknown variable letters
        self.alphabetindex = 0
        # create an object attribute index denoting the current position in the alphabet, used for drawing the equations

        self.option_frame = Frame(self.simultaneousSolverWindow)
        # create a frame to contain the two options for the number of unknowns
        self.option_frame.pack(pady=10)
        # place the frame using pack and give it a vertical padding of 10 pixels

        self.numunknowns = IntVar()
        # create self.unknowns as a tkinter IntVar variable
        # IntVar behaves the same as a python integer in all cases, but it allows me to use it within tkinter methods
        # as I have done below, to use it to create the radio buttons
        self.numunknowns.set(2)
        # set this IntVar to 2
        self.radio_two = Radiobutton(self.option_frame, text="2 Unknowns", variable=self.numunknowns, value=2,
                                     command=self.createinputboxes)
        self.radio_three = Radiobutton(self.option_frame, text="3 Unknowns", variable=self.numunknowns, value=3,
                                       command=self.createinputboxes)
        # create two radio buttons representing the user's choice between 2 or 3 unknowns placing it within the option
        # frame and giving it a command to draw the input boxes when clicked
        self.radio_two.pack(side=LEFT, padx=10)
        self.radio_three.pack(side=LEFT, padx=10)
        # place these buttons using the pack method, placing them on the left side of the option frame, and giving them
        # 10 pixels of horizontal padding

        self.input_frame = Frame(self.simultaneousSolverWindow)
        # create a second frame to hold the entry boxes for inputting coefficients, the solve button, and entry boxes
        # for receiving results
        self.input_frame.pack(pady=10)
        # place this frame using the pack method with a vertical padding of 10 pixels

        self.createinputboxes()
        # call the self.createinputboxes method

    def solve(self):
        # solve method
        coefficients_values = []
        # create an empty array to store the values of the coefficients
        for row in self.coefficients:
            # for every array in the two-dimensional array self.coefficients
            try:
                coefficients_row = [float(entry.get()) if entry.get() else 0 for entry in row]
                # list comprehension to create an array containing the number written in every entry in the row,
                # (on the left hand side of the equals sign) if there is nothing in the entry box, simply input 0
            except ValueError:
                # if converting the results from the results boxes into floats returns an error
                for item in self.solutions:
                    item.insert(END, "Error")
                    # insert error into all the solutions
            coefficients_values.append(coefficients_row)
            # append the array of the row of coefficients to the coefficients_values array
        vector_values = [float(entry.get()) if entry.get() else 0 for entry in self.vector]
        # list comprehension to create an array containing the number written in every entry in the row,
        # (on the right hand side of the equals sign) if there is nothing in the entry box, simply input 0
        coefficients = np.array(coefficients_values)
        vector = np.array(vector_values)
        # convert the coefficients and vector values two-dimensional arrays into numpy arrays so matrix calculations
        # can be applied to them
        self.answers = np.linalg.solve(coefficients, vector)
        # numpy's linalg function uses matrix calculations to solve systems of simultaneous equations
        index = 0
        # set the index to 0
        for item in self.solutions:
            # for every item in the self.solutions array
            item.delete(0, "end")
            # if any item currently in that position, delete it
            item.insert(END, self.answers[index])
            # and replace it with the solution just found
            index += 1
            # move to next solution

    def createinputboxes(self):
        # method to draw the input boxes
        self.alphabetindex = 0
        # return the alphabetindex to 0
        labels_text = [
            f"a(x)+b(y)=c",
            f"d(x)+e(y)=f",
        ]
        labels_text2 = [
            f"a(x)+b(y)+c(z)=d",
            f"e(x)+f(y)+g(z)=h",
            f"i(x)+j(y)+k(z)=l"
        ]
        # text for labels to demonstrate how to input simultaneous equations
        for widget in self.input_frame.winfo_children():
            widget.destroy()
            # destroy all current widgets in the input frame
        numunknowns = self.numunknowns.get()
        # get the number of unknowns
        self.solutions = []
        self.coefficients = []
        self.vector = []
        # create empty arrays to represent the solutions, coefficients, and constant terms
        for i in range(numunknowns):
            rows = []
            # store entries for the current row
            if numunknowns == 2:
                label = Label(self.input_frame, text=labels_text[i], justify="center")
            else:
                label = Label(self.input_frame, text=labels_text2[i], justify="center")
                # create equation labels based on the number of unknowns
            label.grid(row=3 + i, column=0, columnspan=4)
            # place these labels on the grid depending on i
            label.config(font=("Courier New", 12))
            for j in range(numunknowns):
                # loop through the number of unknowns to create coefficient labels and entry boxes
                label = Label(self.input_frame, text=f"{self.alphabet[self.alphabetindex]}=")
                # create a coefficient variable label iterating through the letters of the alphabet
                self.alphabetindex += 1
                # increment the alphabet index by 1
                label.grid(row=i, column=j * 2, padx=5, pady=5)
                entry = Entry(self.input_frame, width=5)
                entry.grid(row=i, column=j * 2 + 1, padx=5, pady=5)
                # create an entry box to enter the value of the coefficient
                rows.append(entry)
                # add this entry box object to the rows array

            label = Label(self.input_frame, text=f"{self.unknowns[i]}:")
            label.grid(row=numunknowns + 3, column=2 * i)
            entry = Entry(self.input_frame, width=5)
            entry.grid(row=numunknowns + 3, column=2 * i + 1)
            self.solutions.append(entry)
            # create a label and entry box for the solution and append the entry box to the solutions array

            self.coefficients.append(rows)
            # make the coefficients array a two-dimensional array containing the arrays rows

            label = Label(self.input_frame, text=f"{self.alphabet[self.alphabetindex]}=")
            self.alphabetindex += 1
            label.grid(row=i, column=numunknowns * 2 + 1, padx=5, pady=5)
            entry = Entry(self.input_frame, width=5)
            entry.grid(row=i, column=numunknowns * 2 + 2, padx=5, pady=5)
            self.vector.append(entry)
            # create and place the label and entry box for the constants in the simultaneous equations

        separator = ttk.Separator(self.input_frame, orient="vertical")
        separator.grid(row=0, column=numunknowns * 2, rowspan=numunknowns, sticky='ns', padx=5)
        # create and place seperator between the coefficients and the constants

        solvebutton = Button(self.input_frame, text="Solve", command=self.solve, relief=RAISED)
        solvebutton.grid(row=numunknowns + 1, column=numunknowns + 3)
        solvebutton.config(font=("Courier New", 12))
        # create and place solve button with command self.solve

        self.alphabetindex = 0
        # finally set the alphabet index to 0
