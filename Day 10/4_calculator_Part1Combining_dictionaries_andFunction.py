
# Calculator

#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def devide(n1,n2):
    return n1 / n2

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":devide
    }


num1 = int(input("What the first number?: "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What the second number?: "))
calculation_function = operation[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

