import tkinter as tk
from tkinter import font

class PocketCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Pocket Calculator")
        self.root.resizable(False, False)

        self.fixed_font = font.Font(family="Courier", size=20)

        self.display_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.display_var, font=self.fixed_font,
                                justify='right', bd=10, relief='sunken', width=10, state='readonly')
        self.display.grid(row=0, column=0, columnspan=4)

        self.current = ""
        self.operator = ""
        self.operand = None

        buttons = [
            ('7', self.append_char), ('8', self.append_char), ('9', self.append_char), ('/', self.set_operator),
            ('4', self.append_char), ('5', self.append_char), ('6', self.append_char), ('*', self.set_operator),
            ('1', self.append_char), ('2', self.append_char), ('3', self.append_char), ('-', self.set_operator),
            ('0', self.append_char), ('.', self.append_char), ('+/-', self.change_sign), ('+', self.set_operator),
            ('C', self.clear), ('=', self.calculate)
        ]

        for idx, (text, cmd) in enumerate(buttons):
            row = 1 + idx // 4
            col = idx % 4
            b = tk.Button(root, text=text, width=5, height=2, font=self.fixed_font,
                          command=lambda t=text, c=cmd: c(t))
            b.grid(row=row, column=col)

    def update_display(self, value):
        if isinstance(value, float):
            if value.is_integer():
                value = int(value)
            else:
                value = round(value, 10)
        value_str = str(value)
        if len(value_str) > 10:
            self.display_var.set("Error")
        else:
            self.display_var.set(value_str)

    def append_char(self, char):
        if len(self.current) >= 10:
            return
        if char == '.' and '.' in self.current:
            return
        self.current += char
        self.update_display(self.current)

    def set_operator(self, op):
        if self.current:
            self.operand = float(self.current)
            self.operator = op
            self.current = ""

    def change_sign(self, _):
        if self.current:
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.update_display(self.current)

    def clear(self, _):
        self.current = ""
        self.operator = ""
        self.operand = None
        self.update_display("")

    def calculate(self, _):
        try:
            if self.operator and self.current:
                second_operand = float(self.current)
                if self.operator == '+':
                    result = self.operand + second_operand
                elif self.operator == '-':
                    result = self.operand - second_operand
                elif self.operator == '*':
                    result = self.operand * second_operand
                elif self.operator == '/':
                    if second_operand == 0:
                        self.update_display("Error")
                        return
                    result = self.operand / second_operand
                else:
                    result = second_operand
                self.current = str(result)
                self.update_display(result)
                self.operator = ""
                self.operand = None
        except Exception:
            self.update_display("Error")

# Run the calculator
root = tk.Tk()
app = PocketCalculator(root)
root.mainloop()