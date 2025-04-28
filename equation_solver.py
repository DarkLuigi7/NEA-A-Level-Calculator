from tkinter import *
from quadratic_solver import QuadraticSolver
from simultaneous_solver import SimultaneousSolver


# import required modules

class EquationSolver:
    def __init__(self, root):
        equationSolverWindow = Toplevel(root)
        equationSolverWindow.title("Equation Solver")
        equationSolverWindow.geometry("500x75")

        # create a class passing root variable in initialise function to create a toplevel window object
        # of the distribution window, name "Equation Solver" and window size 500 by 75

        buttonquadratic = Button(equationSolverWindow, text="Quadratic", width=12,
                                 command=lambda: QuadraticSolver(root), relief=RAISED)
        buttonquadratic.grid(row=0, column=0, padx=3, pady=3)
        buttonquadratic.config(font=("Courier New", 24))
        # create a tkinter button object with text "Quadratic", and command being a lambda function creating an
        # object of the QuadraticSolver class, with root passed as a parameter, place this button in the window

        buttonsimultaneous = Button(equationSolverWindow, text="Simultaneous", width=12,
                                    command=lambda: SimultaneousSolver(root), relief=RAISED)
        buttonsimultaneous.grid(row=0, column=1, padx=3, pady=3)
        buttonsimultaneous.config(font=("Courier New", 24))
        # create a tkinter button object with text "Simultaneous", and command being a lambda function creating an
        # object of the SimultaneousSolver class, with root passed as a parameter, place this button in the window
