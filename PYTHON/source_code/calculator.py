def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        
        elif op == "/":
            return a / b
        
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers")