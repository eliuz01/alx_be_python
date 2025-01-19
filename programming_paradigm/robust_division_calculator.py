def safe_divide(numerator, denominator):
    try:
        # Attempt to convert input to floats
        numerator = float(numerator)
        denominator = float(denominator)
        # Handle division by zero
        if denominator == 0:
            return "Error: cannot devide by zero."
        
        # Perform division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # Catch non-numeric inputs
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unexpected exceptions
        return f"An unexpected error occurred: {str(e)}"