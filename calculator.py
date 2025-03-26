# Simple Calculator App
# with error handling

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def get_choice(answer):
    while True:
            try:
                choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'e' to exit: ").lower()
                if choice not in ['y', 'n', 'e']:
                    raise ValueError("Invalid response! Please enter 'y', 'n', or 'e'.")
                break
            except ValueError as e:
                print(f'Error: {e}')
    return choice

def get_operator():
    while True:
            try:
                operator = input("Pick an operation: ")
                if operator not in {"+", "-", "*", "/"}:
                    raise ValueError("Invalid operator! Please enter +, -, *, or /.")
                break
            except ValueError as e:
                print(f"Error: {e}")
    return operator

def check_if_zero_for_denominator():
    while True:
        try:
            num2 = float(input("What is the next number?: "))
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero! Please enter a different denominator.")
            break
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    return num2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

art = """
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
"""
print(art)
print("Welcome to this simple calculator app!")
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operator = get_operator() # gets the operator from user

        num2 = check_if_zero_for_denominator() # catches if user input is 0 for num2
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        choice = get_choice(answer) # gets a choice from user

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            should_accumulate = False
            print("\n"*10)
            print(art)
            calculator() # recursion
        else:
            print("Goodbye!")
            break
            
calculator()