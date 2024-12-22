num1 = input("Enter the first number: ")

num2 = input("Enter the second number: ")

case_operation  = input("Choose the operation (+, -, *, /): ")

match case_operation: 
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1/num2
            print(f"The result is {result}")
        else:
            print("Error: Cannot divide by zero.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case _:
        print("Invalid operation selected. Please choose from (+, -, *, /).")

