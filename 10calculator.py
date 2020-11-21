from art import calculator_logo
from os import system

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    system('clear')
    print(calculator_logo)
    # First calculation
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    input_operator = input("Pick an operation from the list above: ")
    num2 = float(input("What's the second number?: "))

    result = operations[input_operator](num1, num2)

    print(f"{num1} {input_operator} {num2} = {result}")
    
    # Second calculation (repeatible)
    keep_going = True
    while keep_going:
        another = input(f"Type 'yes' to continue calculating with {result}, 'new' to start with new numbers, or 'exit' to leave the application: ").lower()

        if another == 'yes':
            num1 = result
            system('clear')
            print(calculator_logo)
            for operator in operations:
                print(operator)
            input_operator = input("Pick another operation from the list above: ")
            num2 = float(input("What's the next number?: "))

            result = operations[input_operator](num1, num2)
            print(f"{num1} {input_operator} {num2} = {result}")

        elif another == 'new':
            calculator()

        elif another == 'exit':
            keep_going = False

calculator()