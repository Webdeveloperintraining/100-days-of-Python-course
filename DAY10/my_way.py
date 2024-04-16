import art

def sum(number1,number2):
    return number1 + number2
def subtract(number1,number2):
    return number1 - number2
def multiplication(number1,number2):
    return number1 * number2
def division(number1,number2):
    if number2 == 0 or number1 == 0:
        return print("Error: Division by zero")
    return number1 / number2

def calc(number1, number2, operation):
    if operation == "+":
        result = sum(number1,number2)
        print(f"{number1} + {number2} = {result}")
    elif operation == "-":
        result = subtract(number1,number2)
        print(f"{number1} - {number2} = {result}")
    elif operation == "*":
        result = multiplication(number1,number2)
        print(f"{number1} * {number2} = {result}")
    elif operation == "/":
        result = division(number1,number2)
        print(f"{number1} / {number2} = {result}")
        
    number3 = result
    return number3 

def main():
    print(art.logo)
    confirmation = 'n'

    while confirmation == 'n':
        number1= float(input("What's the first number?: "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation : ")
        if operation not in ["+","-","*","/"]:
            print("Please enter a valid operation.")
            continue
        number2 = float(input("What's the next number?: "))
        number3 = calc(number1, number2,operation)

        confirmation = input(f"Type 'y' to continue calculating with {number3}, or type 'n' to start a new calculation: ")
        while confirmation != 'n':
            print("+\n-\n*\n/")
            operation = input("Pick an operation from above: ")
            number2 = float(input("What's the next number?: "))
            number3 = calc(number3, number2,operation)
            confirmation = input(f"Type 'y' to continue calculating with {number3}, or type 'n' to start a new calculation: ")

main()