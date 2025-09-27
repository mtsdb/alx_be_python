def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations between two numbers.

    Parameters:
        num1: The first number.
        num2: The second number.
        operation: The operation to perform. 
                   Options: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the operation, or an error message if invalid.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
