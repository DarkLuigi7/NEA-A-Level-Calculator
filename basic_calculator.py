# noinspection PyUnresolvedReferences
import math
import re
from fractions import Fraction
from tkinter import *
import sympy
import math

# import required libraries

class BasicCalculator:
    def __init__(self, root):  # pass root as a parameter
        self.root = root
        self.basicCalculatorWindow = Toplevel(root)
        self.basicCalculatorWindow.configure(bg="black")
        # create the basic calculator window as a toplevel window on top of the root window
        self.basicCalculatorWindow.title("Basic Calculator")
        # title the window
        self.basicCalculatorWindow.geometry("320x555")
        # give the window its dimensions
        self.justcalculated = False

        resultbox = Entry(self.basicCalculatorWindow, borderwidth=5, relief=SUNKEN)
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
        self.shift = False
        self.drawbuttons()
        # the following buttons are the number and symbol keys of the keyboard, they all function the same
        # they work by using the ins() function to insert a certain character or string into the result box

    def createbutton(self, name, text, width, x, y, padx, pady, fontsize, command, commandparameters, bg, fg, shiftname,
                     shiftcommand, shiftparameters):
        root = self.basicCalculatorWindow
        if self.shift:
            name = shiftname if shiftname is not None else name
            text = shiftname if shiftname is not None else text
            command = shiftcommand if shiftcommand is not None else command
            commandparameters = shiftparameters if shiftparameters is not None else commandparameters
        if commandparameters is not None:
            button_command = lambda: command(commandparameters)
        else:
            button_command = command
        button = Button(root, text=text, width=width, bg=bg, fg=fg,
                             command=button_command, relief=RAISED)
        button.grid(row=y, column=x, padx=padx, pady=pady)
        button.config(font=("Courier New", fontsize))



    def drawbuttons(self):
        self.createbutton("one", "1", 3, 0, 8, 5, 5, 18, self.ins, "1", None, None, None,
                          None, None)
        self.createbutton("two", "2", 3, 1, 8, 5, 5, 18, self.ins, "2", None, None, None,
                          None, None)
        self.createbutton("three", "3", 3, 2, 8, 5, 5, 18, self.ins, "3", None, None, None,
                          None, None)
        self.createbutton("four", "4", 3, 0, 7, 5, 5, 18, self.ins, "4", None, None, None,
                          None, None)
        self.createbutton("five", "5", 3, 1, 7, 5, 5, 18, self.ins, "5", None, None, None,
                          None, None)
        self.createbutton("six", "6", 3, 2, 7, 5, 5, 18, self.ins, "6", None, None, None,
                          None, None)
        self.createbutton("seven", "7", 3, 0, 6, 5, 5, 18, self.ins, "7", None, None, None,
                          None, None)
        self.createbutton("eight", "8", 3, 1, 6, 5, 5, 18, self.ins, "8", None, None, None,
                          None, None)
        self.createbutton("nine", "9", 3, 2, 6, 5, 5, 18, self.ins, "9", None, None, None,
                          None, None)
        self.createbutton("zero", "0", 3, 0, 9, 5, 5, 18, self.ins, "0", None, None, None,
                          None, None)
        self.createbutton("dot", ".", 3, 1, 9, 5, 5, 18, self.ins, ".", None, None, None,
                          None, None)
        self.createbutton("add", "+", 3, 4, 8, 5, 5, 18, self.ins, "+", None, None, None,
                          None, None)
        self.createbutton("multiply", "*", 3, 3, 7, 5, 5, 18, self.ins, "*", None, None,
                          None, None, None)
        self.createbutton("subtract", "-", 3, 3, 8, 5, 5, 18, self.ins, "-", None, None,
                          None, None, None)
        self.createbutton("divide", "/", 3, 4, 7, 5, 5, 18, self.ins, "/", None, None, None,
                          None, None)
        self.createbutton("subtract", "-", 3, 3, 8, 5, 5, 18, self.ins, "-", None, None,
                          None, None, None)
        self.createbutton("open bracket", "(", 3, 1, 5, 5, 5, 18, self.ins, "(", "black",
                          "white", None, None, None)
        self.createbutton("close bracket", ")", 3, 2, 5, 5, 5, 18, self.ins, ")", "black",
                          "white", None, None, None)
        self.createbutton("button squared", "^2", 3, 3, 5, 5, 5, 18, self.ins, "^2",
                          "black", "white", None, None, None)
        self.createbutton("exponent", "^x", 3, 4, 5, 5, 5, 18, self.ins, "^", "black",
                          "white", None, None, None)
        self.createbutton("sin", "sin", 5, 0, 4, 5, 3, 10, self.ins, "sin(", "black",
                          "white", "arcsin", self.ins, "arcsin(")
        self.createbutton("cos", "cos", 5, 1, 4, 5, 3, 10, self.ins, "cos(", "black",
                          "white", "arccos", self.ins, "arccos(")
        self.createbutton("tan", "tan", 5, 2, 4, 5, 3, 10, self.ins, "tan(", "black",
                          "white", "arctan", self.ins, "arctan(")
        self.createbutton("ANS", "ANS", 3, 3, 9, 5, 5, 18, self.ins, "ANS", None, None,
                          None, None, None)
        self.createbutton("pi", "π", 3, 2, 9, 5, 5, 18, self.ins, "π", None, None, None,
                          None, None)
        self.createbutton("execute", "EXE", 3, 4, 9, 5, 5, 18, self.calculate, None, None,
                          None, None, None, None)
        self.createbutton("clear", "AC", 3, 4, 6, 5, 5, 18, self.clear, None, "royalblue3",
                          None, None, None, None)
        self.createbutton("delete", "DEL", 3, 3, 6, 5, 5, 18, self.delete, None,
                          "royalblue3", None, None, None, None)
        self.createbutton("down", "↓", 3, 1, 2, 5, 5, 18, None, None, "ivory4", None, None,
                          None, None)
        self.createbutton("up", "↑", 3, 1, 1, 5, 5, 18, None, None, "ivory4", None, None,
                          None, None)
        self.createbutton("left", "←", 3, 0, 2, 5, 5, 18, self.move, -1, "ivory4", None,
                          None, None, None)
        self.createbutton("left", "→", 3, 2, 2, 5, 5, 18, self.move, 1, "ivory4", None,
                          None, None, None)
        self.createbutton("form", "S⇔D", 3, 0, 5, 5, 5, 18, self.form, None, "black",
                          "white", None, None, None)
        self.createbutton("shift", "⇧", 3, 0, 3, 5, 5, 18, self.toggleshift, None, "black",
                          "gold", None, None, None)

    def delete(self):
        # this command deletes the last item in the result box before the cursor
        self.justcalculated = False
        # sets justcalculated to false, so when you insert other strings, ANS does not appear
        pos = self.resultbox.index(INSERT)
        if pos > 0:
            self.resultbox.delete(pos - 1)
            # given that the cursor position is greater than 0, delete the last thing before it

    def toggleshift(self):
        self.shift = not self.shift
        self.drawbuttons()

    def clear(self):
        # this is the command to clear the result box, either called manually by the user, or done before inserting
        # the answer
        self.resultbox.delete(0, "end")
        # set just calculated to false so ANS does not appear
        self.justcalculated = False

    def ins(self, val):
        # inserts the "val" parameter into the end of the result box, this is used when pressing any button,
        # and when receiving a result
        if self.justcalculated:
            if val in ["+", "-", "*", "/"]:
                # checks if ANS would be appropriate to insert
                self.clear()
                self.resultbox.insert(END, "ANS")
            else:
                self.clear()
            self.justcalculated = False
        self.resultbox.insert(END, val)

    def up(self):
        pass

    def form(self):
        result = self.resultbox.get()
        if result == "3.141592653589793":
            # if the result is the decimal approximation of pi, replace it with the symbol "π"
            self.clear_and_insert("π")
        elif "/" not in result and "π" not in result:
            # given that the result is not already represented as a fraction, or is pi, attempt to do so
            try:
                ratio = Fraction(result).limit_denominator()
                # use the fraction module to represent the result as a ratio
                self.clear_and_insert(str(ratio))
            except:
                pass
                # if any errors are encountered, simply ignore them and continue
        else:
            self.calculate()

    def clear_and_insert(self, result):
        self.clear()
        self.ins(result)
        # a function to reduce the number of lines needed to clear the answer box and immediately insert into it

    def error(self, result):
        self.clear_and_insert("Error")
        self.resultbox.after(1000, lambda: self.clear_and_insert(result))
        # clears the "Error" message after 1000ms, using the after method in tkinter

    def move(self, value):
        position = self.resultbox.index(INSERT) + value
        self.resultbox.icursor(position)

    def calculate(self):
        initialresult = self.resultbox.get()
        try:
            result = initialresult
            result = result.replace("arcsin(", "__TEMP_ARCSIN__")
            result = result.replace("sin(", "math.sin(")
            result = result.replace("__TEMP_ARCSIN__", "sympy.asin(")
            print(result)
            result = result.replace("arccos(", "__TEMP_ARCCOS__")
            result = result.replace("cos(", "math.cos(")
            result = result.replace("__TEMP_ARCCOS__", "sympy.acos(")
            print(result)
            result = result.replace("arccos(", "__TEMP_ARCTAN__")
            result = result.replace("tan(", "math.tan(")
            result = result.replace("__TEMP_ARCTAN__", "sympy.atan(")
            print(result)
            result = re.sub(r'(\d|π|ANS)(\()', r'\1*(', result)
            print(result)
            result = re.sub(r'(\))(\d|π|ANS)', r')*\2', result)
            print(result)
            result = re.sub(r'(π|ANS)(\d)', r'\1*\2', result)
            print(result)
            result = re.sub(r'(\d)(π|ANS)', r'\1*\2', result)
            print(result)
            result = re.sub(r'(π|ANS)(ANS|π)', r'\1*\2', result)
            print(result)
            result = re.sub(r'(\))\s*(\()', r')*(', result)
            print(result)
            result = result.replace("ANS", "self.ANS")
            print(result)
            result = result.replace("π", "math.pi")
            print(result)
            result = result.replace("^", "**")
            print(result)
            answer = eval(result)
            print(answer)
            print(type(answer))
            # evaluate the string in the result box
            if "sympy" in str(type(answer)):
                if not "sympy.core.mul.Mul" == str(type(answer)):
                     float(answer)
            else:
                if abs(answer) < 1e-10:
                    answer = 0
                if answer.is_integer():
                    print(type(answer))
                    answer = int(answer)
                    # makes the numbers integers if possible, for example without this, if I did the calculation "1/1",
                    # I would have gotten 1.0. it is generally cleaner and more appealing to look at the result as a whole
                    # number if it is possible
                    print(answer)
            answer = str(answer)
            answer = answer.replace("pi", "π")
            self.clear_and_insert(answer)
            # clear the result box and insert the answer into the result box
            self.justcalculated = True
            # set justcalculated to be true so ANS can be used for the next calculation
            self.ANS = answer
            # set self.ANS to the previous answer
            # self.answers = self.answers[:-1]
            # self.answers.append(answer)
            # self.answers.append("")

        except:
            self.error(initialresult)
