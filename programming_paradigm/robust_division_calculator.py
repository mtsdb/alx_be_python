def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and non-numeric inputs.
    Returns an appropriate message depending on the outcome.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
