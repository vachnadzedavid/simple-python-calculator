print("Choose an operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

option = int(input("Choose an operation: "))  # Get the user's choice

# Check if the chosen option is valid (1 to 4)
if option in [1, 2, 3, 4]:
    # Ask for two numbers to perform the operation
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform the correct operation based on the user's choice
    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        # Check for division by zero to avoid an error
        if num2 != 0:
            result = num1 // num2
        else:
            print("Error: Division by zero is not allowed.")
            result = None

    # If result is valid (not None), print it
    if result is not None:
        print("The result of the operation is {}".format(result))

else:
    print("Invalid operation entered")
