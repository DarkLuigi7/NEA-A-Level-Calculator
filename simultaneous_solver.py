from tkinter import *
from tkinter import ttk
import numpy as np


class SimultaneousSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simultaneous Equation Solver")
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        self.unknowns = ["x", "y", "z"]
        self.alphabetindex = 0

        self.option_frame = Frame(root)
        self.option_frame.pack(pady=10)

        self.numunknowns = IntVar()
        self.numunknowns.set(2)
        self.radio_two = Radiobutton(self.option_frame, text="2 Unknowns", variable=self.numunknowns, value=2,
                                     command=self.createinputboxes)
        self.radio_three = Radiobutton(self.option_frame, text="3 Unknowns", variable=self.numunknowns, value=3,
                                       command=self.createinputboxes)
        self.radio_two.pack(side=LEFT, padx=10)
        self.radio_three.pack(side=LEFT, padx=10)

        self.root = Frame(root)
        self.root.pack(pady=10)

        self.createinputboxes()

    def solve(self):
        coefficients_values = []
        for row in self.coefficients:
            coefficients_row = [float(entry.get()) if entry.get() else 0 for entry in row]
            coefficients_values.append(coefficients_row)
        vector_values = [float(entry.get()) if entry.get() else 0 for entry in self.vector]
        coefficients = np.array(coefficients_values)
        vector = np.array(vector_values)
        unknowns = np.linalg.solve(coefficients, vector)
        for item in self.solutions:


    def createinputboxes(self):
        labels_text = [
            f"a(x)+b(y)=c",
            f"d(x)+e(y)=f",
        ]
        labels_text2 = [
            f"a(x)+b(y)+c(z)=d",
            f"e(x)+f(y)+g(z)=h",
            f"i(x)+j(y)+k(z)=l"
        ]
        for widget in self.root.winfo_children():
            widget.destroy()
        numunknowns = self.numunknowns.get()
        self.coefficients = []
        self.vector = []
        self.solutions = []
        for i in range(numunknowns):
            rows = []
            if numunknowns == 2:
                label = Label(self.root, text=labels_text[i], justify="center")
            else:
                label = Label(self.root, text=labels_text2[i], justify="center")
            label.grid(row=3 + i, column=0, columnspan=4)
            label.config(font=("Courier New", 12))
            for j in range(numunknowns):
                label = Label(self.root, text=f"{self.alphabet[self.alphabetindex]}=")
                self.alphabetindex += 1
                label.grid(row=i, column=j * 2, padx=5, pady=5)
                entry = Entry(self.root, width=5)
                entry.grid(row=i, column=j * 2 + 1, padx=5, pady=5)
                rows.append(entry)

            label = Label(self.root, text=f"{self.unknowns[i]}:")
            label.grid(row=numunknowns + 3, column=2*i)
            entry = Entry(self.root, width=5)
            entry.grid(row=numunknowns + 3, column=2*i + 1)
            self.solutions.append(entry)

            self.coefficients.append(rows)

            label = Label(self.root, text=f"{self.alphabet[self.alphabetindex]}=")
            self.alphabetindex += 1
            label.grid(row=i, column=numunknowns * 2 + 1, padx=5, pady=5)
            entry = Entry(self.root, width=5)
            entry.grid(row=i, column=numunknowns * 2 + 2, padx=5, pady=5)
            self.vector.append(entry)

        separator = ttk.Separator(self.root, orient="vertical")
        separator.grid(row=0, column=numunknowns * 2, rowspan=numunknowns, sticky='ns', padx=5)
        self.alphabetindex = 0

        solvebutton = Button(self.root, text="Solve", command=self.solve, relief=RAISED)
        solvebutton.grid(row=numunknowns + 1, column=numunknowns + 3)
        solvebutton.config(font=("Courier New", 12))


if __name__ == "__main__":
    root = Tk()
    app = SimultaneousSolverApp(root)
    root.mainloop()
