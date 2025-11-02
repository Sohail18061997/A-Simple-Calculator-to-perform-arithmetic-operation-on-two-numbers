def calculator():
    print("Welcome to the Calculator!")

    # Input the first number
    num1 = float(input("Enter the first number: "))

    # Input the second number
    num2 = float(input("Enter the second number: "))

    # Choose the operation
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4): ")

    # Perform the operation
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid choice.")
        return

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the calculator
calculator()