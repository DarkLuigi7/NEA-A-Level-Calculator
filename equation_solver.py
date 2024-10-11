import cmath
import math
from tkinter import *

from PIL import Image, ImageTk


class QuadraticSolver:
    def __init__(self, root):
        quadraticSolverWindow = Toplevel(root)
        quadraticSolverWindow.title("Quadratic Solver")
        quadraticSolverWindow.geometry("400x200")

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

        self.xsquared = ImageTk.PhotoImage((Image.open("quadratic.png")).resize((30, 30), Image.Resampling.LANCZOS))

        xsquaredlabel = Label(quadraticSolverWindow, image=self.xsquared)
        xsquaredlabel.grid(row=0, column=2)
        xsquaredlabel.image = self.xsquared

        pluslabel1 = Label(quadraticSolverWindow, text="+")
        pluslabel1.config(font=("Courier New", 22))
        pluslabel1.grid(row=0, column=4)

        self.xsymbol = ImageTk.PhotoImage((Image.open("x_symbol.png")).resize((30, 30), Image.Resampling.LANCZOS))

        xlabel = Label(quadraticSolverWindow, image=self.xsymbol)
        xlabel.grid(row=0, column=7)
        xlabel.image = self.xsymbol

        pluslabel2 = Label(quadraticSolverWindow, text="+")
        pluslabel2.config(font=("Courier New", 22))
        pluslabel2.grid(row=0, column=8)

        equalszerolabel = Label(quadraticSolverWindow, text="= 0")
        equalszerolabel.config(font=("Courier New", 22))
        equalszerolabel.grid(row=0, column=11)

        buttonsolve = Button(quadraticSolverWindow, text="Solve", width=12, command=self.solve, relief=RAISED)
        buttonsolve.grid(row=1, column=0, columnspan=11, pady=10)
        buttonsolve.config(font=("Courier New", 18))

        x1label = Label(quadraticSolverWindow, text="x1 :")
        x1label.config(font=("Courier New", 18))
        x1label.grid(row=2, column=0)

        x1box = Entry(quadraticSolverWindow, width=8, relief=SUNKEN)
        x1box.grid(row=2, column=2, columnspan=4, pady=10, padx=10)
        x1box.config(font=("Arial", 18))
        self.x1box = x1box

        x2label = Label(quadraticSolverWindow, text="x2 :")
        x2label.config(font=("Courier New", 18))
        x2label.grid(row=2, column=7)

        x2box = Entry(quadraticSolverWindow, width=8, relief=SUNKEN)
        x2box.grid(row=2, column=8, columnspan=4, pady=10, padx=10)
        x2box.config(font=("Arial", 18))
        self.x2box = x2box

    def solve(self):
        a = eval(self.coeffbox1.get())
        b = eval(self.coeffbox2.get())
        c = eval(self.coeffbox3.get())
        x = []
        try:
            x.append((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
        except ValueError:
            if True:
                cmplx = ((-b + cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
                alpha = cmplx.real
                if alpha.is_integer:
                    alpha = int(alpha)
                    pass
                beta = cmplx.imag
                if beta.is_integer:
                    beta = int(beta)
                    pass
                x.append(f"{alpha}+{beta}i")
            else:
                x.append("Complex")

        try:
            x.append((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        except ValueError:
            if True:
                cmplx = ((-b - cmath.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
                alpha = cmplx.real
                if alpha.is_integer:
                    alpha = int(alpha)
                    pass
                beta = cmplx.imag
                if beta.is_integer:
                    beta = int(beta)
                    pass
                x.append(f"{alpha}+{beta}i")
            else:
                x.append("Complex")

        for i in range(len(x)):
            try:
                if x[i].is_integer():
                    x[i] = int(x[i])
            except:
                pass

        self.x1box.delete(0, "end")
        self.x2box.delete(0, "end")
        self.x1box.insert(END, x[0])
        self.x2box.insert(END, x[1])


class SimultaneousSolver:
    def __init__(self, root):
        simultaneousSolverWindow = Toplevel(root)


class EquationSolver:
    def __init__(self, root):
        equationSolverWindow = Toplevel(root)
        equationSolverWindow.title("Equation Solver")
        equationSolverWindow.geometry("500x200")

        buttonquadratic = Button(equationSolverWindow, text="Quadratic", width=12,
                                 command=lambda: QuadraticSolver(root), relief=RAISED)
        buttonquadratic.grid(row=0, column=0, padx=3, pady=3)
        buttonquadratic.config(font=("Courier New", 24))

        buttonsimultaneous = Button(equationSolverWindow, text="Simultaneous", width=12,
                                    command=lambda: SimultaneousSolver(root), relief=RAISED)
        buttonsimultaneous.grid(row=0, column=1, padx=3, pady=3)
        buttonsimultaneous.config(font=("Courier New", 24))
