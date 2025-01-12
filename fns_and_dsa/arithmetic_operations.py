def perform_operation(num1, num2, operation):
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1/num2
        else:
            print("Error: Cannot divide by zero.")
    else: 
        print("Invalid operation selected. Please choose from (add, subtract, multiply, divide).")
    return result


num1 = 10
num2 = 5
operation = "add"
result = perform_operation(num1, num2, operation)
print("The result is:", result)
