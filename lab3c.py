#!/usr/bin/env python3

def operate(number1, number2, operator):
        if operator == "add":
                number3 = number1 + number2
        elif operator == "subtract":
                number3 = number1 - number2
        elif operator == "multiply":
                number3 = number1 * number2
        else:
                return('Error: function operator can be "add", "subtract", or "multiply"')

        if 'number3' in locals():
                return(number3)
