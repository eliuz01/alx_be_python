def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    perform_operation  = input("Enter the operation (add, subtract, multiply, divide): ")
    if perform_operation == "add":
        result = num1 + num2
    elif perform_operation == "subtract":
        result = num1 - num2
    elif perform_operation == "multiply":
        result = num1 * num2
    elif perform_operation == "divide":
        if num2 != 0:
            result = num1/num2
        else:
            print("Error: Cannot divide by zero.")
    else: 
        print("Invalid operation selected. Please choose from (add, subtract, multiply, divide).")
    return result

print(perform_operation())