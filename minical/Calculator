# Function to perform addition
def addition(a, b):
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result

# Function to perform subtraction
def subtraction(a, b):
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result

# Function to perform multiplication
def multiplication(a, b):
    result = a * b
    history.append(f"{a} * {b} = {result}")
    return result

# Function to perform division
def division(a, b):
    if b == 0:
        result = "Division by zero is not allowed."
    else:
        result = a / b
    history.append(f"{a} / {b} = {result}")
    return result

# Main calculator loop
history = []  # Initialize an empty history list

while True:
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show History")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '6':
        break

    if choice == '5':
        if not history:
            print("History is empty.")
        else:
            print("Calculation History:")
            for item in history:
                print(item)
    elif choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {addition(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == '4':
            result = division(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4/5/6).")

print("Goodbye!")
