#calculator
from art2 import logo
#Add function
def add(n1, n2):
    return n1 + n2

#Substract Function
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "_":subtract,
    "*":multiply,
    "/":divide

             }
def calculator():
    print(logo)
    num1 = float(input("What is the first number : \n"))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number : \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'yes' to continue calculating with {answer} or Type 'no' to exit: ") == "yes":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()