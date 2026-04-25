
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def clear_screen():
    print("\n" * 50)
    print("Calculator cleared!\n")


def get_number(prompt):
    """Validate numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number! Please enter a valid numeric value.")


def perform_calculation():
    num1 = get_number("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ").strip()
    num2 = get_number("Enter second number: ")

    try:
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operator!")
            return

        print(f"\nResult: {num1} {operator} {num2} = {result}\n")

    except ZeroDivisionError as e:
        print(e)



def show_menu():
    print("====== Command Line Calculator ======")
    print("1. Perform Calculation")
    print("2. Clear Screen")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            perform_calculation()

        elif choice == "2":
            clear_screen()

        elif choice == "3":
            print("Exiting Calculator... Goodbye!")
            break

        else:
            print("Invalid menu choice!\n")


if __name__ == "__main__":
    main()