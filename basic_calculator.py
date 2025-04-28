import math
import re
from fractions import Fraction
from tkinter import *
import sympy
import math
import traceback


# import required libraries

class BasicCalculator:
    def __init__(self, root):
        self.basicCalculatorWindow = Toplevel(root)
        self.basicCalculatorWindow.configure(bg="black")
        self.basicCalculatorWindow.title("Basic Calculator")
        self.basicCalculatorWindow.geometry("320x555")
        # create a class passing root variable in initialise function to create a toplevel window of the main menu
        # window, name "Basic Calculator", background colour black and window size 320 by 555
        self.just_calculated = False
        # create and set the just_calculated attribute to False
        # this attribute is used later on to allow for the ANS
        # variable to be automatically inputted in certain situations
        self.variable_dictionary = {"x": "0", "y": "0", "z": "0"}
        # create a dictionary to store the values of the user-defined variables

        resultbox = Entry(self.basicCalculatorWindow, borderwidth=5, relief=SUNKEN)
        # create the entry / result box to display calculations
        resultbox.grid(row=0, column=0, columnspan=6, pady=5)
        # place the entry box at the top of the window
        resultbox.config(font=("Arial", 18))
        resultbox.focus_set()
        # the focus_set allows you to type into the box before
        self.resultbox = resultbox
        # make the result box an attribute, this allows for us to read, and write to the box in other functions
        self.answers = []
        # create an empty array to store previous answers
        self.max_answers_index = -1
        # initialise the answer maximum index attribute and set it to -1 to show that there are no answers currently
        # stored in the index. since index position 0 is the first, when an answer is added to the list,
        # this attribute will update to reflect the index position of the last item in the array
        self.answers_index = -1
        # initialise the answer index attribute and set it to -1 to indicate our current position in the array

        self.ANS = 0
        # set the initial value of the ANS variable to 0
        self.shift = False
        # initialise the shift attribute and set it to False while first drawing the buttons
        self.draw_buttons()
        # call on the draw_buttons method to draw the buttons as the last step of initialising the calculator

    def create_button(self, name, text, width, x, y, pad_x, pad_y, font_size, command, command_parameters, bg, fg,
                      shift_name,
                      shift_command, shift_parameters):
        # since creating so many buttons would have become monotonous, I created a class to shorten the process
        root = self.basicCalculatorWindow
        if self.shift:
            # if the shift button has been pressed, draw the button with its shift_name and shift_command
            name = shift_name if shift_name is not None else name
            text = shift_name if shift_name is not None else text
            command = shift_command if shift_command is not None else command
            command_parameters = shift_parameters if shift_parameters is not None else command_parameters
        if command_parameters is not None:
            button_command = lambda: command(command_parameters)
            # this is necessary in cases where a parameter must
            # be passed with the button's command, for example
            # if the button's purpose is to insert a character,
            # pass the character as a parameter of the button's command
        else:
            button_command = command
            # otherwise, simply pass the command as a function with no parameters
        button = Button(root, text=text, width=width, bg=bg, fg=fg,
                        command=button_command, relief=RAISED)
        # create the button as a tkinter button object with the chosen parameters
        button.grid(row=y, column=x, padx=pad_x, pady=pad_y)
        # place the button on the grid given the x and y values
        button.config(font=("Courier New", font_size))
        # change the font size given the font_size parameter

    def draw_buttons(self):
        self.create_button("one", "1", 3, 0, 8, 5, 5, 18, self.ins, "1", None, None, None,
                           None, None)
        self.create_button("two", "2", 3, 1, 8, 5, 5, 18, self.ins, "2", None, None, None,
                           None, None)
        self.create_button("three", "3", 3, 2, 8, 5, 5, 18, self.ins, "3", None, None, None,
                           None, None)
        self.create_button("four", "4", 3, 0, 7, 5, 5, 18, self.ins, "4", None, None, None,
                           None, None)
        self.create_button("five", "5", 3, 1, 7, 5, 5, 18, self.ins, "5", None, None, None,
                           None, None)
        self.create_button("six", "6", 3, 2, 7, 5, 5, 18, self.ins, "6", None, None, None,
                           None, None)
        self.create_button("seven", "7", 3, 0, 6, 5, 5, 18, self.ins, "7", None, None, None,
                           None, None)
        self.create_button("eight", "8", 3, 1, 6, 5, 5, 18, self.ins, "8", None, None, None,
                           None, None)
        self.create_button("nine", "9", 3, 2, 6, 5, 5, 18, self.ins, "9", None, None, None,
                           None, None)
        self.create_button("zero", "0", 3, 0, 9, 5, 5, 18, self.ins, "0", None, None, None,
                           None, None)
        self.create_button("dot", ".", 3, 1, 9, 5, 5, 18, self.ins, ".", None, None, None,
                           None, None)
        self.create_button("add", "+", 3, 4, 8, 5, 5, 18, self.ins, "+", None, None, None,
                           None, None)
        self.create_button("multiply", "*", 3, 3, 7, 5, 5, 18, self.ins, "*", None, None,
                           None, None, None)
        self.create_button("subtract", "-", 3, 3, 8, 5, 5, 18, self.ins, "-", None, None,
                           None, None, None)
        self.create_button("divide", "/", 3, 4, 7, 5, 5, 18, self.ins, "/", None, None, None,
                           None, None)
        self.create_button("subtract", "-", 3, 3, 8, 5, 5, 18, self.ins, "-", None, None,
                           None, None, None)
        self.create_button("open bracket", "(", 5, 1, 5, 5, 3, 10, self.ins, "(", "black",
                           "white", None, None, None)
        self.create_button("close bracket", ")", 5, 2, 5, 5, 3, 10, self.ins, ")", "black",
                           "white", None, None, None)
        self.create_button("button squared", "^2", 5, 3, 5, 5, 3, 10, self.ins, "^2",
                           "black", "white", None, None, None)
        self.create_button("exponent", "^x", 5, 4, 5, 5, 3, 10, self.ins, "^", "black",
                           "white", None, None, None)
        self.create_button("⇐", "⇐", 5, 4, 4, 5, 3, 10, self.ins, "⇐", "black",
                           "white", None, None, None)
        self.create_button("ANS", "ANS", 3, 3, 9, 5, 5, 18, self.ins, "ANS", None, None,
                           None, None, None)
        self.create_button("pi", "π", 3, 2, 9, 5, 5, 18, self.ins, "π", None, None, None,
                           None, None)
        self.create_button("x", "x", 3, 2, 3, 5, 5, 18, self.ins, "x", "black",
                           "red3", None, None, None)
        self.create_button("y", "y", 3, 3, 3, 5, 5, 18, self.ins, "y", "black",
                           "red3", None, None, None)
        self.create_button("z", "z", 3, 4, 3, 5, 5, 18, self.ins, "z", "black",
                           "red3", None, None, None)
        # the preceding buttons are simple, they all use the self.ins function to insert one character (or multiple
        # in the case of the squared button, for example). these characters if needed, will be changed into python
        # syntax when the calculate method is run
        self.create_button("sin", "sin", 5, 0, 4, 5, 3, 10, self.ins, "sin(", "black",
                           "white", "arcsin", self.ins, "arcsin(")
        self.create_button("cos", "cos", 5, 1, 4, 5, 3, 10, self.ins, "cos(", "black",
                           "white", "arccos", self.ins, "arccos(")
        self.create_button("tan", "tan", 5, 2, 4, 5, 3, 10, self.ins, "tan(", "black",
                           "white", "arctan", self.ins, "arctan(")
        self.create_button("e", "e", 5, 3, 4, 5, 3, 10, self.ins, "e", "black",
                           "white", "ln(", self.ins, "ln(")
        # the preceding buttons also use the self.ins function, however they all come with a shift function,
        # and a shift parameter, in the case of the trigonometric functions, for example, this means that pressing
        # the shift button turns them into the inverse trigonometric functions, as the shift parameter is different
        # from the regular one.
        self.create_button("execute", "EXE", 3, 4, 9, 5, 5, 18, self.execute, None, None,
                           None, None, None, None)
        # this button calls the execute function to complete the calculation in the result box
        self.create_button("clear", "AC", 3, 4, 6, 5, 5, 18, self.clear, None, "royalblue3",
                           None, None, None, None)
        # this button calls the clear function to clear the result box of any and all characters
        self.create_button("delete", "DEL", 3, 3, 6, 5, 5, 18, self.delete, None,
                           "royalblue3", None, None, None, None)
        # this button calls the delete method to delete the last item in the result box before the cursor
        self.create_button("down", "↓", 3, 1, 2, 5, 5, 18, self.down, None, "ivory4", None, None,
                           None, None)
        # this button calls the down method to replace the text in the result box with the next result stored in the
        # memory
        self.create_button("up", "↑", 3, 1, 1, 5, 5, 18, self.up, None, "ivory4", None, None,
                           None, None)
        # this button calls the up method to replace the text in the result box with the previous result stored in the
        # memory
        self.create_button("left", "←", 3, 0, 2, 5, 5, 18, self.move, -1, "ivory4", None,
                           None, None, None)
        # this button calls the left method to move the cursor one space to the left
        self.create_button("right", "→", 3, 2, 2, 5, 5, 18, self.move, 1, "ivory4", None,
                           None, None, None)
        # this button calls the right method to move the cursor one space to the right
        self.create_button("form", "S⇔D", 5, 0, 5, 5, 3, 10, self.form, None, "black",
                           "white", None, None, None)
        # this button calls the form method to change the form of the answer in the result box
        self.create_button("shift", "⇧", 3, 0, 3, 5, 5, 18, self.toggle_shift, None, "black",
                           "gold", None, None, None)
        # this button calls the toggle_shift method to enable pressing the shift buttons

    def delete(self):
        # this command deletes the last item in the result box before the cursor
        self.just_calculated = False
        # sets just_calculated to false, so when you insert other strings, ANS does not appear
        pos = self.resultbox.index(INSERT)
        if pos > 0:
            self.resultbox.delete(pos - 1)
            # given that the cursor position is greater than 0, delete the last thing before it

    def toggle_shift(self):
        self.shift = not self.shift
        # negate the current self.shift boolean value
        self.draw_buttons()
        # redraw the buttons so the buttons affected by the shift button change

    def clear(self):
        # this is the command to clear the result box, either called manually by the user, or done before inserting
        # the answer
        self.resultbox.delete(0, "end")
        self.just_calculated = False
        # set just calculated to false so ANS does not appear

    def ins(self, val):
        self.assignment_mode = False
        # inserts the "val" parameter into the end of the result box, this is used when pressing any button,
        # and when receiving a result
        if self.just_calculated:
            if val in ["+", "-", "*", "/"]:
                # checks if ANS would be appropriate to insert
                self.clear()
                self.resultbox.insert(END, "ANS")
                # if so, clear the answer box, and insert
            else:
                self.clear()
            self.just_calculated = False
        self.resultbox.insert(END, val)

    def up(self):
        if self.max_answers_index == -1 or self.answers_index == 0:
            pass
        else:
            self.answers_index -= 1
            self.clear_and_insert(self.answers[self.answers_index])
    def down(self):
        if self.max_answers_index == -1 or self.answers_index >= self.max_answers_index:
            pass
        else:
            self.answers_index += 1
            self.clear_and_insert(self.answers[self.answers_index])

    def form(self):
        result = self.resultbox.get()

        if result in {"π", "e"} or "/" in result:
            self.execute()
        try:
            if abs(float(result) - math.pi) < 1e-9:
                # if the result is the decimal approximation of pi, replace it with the symbol "π"
                self.clear_and_insert("π")
            elif abs(float(result) - math.e) < 1e-9:
                # if the result is the decimal approximation of e, replace it with the letter "e"#
                self.clear_and_insert("e")
            elif result not in {"π", "e"} or "/" not in result:
                # given that the result is not already represented as a fraction, or is pi, attempt to do so
                ratio = Fraction(result).limit_denominator()
                # use the fraction module to represent the result as a ratio
                self.clear_and_insert(str(ratio))
            else:
                self.execute()
        except ValueError:
            print("there was an error")
            pass
            # if any errors are encountered, simply ignore them and continue

    def clear_and_insert(self, result):
        self.clear()
        self.ins(result)
        # a function to reduce the number of lines needed to clear the answer box and immediately insert into it

    def error(self, result):
        self.clear_and_insert("Error")
        print("ERROR HERE")
        self.resultbox.after(1000, lambda: self.clear_and_insert(result))
        # clears the "Error" message after 1000ms, using the after method in tkinter

    def move(self, value):
        position = self.resultbox.index(INSERT) + value
        self.resultbox.icursor(position)

    def convert_to_sympy_expression(self, result):
        try:
            # try converting the string to a SymPy expression
            expr = sympy.sympify(result)
            return expr
        except (sympy.SympifyError, ValueError):
            # if sympify fails, check if it's a math function and convert it to a SymPy expression
            if "math." in result:
                # if a method of the math module
                result = result.replace("math.", "sympy.")
                # replace with sympy method
                try:
                    expr = sympy.sympify(result)
                    # try to evaluate the expression using sympy
                    return expr
                except sympy.SympifyError:
                    # if the above try statement fails, raise an error
                    raise ValueError("Failed to convert to a valid SymPy expression")
            else:
                raise ValueError("The input is neither a valid SymPy expression nor a math function")
                # if both converting it directly to a sympy expression and converting it from a math function to a
                # sympy expression fail, raise an error

    def calculate(self, initial_result):
        try:
            if "⇐" in initial_result:
                # first, try to check if there is a "⇐" in the
                parts = initial_result.split("⇐")
                # split the string initial_result between every "⇐"
                if len(parts) == 2:
                    # if there are two parts in this split (if there was only one "⇐")
                    var, value = parts[0].strip(), parts[1].strip()
                    # strip all leading spaces if there are any
                    if var in {"x", "y", "z"}:
                        # if the string var is any of the characters in the given set
                        self.variable_dictionary[var] = self.calculate(value)
                        # change the corresponding value of the variable in the variable_dictionary to the given value
                        self.clear_and_insert(var)
                        # clear the result box and re-insert the variable
                        return
                        # stop the method here
                    else:
                        self.error(initial_result)
                        # if the variable given is not x y or z call the error method with parameter initial_result
                        return

            result = initial_result
            # the following lines of code ensure that the inputted result is a valid mathematical python expression
            result = re.sub(r'(\d|π|ANS|e)(\()', r'\1*(', result)
            # this replaces implicit multiplication where a number or any of the collection of strings appears before
            # a bracket with explicit multiplication by adding a "*" eg; 2(3+4) will become 2*(3+4)
            result = re.sub(r'(\))(\d|π|ANS|e|ln|sin|cos|tan)', r')*\2', result)
            # this replaces implicit multiplication where a number or any of the collection of strings
            # π|ANS|e|ln|sin|cos|tan appears after a bracket with explicit multiplication by adding a "*"
            # eg; (7+2)ANS will become (7+2)*ANS
            result = re.sub(r'(π|ANS|e)(\d)', r'\1*\2', result)
            # this replaces implicit multiplication where a number or any of the collection of strings
            # π|ANS|e appears before a number with explicit multiplication by adding a "*" eg; π5 will become π*5
            result = re.sub(r'(\d)(π|ANS|e|ln|sin|cos|tan)', r'\1*\2', result)
            # this replaces implicit multiplication where a number or any of the collection of strings
            # π|ANS|e|ln|sin|cos|tan appears after a number with explicit multiplication by adding a "*"
            # eg; 3e will become 3*e
            result = re.sub(r'(π|ANS|e)(ANS|π|e|ln|sin|cos|tan)', r'\1*\2', result)
            # this replaces implicit multiplication where any of the collection of strings π|ANS|e appears before any
            # other string of the collection ANS|π|e|ln|sin|cos|tan with explicit multiplication by adding a "*"
            # eg; πsin(30) will become π*sin(30)
            result = re.sub(r'(\))\s*(\()', r')*(', result)
            # this replaces implicit multiplication where any closing bracket is directly to the left of an opening
            # bracket with explicit multiplication by adding a "*" eg; (3)(4) becomes (3)*(4)
            result = result.replace("arcsin(", "__TEMP_ARCSIN__")
            # I am using temporary strings here otherwise later on when I replace sin, I could result in something
            # that was originally arcsin( becoming sympy.asympy.sin(
            result = result.replace("arccos(", "__TEMP_ARCCOS__")
            result = result.replace("arctan(", "__TEMP_ARCTAN__")
            result = result.replace("sin(", "sympy.sin(")
            # replace any instance of sin( with a valid sympy expression for sin
            result = result.replace("__TEMP_ARCSIN__", "sympy.asin(")
            # replace any instance of __TEMP_ARCSIN__ with a valid sympy expression for arcsin
            result = result.replace("cos(", "sympy.cos(")
            # replace any instance of sin( with a valid sympy expression for cos
            result = result.replace("__TEMP_ARCCOS__", "sympy.acos(")
            # replace any instance of __TEMP_ARCCOS__ with a valid sympy expression for arccos
            result = result.replace("tan(", "sympy.tan(")
            # replace any instance of sin( with a valid sympy expression for tan
            result = result.replace("__TEMP_ARCTAN__", "sympy.atan(")
            # replace any instance of __TEMP_ARCTAN__ with a valid sympy expression for arctan
            result = result.replace("ln(", "math.log(")
            # replace any instance of ln( with a valid math expression for natural log
            result = result.replace("ANS", "self.ANS")
            # replace any instance of ANS with the object's attribute self.ANS
            result = result.replace("e", "math.e")
            # replace any instance of the letter e in the string with the math module attribute math.e
            result = result.replace("π", "math.pi")
            # replace any instance of π in the string with the math module attribute math.e
            result = result.replace("^", "**")
            # replace any instance of ^ in the string with the python exponent **
            for variable in self.variable_dictionary:
                # for each variable in the dictionary
                if self.variable_dictionary[variable] is not None:
                    # given that the variable has a corresponding value in the dictionary
                    result = result.replace(variable, self.variable_dictionary[variable])
                    # replace every instance (if any) of the variable in the result string with its corresponding value

            try:
                answer = eval(result)
                # try to evaluate the result using the python eval function
            except:
                self.error(result)
                # if this fails call the error method with the result parameter
                return
                # return to end the function

            if "sympy" in result:
                # if there is a sympy expression in the evaluated result use the sympy evaluate method to evaluate it
                answer = answer.evalf()

            if "sympy" in str(type(answer)):
                # if the sympy evaluated result gave another sympy expression
                if not "sympy.core.mul.Mul" == str(type(answer)):
                    # if the type of the answer isn't sympy.core.mul.Mul
                    answer = float(answer)
                    # convert the answer to a float, converting it from a sympy object to a python data type
                    if abs(answer - 0.5) < 1e-10:
                        answer = 0.5
                        # if the answer is cose to 0.5 with a tolerance of 10^-10 set the answer to 0.5
                    if answer.is_integer():
                        answer = int(answer)
                        # if the answer is a float that can be expressed as an integer
                        # set the answer to a python integer
            else:
                # if the sympy evaluated result evaluated to a python object or if there was no sympy expression in
                # the original result to begin with
                if abs(answer) < 1e-10:
                    answer = 0
                    # if the answer is smaller than 10^-10 simply set the answer equal to 0
                if answer.is_integer():
                    answer = int(answer)
                    # makes the numbers integers if possible, for example without this, if I did the calculation
                    # "1/1", I would have gotten 1.0. it is generally cleaner and more appealing to look at the
                    # result as a whole number if it is possible
            self.ANS = answer
            # set self.ANS to the previous answer
            answer = str(answer)
            # set the answer to the string of itself so it can
            answer = answer.replace("pi", "π")
            self.just_calculated = True
            # set just_calculated to be true so ANS can be used for the next calculation
            return answer

        except Exception as e:
            # if any part of the calculate method fails
            self.error(initial_result)
            # call the error method with parameter initial_result
            traceback.print_exc()
            # print the most recent exception traceback to the console

    def execute(self):
        # this method is called when the execute button is pressed
        initial_result = self.resultbox.get()
        # initialise the initial_result variable and set it to the contents of the resultbox
        answer = self.calculate(initial_result)
        # call the calculate method with parameter initial_result, and set the variable to the returned value
        self.answers.append(answer)
        # append this answer to the self.answers array so the user can use the arrow buttons to navigate through
        # previous answers
        self.max_answers_index += 1
        # increment the self.max_answers_index by 1 for use in making sure if the user presses the down arrow when
        # already at the end of the self.answers array, no errors are raised
        self.answers_index = self.max_answers_index
        # if the user has inputted a new answer by pressing the execute button, change their position in the
        # self.answer array to the maximum value (the last answer inputted)

        self.clear_and_insert(answer)
        # finally, clear the answer box and insert the answer gotten from the calculate method
