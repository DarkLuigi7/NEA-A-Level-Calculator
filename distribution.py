from tkinter import *
from normal import Normal
from binomial import Binomial
from PIL import Image, ImageTk

# import required modules


class Distribution:
    def __init__(self, root):
        distributionWindow = Toplevel(root)
        distributionWindow.title("Distributions")
        distributionWindow.geometry("500x75")
        # create a class passing root variable in initialise function to create a toplevel window of the main menu
        # window, name "Distributions" and window size 500 by 75

        buttonbinomial = Button(distributionWindow, text="Binomial", width=12,
                                 command=lambda: Binomial(root), relief=RAISED)
        buttonbinomial.grid(row=0, column=0, padx=3, pady=3)
        buttonbinomial.config(font=("Courier New", 24))

        buttonnormal = Button(distributionWindow, text="Normal", width=12,
                                    command=lambda: Normal(root), relief=RAISED)
        buttonnormal.grid(row=0, column=1, padx=3, pady=3)
        buttonnormal.config(font=("Courier New", 24))

        # create two buttons for opening the binomial and normal distribution windows

