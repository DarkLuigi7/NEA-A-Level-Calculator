from tkinter import *
from equation_solver import EquationSolver
from basic_calculator import BasicCalculator
from grapher import Grapher
from distribution import Distribution

# import required modules

root = Tk()

# declaring the root variable to initialise the tkinter root window


class MainMenu:
    def __init__(self):  # I don't need to pass any parameters upon initialisation, all main menu windows are the same
        root.title("Main Menu")
        root.geometry("400x400")

        # name the window and make it 400 by 400 pixels

        basic_button_photo = PhotoImage(file="basic_operators.png")
        # import the basic operators image and assign it to a variable
        basic_button = Button(root, image=basic_button_photo, command=lambda: BasicCalculator(root))
        # create the button with the image as an attribute,
        # and give it a lambda command to create a basiccalculator object by passing the root variable
        basic_button.place(x=50, y=50)
        # place the button on the window on the top left

        equation_button_photo = PhotoImage(file="quadratic.png")
        equation_button = Button(root, image=equation_button_photo, command=lambda: EquationSolver(root))
        equation_button.place(x=250, y=50)
        # same as above, placing the button on the top right

        distribution_button_photo = PhotoImage(file="distribution.png")
        distribution_button = Button(root, image=distribution_button_photo, command=lambda: Distribution(root))
        distribution_button.place(x=50, y=250)
        # placing the button on the bottom left

        grapher_button_photo = PhotoImage(file="grapher.png")
        grapher_button = Button(root, image=grapher_button_photo, command=lambda: Grapher(root))
        grapher_button.place(x=250, y=250)
        # placing the button on the bottom right

        root.mainloop()
        # start the mainloop


def start():
    MainMenu()
    # function to create a mainmenu object and therefore start the program


start()
# start the program
