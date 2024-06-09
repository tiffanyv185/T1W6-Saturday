# a simple calculator using if-else statements

# get user inputs

num1 = float(input("enter first number: "))
operation = input ("enter operatoion (+ - * /): ")
num2 = float(input("enter second number: "))

# perform calculation using if-else statements 

if operation == "+" :
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "invalid operation"

print(f"the result is: {result}")
