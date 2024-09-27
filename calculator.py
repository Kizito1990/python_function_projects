#calculator

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

num1 = float(input("What is the first number : \n"))

for symbol in operations:
    print(symbol)


operation_symbol = input("Pick an operation from the line above: ")

num2 = float(input("What is the second number : \n"))

calculation_function = operations[operation_symbol]
result = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")
