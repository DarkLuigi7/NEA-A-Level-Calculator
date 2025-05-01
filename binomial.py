import math
import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np


# import required modules


class Binomial:
    def __init__(self, root):
        self.binomialWindow = Toplevel(root)
        self.binomialWindow.title("Binomial Distribution")
        self.binomialWindow.geometry("400x185")
        # create a class passing root variable in initialise function to create a toplevel window of the distribution
        # window, name "Binomial Distribution" and window size 400 by 185
        self.tail_type = ttk.Combobox(self.binomialWindow, width=15, state="readonly")
        # create a "combobox", essentially a drop-down list box
        # for selecting the type of tail to use for the distribution
        # I made it read only so only chosen values are valid
        self.tail_type.grid(column=0, row=0, padx=5)
        self.tail_type["values"] = ("X≤",
                                    "≤X≤",
                                    "X≥",
                                    "X="
                                    )
        self.tail_type.set("X≤")
        # place this combobox at the top of the window using the grid placement method, and give it a set of possible
        # values to use, set the box to a value by default so the box isn't empty when the window initialises
        self.tail_type.bind("<<ComboboxSelected>>", lambda e: self.create_variables())
        # the tkinter bind method assigns a command, in this case, being the create variables method to the user
        # changing the value in the drop-down list
        self.input_frame = Frame(self.binomialWindow)
        # create an input frame to include any dynamically drawn tkinter gui widgets
        self.input_frame.grid(column=0, row=1, padx=5, pady=5)
        self.create_variables()
        # upon initialising the window, call the create_variables method to draw the variable input boxes

    def create_variables(self):

        numtrial_temp = ""
        if hasattr(self, "numtrial_entry"):
            numtrial_temp = self.numtrial_entry.get()

        p_temp = ""
        if hasattr(self, "p_entry"):
            p_temp = self.p_entry.get()

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

        Label(self.input_frame, text="n:").grid(row=1 + offset, column=0, padx=5)
        self.n_entry = Entry(self.input_frame)
        self.n_entry.grid(row=1 + offset, column=1, padx=5)
        self.n_entry.insert(0, numtrial_temp)

        Label(self.input_frame, text="p:").grid(row=2 + offset, column=0, padx=5)
        self.p_entry = Entry(self.input_frame)
        self.p_entry.grid(row=2 + offset, column=1, padx=5)
        self.p_entry.insert(0, p_temp)

        # add the input labels and boxes for the standard number of trials (n) and the probability (p),
        # their placement on the grid is reliant on the offset variable depending on the tail type if there is a
        # temporary value for sigma or mu, insert it into the end of the result box

        self.execute_button = Button(self.binomialWindow, text="Execute", bg="white", fg="blue", command=self.execute)
        self.execute_button.grid(row=2, column=0, padx=5)

        # at the bottom of the window, create an execute button to find the probability given the inputted parameters

    def execute(self):
        result_text = ""
        # create an empty variable result_text in case any errors are encountered and result_text is not created and
        # is tried to be passed as a variable
        if not hasattr(self, "result_label"):
            # to avoid redrawing the result label, check if it already exists before drawing it
            # this way it will only be drawn on the first press of the execute button, and will be modified afterward
            self.result_label = Label(self.binomialWindow, justify=CENTER, wraplength=200)
            self.result_label.grid(row=0, column=1, padx=10, pady=5)
            self.result_label.config(font=("Arial", 15))
            # create the result label as a tkinter label widget with no text yet

        n = self.n_entry.get()
        p = self.p_entry.get()
        # get the results from the numtrial and probability entry boxes
        try:
            if not float(n).is_integer():
                error_text = "number of trials must be an integer"
                self.result_label.config(text=error_text)
                # perform a check to see if the number of trials is an integer, which it, along with every variable other
                # than probability must be to complete this calculation
            elif float(p) > 1 or float(p) < 0:
                error_text = "probability must be between 0 and 1"
                self.result_label.config(text=error_text)
                # perform a check to see if the inputted probability is inbetween 0 and 1
                # which is what a probability is, by definition
            else:
                n = int(n)
                p = float(p)
                # convert the n variable to an integer and the p variable to a float
                if self.tail_type.get() == "≤X≤":
                    lower = float(self.lower_entry.get())
                    upper = float(self.upper_entry.get())
                    # given that the tail type is ≤X≤, get the lower and upper bound values as floats
                    if not lower.is_integer() or not upper.is_integer():
                        error_text = "both bounds must be integers"
                        self.result_label.config(text=error_text)
                        # check if both bounds can be expressed as integers
                    elif not (0 <= lower <= n and 0 <= upper <= n):
                        error_text = "both bounds must be inbetween 0 and the number of trials"
                        self.result_label.config(text=error_text)
                        # check if both bounds lie within the range of 0 and the number of trials
                    elif lower > upper:
                        error_text = "the lower bound must be less than or equal to the upper bound"
                        self.result_label.config(text=error_text)
                        # check that the lower bound is in fact the lower of the two bounds
                    else:
                        # given that the variables inputted have passed these tests...
                        probability = 0
                        # initialise the final probability variable and set it to 0
                        for k in range(int(lower), int(upper)):
                            # for every integer k from the lower bound to the upper bound
                            nCp = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
                            # define the result of the combination function of n and k as nCp
                            probability += nCp * p ** k * (1 - p) ** (n - k)
                            # add to the probability variable the result of the probability mass function for binomial
                            # distribution with the given parameters for each integer k

                            formatted_probability = f"{probability:.6f}"
                            # round this probability to 6 decimal places
                            result_text = f"P({lower} ≤ X ≤ {upper}) = \n{formatted_probability}"
                            # this will show the result as this, for example:
                            #     P(3.0 ≤X≤ 5.0) =
                            #       0.546875
                else:
                    x = self.x_entry.get()
                    # if tail_type is not ≤X≤, simply get the x value
                    if not float(x).is_integer():
                        error_text = "number of successes must be an integer"
                        self.result_label.config(text=error_text)
                        # check if the number of successes can be expressed as integers
                    elif not (0 <= int(x) <= n):
                        error_text = "number of successes must be inbetween 0 and the number of trials"
                        self.result_label.config(text=error_text)
                        # check that the number of successes lies within the range of 0 and the number of trials
                    else:
                        # given that none of these errors have been triggered...
                        x = int(x)
                        # get the x value as an integer
                        if self.tail_type.get() == "X≤":
                            probability = 0
                            for k in range(x + 1):
                                nCp = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
                                # define the result of the combination function of n and k as nCp
                                probability += nCp * p ** k * (1 - p) ** (n - k)
                                # add to the probability variable the result of the probability mass function for binomial
                                # distribution with the given parameters
                            formatted_probability = f"{probability:.6f}"
                            # round this probability to 6 decimal places
                            result_text = f"P(X ≤ {x}) = \n{formatted_probability}"
                            # this will show the result as this, for example:
                            #   P(X≤ 4.0) =
                            #    0.200121
                        elif self.tail_type.get() == "X≥":
                            probability = 0
                            for k in range(x, n + 1):
                                nCp = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
                                # define the result of the combination function of n and k as nCp
                                probability += nCp * p ** k * (1 - p) ** (n - k)
                                # add to the probability variable the result of the probability mass function for binomial
                                # distribution with the given parameters
                            formatted_probability = f"{probability:.6f}"
                            # round this probability to 6 decimal places
                            result_text = f"P(X ≥ {x}) = \n{formatted_probability}"
                            # this will show the result as this, for example:
                            #   P(X ≥ 4.0) =
                            #    0.200121
                        elif self.tail_type.get() == "X=":
                            nCp = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
                            # define the result of the combination function of n and x as nCp
                            probability = nCp * p ** x * (1 - p) ** (n - x)
                            # set  the probability variable the to result of the probability mass function for binomial
                            # distribution with the given parameters
                            formatted_probability = f"{probability:.6f}"
                            # round this probability to 6 decimal places
                            result_text = f"P(X = {x}) = \n{formatted_probability}"
                            # this will show the result as this, for example:
                            #   P(X = 4.0) =
                            #    0.200121

            self.result_label.config(text=result_text)
            # configure the result_label to have the text inside the variable result_text
        except:
            error_text = "Error"
            self.result_label.config(text=error_text)
            # check for any other miscellaneous errors

