import art

def main():
    print(art.logo)
    
    confirmation = 'n'
    while confirmation == 'n':
        number1= float(input("What's the first number?: "))
        answer = calculator(number1)
        confirmation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        while confirmation != 'n':
            answer2 = calculator(answer)
            confirmation = input(f"Type 'y' to continue calculating with {answer2}, or type 'n' to start a new calculation: ")
            if confirmation == 'y':
                answer = answer2
                
def add(number1,number2):
    return number1 + number2
def subtract(number1,number2):
    return number1 - number2
def multiply(number1,number2):
    return number1 * number2
def divide(number1,number2):
    if number2 == 0 or number1 == 0:
        return "Error: Division by zero"
    return number1 / number2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculation(number1, number2, operation_symbol):
    calculation = operations[operation_symbol]
    answer = calculation(number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {answer}")
    return answer

def calculator(number1):
    for operator in operations:
        print(f"{operator}")
    operation_symbol = input("Pick an operation from the line above: ")
    number2 = float(input("What's the next number?: "))
    answer = calculation(number1, number2,operation_symbol)
    return answer

main()