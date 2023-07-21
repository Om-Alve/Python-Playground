# Taking input from user
num1 = int(input("Enter first number: "))
operation = input("Enter operation symbol: ")
num2 = int(input("Enter second number: "))
# For Addition
if operation == '+':
    add = num1+num2
    print(add)
# For Subtraction
elif operation == '-':
    subtract = num1-num2
    print(subtract)
# For Multipllication
elif operation == '*':
    multiplication = num1*num2
    print(multiplication)
# For Division
elif operation == '/':
    division = num1/num2
    print(division)
else:
    print("Invalid Operator")
