while True:
    operation = input("Enter operation (+, -, *, /): ")
    if operation == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2 
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation."
    print("result",result) 
       
    