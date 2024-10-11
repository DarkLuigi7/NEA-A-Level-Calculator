from tkinter import *
import time
from fractions import Fraction
import re
# noinspection PyUnresolvedReferences
import math


# import required libraries


class BasicCalculator:
    def __init__(self, root):  # pass root as a parameter
        basicCalculatorWindow = Toplevel(root)
        basicCalculatorWindow.configure(bg="black")
        # create the basic calculator window as a toplevel window on top of the root window
        basicCalculatorWindow.title("Basic Calculator")
        # title the window
        basicCalculatorWindow.geometry("290x420")
        # give the window its dimensions
        self.justcalculated = False

        resultbox = Entry(basicCalculatorWindow, borderwidth=5, relief=SUNKEN)
        # create the entry / result box to display calculations
        resultbox.grid(row=0, column=0, columnspan=6, pady=5)
        # place the entry box on the window
        resultbox.config(font=("Arial", 18))
        resultbox.focus_set()
        # the focus_set method allows you to type into the box without having to click on it first
        self.resultbox = resultbox
        # make the result box an attribute, this allows for us to read, and write to the box in other functions
        self.answers = []
        # create an empty array to store previous answers
        self.answers_index = -1
        self.ANS = 0

        # the following buttons are the number and symbol keys of the keyboard, they all function the same

        button1 = Button(basicCalculatorWindow, text="1", width=3, command=lambda: self.ins("1"), relief=RAISED)
        # the command calls on the insert function of the class to insert the number 1 into the text box
        button1.grid(row=8, column=0, padx=3, pady=3)
        # place the button in the correct position
        button1.config(font=("Courier New", 18))

        button2 = Button(basicCalculatorWindow, text="2", width=3, command=lambda: self.ins("2"), relief=RAISED)
        button2.grid(row=8, column=1, padx=3, pady=3)
        button2.config(font=("Courier New", 18))

        button3 = Button(basicCalculatorWindow, text="3", width=3, command=lambda: self.ins("3"), relief=RAISED)
        button3.grid(row=8, column=2, padx=3, pady=3)
        button3.config(font=("Courier New", 18))

        button4 = Button(basicCalculatorWindow, text="4", width=3, command=lambda: self.ins("4"), relief=RAISED)
        button4.grid(row=7, column=0, padx=3, pady=3)
        button4.config(font=("Courier New", 18))

        button5 = Button(basicCalculatorWindow, text="5", width=3, command=lambda: self.ins("5"), relief=RAISED)
        button5.grid(row=7, column=1, padx=3, pady=3)
        button5.config(font=("Courier New", 18))

        button6 = Button(basicCalculatorWindow, text="6", width=3, command=lambda: self.ins("6"), relief=RAISED)
        button6.grid(row=7, column=2, padx=3, pady=3)
        button6.config(font=("Courier New", 18))

        button7 = Button(basicCalculatorWindow, text="7", width=3, command=lambda: self.ins("7"), relief=RAISED)
        button7.grid(row=6, column=0, padx=3, pady=3)
        button7.config(font=("Courier New", 18))

        button8 = Button(basicCalculatorWindow, text="8", width=3, command=lambda: self.ins("8"), relief=RAISED)
        button8.grid(row=6, column=1, padx=3, pady=3)
        button8.config(font=("Courier New", 18))

        button9 = Button(basicCalculatorWindow, text="9", width=3, command=lambda: self.ins("9"), relief=RAISED)
        button9.grid(row=6, column=2, padx=3, pady=3)
        button9.config(font=("Courier New", 18))

        button0 = Button(basicCalculatorWindow, text="0", width=3, command=lambda: self.ins("0"), relief=RAISED)
        button0.grid(row=9, column=0, padx=3, pady=3)
        button0.config(font=("Courier New", 18))

        buttondot = Button(basicCalculatorWindow, text=".", width=3, command=lambda: self.ins("."), relief=RAISED)
        buttondot.grid(row=9, column=1, padx=3, pady=3)
        buttondot.config(font=("Courier New", 18))

        buttonadd = Button(basicCalculatorWindow, text="+", width=3, command=lambda: self.ins("+"), relief=RAISED)
        buttonadd.grid(row=8, column=3, padx=3, pady=3)
        buttonadd.config(font=("Courier New", 18))

        buttonmult = Button(basicCalculatorWindow, text="*", width=3, command=lambda: self.ins("*"), relief=RAISED)
        buttonmult.grid(row=7, column=3, padx=3, pady=3)
        buttonmult.config(font=("Courier New", 18))

        buttonsub = Button(basicCalculatorWindow, text="-", width=3, command=lambda: self.ins("-"), relief=RAISED)
        buttonsub.grid(row=8, column=4, padx=3, pady=3)
        buttonsub.config(font=("Courier New", 18))

        buttondiv = Button(basicCalculatorWindow, text="/", width=3, command=lambda: self.ins("/"), relief=RAISED)
        buttondiv.grid(row=7, column=4, padx=3, pady=3)
        buttondiv.config(font=("Courier New", 18))

        buttonopenbr = Button(basicCalculatorWindow, text="(", width=3, bg="black", fg="white",
                              command=lambda: self.ins("("), relief=RAISED)
        buttonopenbr.grid(row=5, column=1, padx=3, pady=3)
        buttonopenbr.config(font=("Courier New", 18))

        buttonclosebr = Button(basicCalculatorWindow, text=")", width=3, bg="black", fg="white",
                               command=lambda: self.ins(")"), relief=RAISED)
        buttonclosebr.grid(row=5, column=2, padx=3, pady=3)
        buttonclosebr.config(font=("Courier New", 18))

        buttonexe = Button(basicCalculatorWindow, text="EXE", width=3, fg="royalblue3",
                           command=lambda: self.calculate(), relief=RAISED)
        # this command calls on the calculate function to calculate the contents of the result box
        buttonexe.grid(row=9, column=4, padx=3, pady=3)
        buttonexe.config(font=("Courier New", 18))

        buttonclear = Button(basicCalculatorWindow, text="AC", width=3, bg="royalblue3", command=lambda: self.clear(),
                             relief=RAISED)
        # this command calls on the clear function to clear the result box
        buttonclear.grid(row=6, column=4, padx=3, pady=3)
        buttonclear.config(font=("Courier New", 18))

        buttondelete = Button(basicCalculatorWindow, text="DEL", width=3, bg="royalblue3",
                              command=lambda: self.delete(), relief=RAISED)
        # this command calls on the delete function to remove one character from the result box
        buttondelete.grid(row=6, column=3, padx=3, pady=3)
        buttondelete.config(font=("Courier New", 18))

        buttondown = Button(basicCalculatorWindow, text="↓", width=3, bg="ivory4", command=None, relief=RAISED)
        buttondown.grid(row=3, column=1, padx=3, pady=3)
        buttondown.config(font=("Courier New", 18))

        buttonup = Button(basicCalculatorWindow, text="↑", width=3, bg="ivory4", command=None, relief=RAISED)
        buttonup.grid(row=2, column=1, padx=3, pady=3)
        buttonup.config(font=("Courier New", 18))

        buttonleft = Button(basicCalculatorWindow, text="←", width=3, bg="ivory4", command=None, relief=RAISED)
        buttonleft.grid(row=3, column=0, padx=3, pady=3)
        buttonleft.config(font=("Courier New", 18))

        buttonright = Button(basicCalculatorWindow, text="→", width=3, bg="ivory4", command=None, relief=RAISED)
        buttonright.grid(row=3, column=2, padx=3, pady=3)
        buttonright.config(font=("Courier New", 18))

        buttonform = Button(basicCalculatorWindow, text="S⇔D", width=3, height=1, bg="black", fg="white", padx=6,
                            pady=6, command=lambda: self.form(), relief=RAISED)
        buttonform.grid(row=5, column=0, padx=3, pady=3)
        buttonform.config(font=("Courier New", 13))

        buttonsquared = Button(basicCalculatorWindow, text="^2", width=3, bg="black", fg="white",
                               command=lambda: self.ins("^2"), relief=RAISED)
        buttonsquared.grid(row=5, column=3, padx=3, pady=3)
        buttonsquared.config(font=("Courier New", 18))

        buttonexponent = Button(basicCalculatorWindow, text="^", width=3, bg="black", fg="white",
                                command=lambda: self.ins("^"), relief=RAISED)
        buttonexponent.grid(row=5, column=4, padx=3, pady=3)
        buttonexponent.config(font=("Courier New", 18))

        buttonans = Button(basicCalculatorWindow, text="ANS", width=3, command=lambda: self.ins("ANS"), relief=RAISED)
        buttonans.grid(row=9, column=3, padx=3, pady=3)
        buttonans.config(font=("Courier New", 18))

        buttonpi = Button(basicCalculatorWindow, text="π", width=3, command=lambda: self.ins("π"), relief=RAISED)
        buttonpi.grid(row=9, column=2, padx=3, pady=3)
        buttonpi.config(font=("Courier New", 18))

    def delete(self):
        # this is the command to remove one character from the result box
        self.justcalculated = False
        # set justcalculated to false, so when pressing any other button, do not insert ANS before it
        x = self.resultbox.get()
        self.resultbox.delete(0, "end")
        y = x[:-1]
        # remvoe everything from the result box and replace it with what it was previously minus one character
        self.resultbox.insert(0, y)

    def clear(self):
        # this is the command to clear the result box, either called manually by the user, or done before inserting
        # the answer
        self.resultbox.delete(0, "end")
        # set just calculated to false so ANS does not appear
        self.justcalculated = False

    def ins(self, val):
        # inserts the "val" parameter into the end of the result box, this is used when pressing any button,
        # and when receiving a result
        if self.justcalculated and val in ["+", "-", "*", "/"]:
            # checks if ANS would be appropriate to insert
            self.clear()
            self.resultbox.insert(END, "ANS")
        self.resultbox.insert(END, val)
        # self.answers[-1] + val

    def up(self):
        pass

    def form(self):
        result = self.resultbox.get()
        if result == "3.141592653589793":
            self.clear()
            self.ins("π")
        elif "/" not in result and "π" not in result:
            try:
                self.clear()
                ratio = Fraction(result).limit_denominator()
                self.ins(str(ratio))
            except:
                pass
        else:
            self.calculate()

    def clear_and_insert(self, result):
        self.clear()
        self.ins(result)

    def error(self, result):
        self.clear()
        self.ins("Error")
        self.resultbox.after(1000, lambda: self.clear_and_insert(result))

    def calculate(self):
        initialresult = self.resultbox.get()
        try:
            result = initialresult
            result = re.sub(r'(\d|π|ANS)(\()', r'\1*(', result)
            result = re.sub(r'(\))(\d|π|ANS)', r')*\2', result)
            result = re.sub(r'(π|ANS)(\d)', r'\1*\2', result)
            result = re.sub(r'(\d)(π|ANS)', r'\1*\2', result)
            result = re.sub(r'(π|ANS)(ANS|π)', r'\1*\2', result)
            result = re.sub(r'(\))\s*(\()', r')*(', result)
            result = result.replace("ANS", "self.ANS")
            result = result.replace("π", "math.pi")
            result = result.replace("^", "**")
            answer = eval(result)
            # evaluate the string in the result box
            if answer.is_integer():
                answer = int(answer)
                # makes the numbers integers if possible, for example without this, if I did the calculation "1/1",
                # I would have gotten 1.0. it is generally cleaner and more appealing to look at the result as a whole
                # number if it is possible
            self.clear()
            # clear the result box
            self.ins(answer)
            # insert the answer into the result box
            self.justcalculated = True
            # set justcalculated to be true so ANS can be used for the next calculation
            self.ANS = answer
            # set self.ANS to the previous answer
            # self.answers = self.answers[:-1]
            # self.answers.append(answer)
            # self.answers.append("")

        except:
            self.error(initialresult)
