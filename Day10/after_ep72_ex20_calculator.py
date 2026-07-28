import art
def add(n1, n2):
    sum = n1 + n2
    return sum

def subctract(n1, n2):
    if(n1 < n2):
        return "Please keep number1 greater than number2."
    else:
        sub = n1 - n2
        return sub

def multiply(n1, n2):
    mul = n1 * n2
    return mul

def division(n1, n2):
    if n2 == 0:
        return "Please keep number2 greater than 0."
    else:
        div = n1 / n2
        return div

operations = {
    "+": add,
    "-": subctract,
    "*": multiply,
    "/": division,
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
