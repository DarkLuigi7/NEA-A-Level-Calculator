class CreateButton:

    def __init__(self, name, text, x, y, padx, pady, fontsize, command, commandparameters, bg):
        self.name = name
        self.text = text
        self.x = x
        self.y = y
        self.padx = padx
        self.pady = pady
        self.fontsize = fontsize
        self.command = command
        self.commandparameters = commandparameters
        self.bg = bg
        button = Button(basicCalculatorWindow, text=self.text, width=self.x, bg=self.bg,
                        command=lambda: self.command(self.commandparameters), relief=RAISED)
        button.grid(row=self.x, column=self.y, padx=self.padx, pady=self.pady)
        button.config(font=("Courier New", self.fontsize))
