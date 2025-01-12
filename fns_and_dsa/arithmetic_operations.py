def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation  = input("Enter the operation (add, subtract, multiply, divide): ")
    if operation == "add":
        result = num1 + num2
    elif operation == "substract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif result == "division":
        if num2 != 0:
            result = num1/num2
        else:
            print("Error: Cannot divide by zero.")
    else: 
        print("Invalid operation selected. Please choose from (add, subtract, multiply, divide).")
    return result

print(perform_operation())