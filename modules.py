from tkinter import *

root = Tk()

class BasicCalculator:
    def __init__(self):
        basicCalculatorWindow = Toplevel(root)
        basicCalculatorWindow.title("Basic Calculator")
        basicCalculatorWindow.geometry("290x260")
        
        resultwindow = Entry(basicCalculatorWindow, borderwidth=5, relief=SUNKEN)
        resultwindow.grid(row=0, column=0, columnspan=6, pady=5)
        resultwindow.config(font=("Arial", 18))
        resultwindow.focus_set()
        self.resultwindow = resultwindow

        button1 = Button(basicCalculatorWindow, text="1", width=3, command=lambda:self.ins("1"),relief=RAISED)
        button1.grid(row=3, column=0, padx=3, pady=3)
        button1.config(font=(("Courier New", 18)))

        button2 = Button(basicCalculatorWindow, text="2", width=3, command=lambda:self.ins("2"),relief=RAISED)
        button2.grid(row=3, column=1, padx=3, pady=3)
        button2.config(font=(("Courier New", 18)))

        button3 = Button(basicCalculatorWindow, text="3", width=3, command=lambda:self.ins("3"),relief=RAISED)
        button3.grid(row=3, column=2, padx=3, pady=3)
        button3.config(font=(("Courier New", 18)))

        button4 = Button(basicCalculatorWindow, text="4", width=3, command=lambda:self.ins("4"),relief=RAISED)
        button4.grid(row=2, column=0, padx=3, pady=3)
        button4.config(font=(("Courier New", 18)))

        button5 = Button(basicCalculatorWindow, text="5", width=3, command=lambda:self.ins("5"),relief=RAISED)
        button5.grid(row=2, column=1, padx=3, pady=3)
        button5.config(font=(("Courier New", 18)))
        
        button6 = Button(basicCalculatorWindow, text="6", width=3, command=lambda:self.ins("6"),relief=RAISED)
        button6.grid(row=2, column=2, padx=3, pady=3)
        button6.config(font=(("Courier New", 18)))

        button7 = Button(basicCalculatorWindow, text="7", width=3, command=lambda:self.ins("7"),relief=RAISED)
        button7.grid(row=1, column=0, padx=3, pady=3)
        button7.config(font=(("Courier New", 18)))

        button8 = Button(basicCalculatorWindow, text="8", width=3, command=lambda:self.ins("8"),relief=RAISED)
        button8.grid(row=1, column=1, padx=3, pady=3)
        button8.config(font=(("Courier New", 18)))

        button9 = Button(basicCalculatorWindow, text="9", width=3, command=lambda:self.ins("9"),relief=RAISED)
        button9.grid(row=1, column=2, padx=3, pady=3)
        button9.config(font=(("Courier New", 18)))

        button0 = Button(basicCalculatorWindow, text="0", width=3, command=lambda:self.ins("0"),relief=RAISED)
        button0.grid(row=4, column=0, padx=3, pady=3)
        button0.config(font=(("Courier New", 18)))

        buttondot = Button(basicCalculatorWindow, text=".", width=3, command=lambda:self.ins("."),relief=RAISED)
        buttondot.grid(row=4, column=1, padx=3, pady=3)
        buttondot.config(font=(("Courier New", 18)))

        buttonexe = Button(basicCalculatorWindow, text="EXE", width=3, command=lambda:self.calculate(),relief=RAISED)
        buttonexe.grid(row=4, column=3, padx=3, pady=3)
        buttonexe.config(font=(("Courier New", 18)))

        buttonadd = Button(basicCalculatorWindow, text="+", width=3, command=lambda:self.ins("+"),relief=RAISED)
        buttonadd.grid(row=3, column=3, padx=3, pady=3)
        buttonadd.config(font=(("Courier New", 18)))

                     
    def ins(self, val):
        self.resultwindow.insert(END, val)

    def calculate(self):
        result = self.resultwindow.get()
        answer = eval(result)
        self.resultwindow.delete(0, "end")
        self.resultwindow.insert(0, answer)
        

    

class MainMenu:
    def __init__(self):
        root.title("Main Menu")
        root.geometry("400x400")
        
        basic_button_photo = PhotoImage(file="basic_operators.png")
        basic_button = Button(root, text="Basic", image=basic_button_photo, command = BasicCalculator)
        basic_button.place(x=50, y=50)

        equation_button_photo = PhotoImage(file="quadractic.png")
        equation_button = Button(root, text="Equation Solver", image=equation_button_photo)
        equation_button.place(x=250, y=50)
        
        
        root.mainloop()
       
        
def start():
    MainMenu()

        
start()
    
