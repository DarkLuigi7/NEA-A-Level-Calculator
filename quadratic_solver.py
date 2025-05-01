import cmath
import math
from tkinter import *

from PIL import Image, ImageTk


# import required libraries

class QuadraticSolver:
    # creating the quadratic solver class for the window
    def __init__(self, root):

        self.complex_mode = False

        quadraticSolverWindow = Toplevel(root)
        quadraticSolverWindow.title("Quadratic Solver")
        quadraticSolverWindow.geometry("400x200")
        # pass root as a parameter and configure the window size and title

        coeffbox1 = Entry(quadraticSolverWindow, width=3, relief=SUNKEN)
        coeffbox1.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        coeffbox1.config(font=("Arial", 18))
        coeffbox1.focus_set()
        self.coeffbox1 = coeffbox1

        coeffbox2 = Entry(quadraticSolverWindow, width=3, relief=SUNKEN)
        coeffbox2.grid(row=0, column=5, columnspan=2, pady=10, padx=10)
        coeffbox2.config(font=("Arial", 18))
        self.coeffbox2 = coeffbox2

        coeffbox3 = Entry(quadraticSolverWindow, width=3, relief=SUNKEN)
        coeffbox3.grid(row=0, column=9, columnspan=2, pady=10, padx=10)
        coeffbox3.config(font=("Arial", 18))
        self.coeffbox3 = coeffbox3

        # create the three boxes for inputting the coefficients of the equation

        self.xsquared = ImageTk.PhotoImage((Image.open("quadratic.png")).resize((30, 30), Image.Resampling.LANCZOS))
        # creating the xsquared image as a tkinter photoimage object, to place it in front of the first coefficient box

        xsquaredlabel = Label(quadraticSolverWindow, image=self.xsquared)
        xsquaredlabel.grid(row=0, column=2)
        xsquaredlabel.image = self.xsquared

        pluslabel1 = Label(quadraticSolverWindow, text="+")
        pluslabel1.config(font=("Courier New", 22))
        pluslabel1.grid(row=0, column=4)
        # create the first label plus inbetween the first two coefficients

        self.xsymbol = ImageTk.PhotoImage((Image.open("x_symbol.png")).resize((30, 30), Image.Resampling.LANCZOS))
        # creating the xsymbol image as a tkinter photoimage object, to place it in front of the first coefficient box

        xlabel = Label(quadraticSolverWindow, image=self.xsymbol)
        xlabel.grid(row=0, column=7)
        xlabel.image = self.xsymbol

        pluslabel2 = Label(quadraticSolverWindow, text="+")
        pluslabel2.config(font=("Courier New", 22))
        pluslabel2.grid(row=0, column=8)
        # create the second label plus inbetween the first two coefficients

        equalszerolabel = Label(quadraticSolverWindow, text="= 0")
        equalszerolabel.config(font=("Courier New", 22))
        equalszerolabel.grid(row=0, column=11)
        # create a label, showing equals zero at the end of the equation

        buttonsolve = Button(quadraticSolverWindow, text="Solve", width=12, command=self.solve, relief=RAISED)
        buttonsolve.grid(row=1, column=0, pady=10, padx=10, columnspan=6)
        buttonsolve.config(font=("Courier New", 18))
        # add a button to solve the equation, with command being the function solve

        complex_checkbox = Checkbutton(quadraticSolverWindow, text="Complex", command=self.toggle_complex_mode,
                                       font=("Courier New", 12))
        complex_checkbox.grid(row=1, column=7, pady=10, padx=15, columnspan=3)
        self.complex_checkbox = complex_checkbox

        x1label = Label(quadraticSolverWindow, text="x1 :")
        x1label.config(font=("Courier New", 18))
        x1label.grid(row=2, column=0)
        # add a label to denote the first solution to the equation

        x1box = Entry(quadraticSolverWindow, width=8, relief=SUNKEN)
        x1box.grid(row=2, column=2, columnspan=4, pady=10, padx=10)
        x1box.config(font=("Arial", 18))
        self.x1box = x1box
        # add a box to display the first solution to the equation

        x2label = Label(quadraticSolverWindow, text="x2 :")
        x2label.config(font=("Courier New", 18))
        x2label.grid(row=2, column=7)
        # add a label to denote the second solution to the equation

        x2box = Entry(quadraticSolverWindow, width=8, relief=SUNKEN)
        x2box.grid(row=2, column=8, columnspan=4, pady=10, padx=10)
        x2box.config(font=("Arial", 18))
        self.x2box = x2box
        # add a box to display the first solution to the equation

    def toggle_complex_mode(self):
        if self.complex_mode:
            self.complex_mode = False
        else:
            self.complex_mode = True

    def solve(self):
        # this method solves the quadratic equation, given three coefficients
        try:
            if self.coeffbox1.get() == "":
                raise ValueError
                # raise an error if the a coefficient box is empty, as it is no longer a quadratic equation
            else:
                a = eval(self.coeffbox1.get())
                if a == 0:
                    self.x1box.delete(0, "end")
                    self.x1box.insert(END, "Error")
                    self.x2box.delete(0, "end")
                    self.x2box.insert(END, "Error")
                    return
            if self.coeffbox2.get() == "":
                b = 0
            else:
                b = eval(self.coeffbox2.get())
            if self.coeffbox3.get() == "":
                c = 0
            else:
                c = eval(self.coeffbox3.get())
            # if the box is empty, assume the number is zero, otherwise get the vales from the boxes and assign them to
            # the coefficient variables
        except:
            self.x1box.delete(0, "end")
            self.x1box.insert(END, "Error")
            self.x2box.delete(0, "end")
            self.x2box.insert(END, "Error")
            return

        if not (type(a) in (int, float) or type(b) in (int, float) or type(c) in (int, float)):
            self.x1box.delete(0, "end")
            self.x1box.insert(END, "Error")
            self.x2box.delete(0, "end")
            self.x2box.insert(END, "Error")
            return

        # evaluate the contents of the boxes in the window so that math.sqrt(2), for example is accepted as a valid
        # coefficient
        x = []
        # create an empty array to place the answer(s) in once done
        try:
            x.append((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
            # given that the answer is not complex (hence the try:), append the first value received when the
            # quadratic equation is applied on the three coefficients
        except ValueError:
            # given that the answer is complex, and the complex mode is turned on, give the answer in the form a+bi
            if self.complex_mode:
                # checking if the complex mode is turned on
                cmplx = ((-b + cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
                # use cmath to complete a square root function on a negative number, with the quadratic formula,
                # and store the result as a complex object in a variable: cmplx
                alpha = cmplx.real
                print(alpha)
                # let alpha equal the real part of the complex number "cmplx"
                if alpha.is_integer():
                    alpha = int(alpha)
                    print(alpha)
                    # given that alpha is an integer, convert it to the integer file type to eliminate results like:
                    # "1.0"
                beta = cmplx.imag
                print(beta)
                # let beta equal the imaginary part of the complex number "cmplx"
                if beta.is_integer():
                    beta = int(beta)
                    print(beta)
                    # given that beta is an integer, convert it to the integer file type to eliminate results like:
                    # "1.0"
                x.append(f"{alpha}+{beta}i")
                # append to the array x the complex number given as a string
            else:
                x.append("Complex")
                # if complex mode is off, append as the answer "Complex"

        try:
            x.append((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
            # given that the answer is not complex (hence the try:), append the first value received when the
            # quadratic equation is applied on the three coefficients
        except ValueError:
            # given that the answer is complex, and the complex mode is turned on, give the answer in the form a+bi
            if self.complex_mode:
                # checking if the complex mode is turned on
                cmplx = ((-b - cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
                # use cmath to complete a square root function on a negative number, with the quadratic formula,
                # and store the result as a complex object in a variable: cmplx
                alpha = cmplx.real
                # let alpha equal the real part of the complex number "cmplx"
                if alpha.is_integer:
                    alpha = int(alpha)
                    # given that alpha is an integer, convert it to the integer file type to eliminate results like:
                    # "1.0"
                    pass
                beta = cmplx.imag
                # let beta equal the imaginary part of the complex number "cmplx"
                if beta.is_integer:
                    beta = int(beta)
                    # given that beta is an integer, convert it to the integer file type to eliminate results like:
                    # "1.0"
                    pass
                x.append(f"{alpha}+{beta}i")
                # append to the array x the complex number given as a string
            else:
                x.append("Complex")
                # if complex mode is off, append as the answer "Complex"

        for i in range(len(x)):
            try:
                if x[i].is_integer():
                    x[i] = int(x[i])
                    # check if each result in the array x is an integer, and if so, convert it to the integer data type
            except:
                pass

        self.x1box.delete(0, "end")
        self.x2box.delete(0, "end")
        self.x1box.insert(END, x[0])
        self.x2box.insert(END, x[1])
        # delete any previous values inside the result boxes, and insert the new ones
