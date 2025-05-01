import math
import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np

# import required modules


class Normal:
    def __init__(self, root):
        self.normalWindow = Toplevel(root)
        self.normalWindow.title("Normal Distribution")
        self.normalWindow.geometry("400x185")
        # create a class passing root variable in initialise function to create a toplevel window of the distribution
        # window, name "Normal Distribution" and window size 400 by 185
        self.tail_type = ttk.Combobox(self.normalWindow, width=15, state="readonly")
        # create a "combobox", essentially a drop-down list box
        # for selecting the type of tail to use for the distribution
        # I made it read only so only chosen values are valid
        self.tail_type.grid(column=0, row=0, padx=5)
        self.tail_type["values"] = ("X≤",
                                    "≤X≤",
                                    "X≥"
                                    )
        self.tail_type.set("X≤")
        # place this combobox at the top of the window using the grid placement method, and give it a set of possible
        # values to use, set the box to a value by default so the box isn't empty when the window initialises
        self.tail_type.bind("<<ComboboxSelected>>", lambda e: self.create_variables())
        # the tkinter bind method assigns a command, in this case, being the create variables method to the user
        # changing the value in the drop-down list
        self.input_frame = Frame(self.normalWindow)
        # create an input frame to include any dynamically drawn tkinter gui widgets
        self.input_frame.grid(column=0, row=1, padx=5, pady=5)
        self.create_variables()
        # upon initialising the window, call the create_variables method to draw the variable input boxes

    def create_variables(self):

        sigma_temp = ""
        if hasattr(self, "sigma_entry"):
            sigma_temp = self.sigma_entry.get()

        mu_temp = ""
        if hasattr(self, "mu_entry"):
            mu_temp = self.mu_entry.get()

        # if the input boxes have been drawn before, store their contents inside a temporary variable to be placed
        # back into the widget after it has been destroyed and redrawn

        for widget in self.input_frame.winfo_children():
            widget.destroy()

        # destroy all widgets within the input frame ready to be redrawn

        tail_type = self.tail_type.get()

        # get the tail type from the value of the drop-down box

        offset = 0
        # initialise a variable "offset" so the sigma and mu labels can be moved down accordingly if the two-tailed
        # option is chosen, meaning more input box widgets above them
        if tail_type == "≤X≤":
            offset = 1
            # set this offset to 1 if the two-tailed tail type is chosen
            Label(self.input_frame, text="Lower:").grid(row=0, column=0, padx=5)
            self.lower_entry = Entry(self.input_frame)
            self.lower_entry.grid(row=0, column=1, padx=5)

            Label(self.input_frame, text="Upper:").grid(row=1, column=0, padx=5)
            self.upper_entry = Entry(self.input_frame)
            self.upper_entry.grid(row=1, column=1, padx=5)

            # create two labels and entry boxes representing the inputs for the upper and lower bound of the tails

        else:
            Label(self.input_frame, text="x:").grid(row=0, column=0, padx=5)
            self.x_entry = Entry(self.input_frame)
            self.x_entry.grid(row=0, column=1, padx=5)

            # for any other tail type, simply add an input for the one tail

        Label(self.input_frame, text="σ:").grid(row=1 + offset, column=0, padx=5)
        self.sigma_entry = Entry(self.input_frame)
        self.sigma_entry.grid(row=1 + offset, column=1, padx=5)
        self.sigma_entry.insert(0, sigma_temp)

        Label(self.input_frame, text="μ:").grid(row=2 + offset, column=0, padx=5)
        self.mu_entry = Entry(self.input_frame)
        self.mu_entry.grid(row=2 + offset, column=1, padx=5)
        self.mu_entry.insert(0, mu_temp)

        # add the input labels and boxes for the standard deviation (sigma) and the mean (mu), their placement on the
        # grid is reliant on the offset variable depending on the tail type
        # if there is a temporary value for sigma or mu, insert it into the end of the result box

        self.execute_button = Button(self.normalWindow, text="Execute", bg="white", fg="blue", command=self.execute)
        self.execute_button.grid(row=2, column=0, padx=5)

        # at the bottom of the window, create an execute button to find the probability given the inputted parameters

    def normal_cdf(self, x, mu, sigma):
        return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))
        # defining the normal cumulative distribution function with parameters x, mu and sigma

    def execute(self):
        result_text = ""
        # create an empty variable result_text in case any errors are encountered and result_text is not created and
        # is tried to be passed as a variable
        if not hasattr(self, "result_label"):
            # to avoid redrawing the result label, check if it already exists before drawing it
            # this way it will only be drawn on the first press of the execute button, and will be modified afterward
            self.result_label = Label(self.normalWindow, justify=CENTER, wraplength=200)
            self.result_label.grid(row=0, column=1, padx=10, pady=5)
            self.result_label.config(font=("Arial", 15))
            # create the result label as a tkinter label widget with no text yet

        sigma = self.sigma_entry.get()
        mu = self.mu_entry.get()
        # get the results from the sigma and mu entry boxes
        try:
            if float(sigma) < 0:
                error_text = "standard deviation must be positive"
                self.result_label.config(text=error_text)
                # perform a check to verify that standard deviation (sigma) is positive
                # which it must be to complete this calculation
            else:
                sigma = float(sigma)
                mu = float(mu)
                # convert the sigma and mu variables to floats
                if self.tail_type.get() == "≤X≤":
                    lower = float(self.lower_entry.get())
                    upper = float(self.upper_entry.get())
                    # given that the tail type is ≤X≤, get the lower and upper bound values as floats
                    if lower > upper:
                        error_text = "the upper bound must be greater than the lower bound"
                        self.result_label.config(text=error_text)
                        return
                        # self-explanatory, a lower bound must be lower and an upper bound must be greater
                    else:
                        probability = self.normal_cdf(upper, mu, sigma) - self.normal_cdf(lower, mu, sigma)
                        # find the results when the cumulative distribution function is applied with the parameters
                        # given, and with the upper and lower bounds, then subtract these two to find the probability
                        # between these two bounds
                        formatted_probability = f"{probability:.6f}"
                        # round this probability to 6 decimal places
                        result_text = f"P({lower} ≤ X ≤ {upper}) = \n{formatted_probability}"
                        # this will show the result as this, for example:
                        #     P(3.0 ≤X≤ 5.0) =
                        #       0.382925

                else:
                    x = float(self.x_entry.get())
                    # if the tail type is not between two bounds, simply get the x value
                    if self.tail_type.get() == "X≥":
                        probability = 1 - self.normal_cdf(x, mu, sigma)
                        # if the tail type is X≥ the probability is 1 take the cumulative distribution function
                    else:
                        # otherwise, the tail type is X≤ and the probability simply the cumulative distribution function
                        probability = self.normal_cdf(x, mu, sigma)

                    formatted_probability = f"{probability:.6f}"
                    # round this probability to 6 decimal places

                    result_text = f"P({self.tail_type.get()} {x}) = \n{formatted_probability}"
                    # this will show the result as this, for example:
                    #   P(X≤ 4.0) =
                    #     0.736742

                self.result_label.config(text=result_text)
                # configure the result_label to have the text inside the variable result_text
        except:
            error_text = "Error"
            self.result_label.config(text=error_text)
            # check for any other miscellaneous errors
