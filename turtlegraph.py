import turtle
import numpy as np
import math


# import required libraries

class Plotter:
    # Create a class Plotter to create objects being instances of a turtle window that will draw the functions
    def __init__(self, equations, x_min, x_max, y_min, y_max):
        # pass as parameters list containing the equations to be drawn, as well as the maximum and minimum x and y
        # values for the bounds of the graph
        self.equations = equations
        self.X_MIN, self.X_MAX = x_min, x_max
        self.Y_MIN, self.Y_MAX = y_min, y_max
        # use these parameters to create object attributes

        turtle.setup(width=500, height=500)
        turtle.screensize(400, 400)
        # set up a window of 500 by 500 pixels in real size, and inner drawing dimensions 400 by 400 pixels

        self.screen = turtle.Screen()
        window_width = self.screen.window_width()
        window_height = self.screen.window_height()
        # get the screen object as an attribute and use it to get the window width and height in order to find scale
        self.SCALE = min(window_width, window_height) / max(abs(self.X_MAX - self.X_MIN), abs(self.Y_MAX - self.Y_MIN))
        # create object attribute scale to represent the relationship between a unit in the coordinate system and the
        # number of pixels in the window it is represented by

        self.t = turtle.Turtle()
        # create a turtle object as an object attribute to draw the axes and functions
        self.t.hideturtle()
        # make the shape of the turtle object invisible
        self.t.speed("fastest")
        # set the speed of this object to be as fast as possible

        self.draw_axes()
        # call the class method draw_axes to draw the axes

    def draw_axes(self):
        self.t.color("grey")
        # draw the axes in the colour grey which is not used when drawing the functions so they stand out
        turtle.tracer(0, 0)
        # disable turtle drawing updates until after the axes have been drawn

        self.t.penup()
        # move the pen up before moving to its position
        self.t.goto(-self.SCALE * abs(self.X_MIN), 0)
        # send the turtle to the start of the x-axis as defined by scale and x_minimum
        self.t.pendown()
        # place the pen down to begin drawing
        self.t.goto(self.SCALE * abs(self.X_MAX), 0)
        # send the turtle to the other side of the x-axis, drawing the line as it goes
        self.draw_ticks('x', 10)
        # call the draw_ticks method to draw axis ticks on the x-axis with tick_length 10

        self.t.penup()
        # move the pen up before moving to its position
        self.t.goto(0, -self.SCALE * abs(self.Y_MIN))
        # send the turtle to the start of the y-axis as defined by scale and x_minimum
        self.t.pendown()
        # place the pen down to begin drawing
        self.t.goto(0, self.SCALE * abs(self.Y_MAX))
        # send the turtle to the other side of the y-axis, drawing the line as it goes
        self.draw_ticks('y', 10)
        # call the draw_ticks method to draw axis ticks on the y-axis with tick_length 10

        turtle.update()
        # update the screen to process what has been drawn
        turtle.tracer(1, 0)
        # re-enable the turtle tracer so the screen updates as it is drawing

    def draw_ticks(self, axis, tick_length):
        # create method draw_ticks passing as parameters the axis which it is being drawn on, and the width in pixels
        # of the tick
        for i in range(self.X_MIN if axis == 'x' else self.Y_MIN, (self.X_MAX if axis == 'x' else self.Y_MAX) + 1):
            # for each whole number between the minimum and maximum x or y value...
            self.t.penup()
            # lift the pen up
            if axis == 'x':
                # if we are drawing ticks for the x-axis
                self.t.goto(i * self.SCALE, 0)
                # go to the start of the x-axis
                self.t.setheading(90)
                # set the turtle to face perpendicular to the axis
            else:
                # otherwise, we are drawing ticks for the y-axis
                self.t.goto(0, i * self.SCALE)
                # go to the start of the y-axis
                self.t.setheading(0)
                # set the turtle to face perpendicular to the axis
            self.t.backward(tick_length / 2)
            # move backwards half of the tick length
            self.t.pendown()
            # place the pen down
            self.t.forward(tick_length)
            # move forward the entire tick length, drawing the tick now that the pen is down

    def plot_function(self, equation):
        # method to draw the function object stored in the equation parameter
        turtle.tracer(0, 0)
        # disable screen updates until all functions drawn
        self.t.penup()
        # lift the pen up
        first_point = True
        # since we are drawing the first point, set first_point to be true
        func_type, func_str, func_colour = equation.functype, equation.function, equation.colour
        # let func_type, func_str and func_colour be the variables containing the attributes of the equation
        # containing the type, colour and actual expression of the equation
        self.t.color(func_colour)
        # set the colour of the pen to be the colour assigned to the function
        if func_type == "y=":
            # if the function is in terms of y
            func = lambda x: eval(func_str)
            # turn the mathematical function as a python function in terms of a variable x
            for x in np.arange(self.X_MIN, self.X_MAX, 0.01):
                # start a loop that iterates over values of x between x_min and x_max with a step of 0.01
                try:
                    y = func(x)
                    # let y, as in the y coordinate, be the evaluation of the func function with the current x value
                    # from the for loop as its value
                    if self.Y_MIN <= y <= self.Y_MAX:
                        # check if the current y value is between the minimum and maximum y values, to avoid drawing
                        # outside the bounds of the graph
                        if first_point:
                            # if we are drawing our first point
                            self.t.goto(x * self.SCALE, y * self.SCALE)
                            # go to the coordinates of the first point while the pen is still up to avoid drawing any
                            # erroneous connecting lines
                            first_point = False
                            # now that we have moved to the first point, set it to false
                        if not self.t.isdown():
                            self.t.pendown()
                            # place the pen down if not down already, to avoid any redundant calls of the pendown method
                        self.t.goto(x * self.SCALE, y * self.SCALE)
                        # go to the coordinates of the next point
                    else:
                        # if the y value of the point to be drawn lies outside the boundaries defined by the max and
                        # min y values, lift the pen up and simply ignore it
                        self.t.penup()
                        first_point = True
                        # re-enable first_point, so no erroneous lines are drawn between where it exited the bounds
                        # and re-enters, if indeed it does re-enter
                    self.t.penup()
                    # lift the pen back up
                except ValueError:
                    # if a value error occurred somewhere in the above code, simply pass instead
                    pass
        elif func_type == "x=":
            # if the function is in terms of y
            func = lambda y: eval(func_str)
            # turn the mathematical function as a python function in terms of a variable y
            for y in np.arange(self.Y_MIN, self.Y_MAX, 0.01):
                # start a loop that iterates over values of y between y_min and y_max with a step of 0.01
                try:
                    x = func(y)
                    # let x, as in the x coordinate, be the evaluation of the func function with the current y value
                    # from the for loop as its value
                    if self.Y_MIN <= x <= self.Y_MAX:
                        # check if the current x value is between the minimum and maximum x values, to avoid drawing
                        # outside the bounds of the graph
                        if first_point:
                            # if we are drawing our first point
                            self.t.goto(x * self.SCALE, y * self.SCALE)
                            # go to the coordinates of the first point while the pen is still up to avoid drawing any
                            # erroneous connecting lines
                            first_point = False
                            # now that we have moved to the first point, set it to false
                        if not self.t.isdown():
                            self.t.pendown()
                            # place the pen down if not down already, to avoid any redundant calls of the pendown method
                        self.t.goto(x * self.SCALE, y * self.SCALE)
                        # go to the coordinates of the next point
                    else:
                        # if the x value of the point to be drawn lies outside the boundaries defined by the max and
                        # min x values, lift the pen up and simply ignore it
                        self.t.penup()
                        first_point = True
                        # re-enable first_point, so no erroneous lines are drawn between where it exited the bounds
                        # and re-enters, if indeed it does re-enter
                    self.t.penup()
                    # lift the pen back up
                except ValueError:
                    # if a value error occurred somewhere in the above code, simply pass instead
                    pass
        self.screen.update()
        # update the screen

    def plot(self):
        # method to plot all functions
        for equation in self.equations:
            # for every equation object in the self.equations attribute array
            self.plot_function(equation)
            # call the plot_function method on each equation object
        turtle.done()
        # declare the turtle to be done once functions drawn so the user can safely close the window
