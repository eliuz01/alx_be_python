def perform_operation(num1, num2, operation):
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1/num2
    else: 
        print("Invalid operation selected. Please choose from (add, subtract, multiply, divide).")
    return result



result = perform_operation(5, 10, "add")
print("The result is:", result)
