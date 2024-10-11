from tkinter import *
# import required libraries

from equation_solver import EquationSolver
from basic_calculator import BasicCalculator

# import all modules

root = Tk()


# declaring the root variable to initialise the tkinter root window


# creating the main menu class below
class MainMenu:
    def __init__(self):  # I don't need to pass any parameters upon initialisation, all main menu windows are the same
        root.title("Main Menu")
        root.geometry("400x400")

        # name the window and make it 400 by 400 pixels

        basic_button_photo = PhotoImage(file="basic_operators.png")
        # import my image and assign it to a variable
        basic_button = Button(root, image=basic_button_photo, command=lambda: BasicCalculator(root))
        # create the button with the image as an attribute,
        # and give it a lambda command to create a basiccalculator object by passing the root variable
        basic_button.place(x=50, y=50)
        # place the button on the window

        equation_button_photo = PhotoImage(file="quadratic.png")
        equation_button = Button(root, image=equation_button_photo, command=lambda: EquationSolver(root))
        equation_button.place(x=250, y=50)
        # same as above

        root.mainloop()
        # start the mainloop


def start():
    MainMenu()


start()
# start the program
