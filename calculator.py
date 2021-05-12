# Calculator Project
from art import logo


def add(n1, n2):
    """Performs Addition of two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Performs Subtraction of two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Performs Multiplication of two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Performs Division of two numbers"""
    return n1 / n2


def exponent(n1, n2):
    """Raises a number to the power of another number"""
    return n1 ** n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': exponent,
}


# We are going to use recursion to restart the calculator if the user want to start with different numbers.
def calculator():
    print(logo)

    should_continue = True
    num1 = float(input('What is the first number? '))

    for operation in operations:
        print(operation)

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What is the next number? '))
        # When we try to get the values of any of the keys in the Dict, if it is a function, it return where the
        # function is Stored in memory. print(operations['+'])
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {result}')

        continue_calculation = input(f"Type 'y' to continue calculating with {result} or type 'n' to start again, or "
                                     f"Type 'END' to end the calculator: ")

        if continue_calculation == 'y':
            num1 = result
        elif continue_calculation == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()
