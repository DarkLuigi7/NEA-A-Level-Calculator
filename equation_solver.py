import cmath
import math
from tkinter import *
from quadratic_solver import QuadraticSolver

from PIL import Image, ImageTk

# import required libraries


class SimultaneousSolver:
    # create the simultaneous equation solver class for the window
    def __init__(self, root):
        simultaneousSolverWindow = Toplevel(root)
        simultaneousSolverWindow.title("Simultaneous Equations")


class EquationSolver:
    # create the equation solver class for the menu window
    def __init__(self, root):
        equationSolverWindow = Toplevel(root)
        equationSolverWindow.title("Equation Solver")
        equationSolverWindow.geometry("500x200")
        # pass root as a parameter and configure the window size and title

        buttonquadratic = Button(equationSolverWindow, text="Quadratic", width=12,
                                 command=lambda: QuadraticSolver(root), relief=RAISED)
        buttonquadratic.grid(row=0, column=0, padx=3, pady=3)
        buttonquadratic.config(font=("Courier New", 24))

        buttonsimultaneous = Button(equationSolverWindow, text="Simultaneous", width=12,
                                    command=lambda: SimultaneousSolver(root), relief=RAISED)
        buttonsimultaneous.grid(row=0, column=1, padx=3, pady=3)
        buttonsimultaneous.config(font=("Courier New", 24))
        # give the window the two menu options, quadratic and simultaneous, and attatch to them a command to create a
        # new object of the desired window
