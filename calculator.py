#Create a simple calculator with the 4 basic operators43

#If an undefined operator is used display invalid operator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operator between [+,-,*,/]")

operator = input("Enter operator: ")
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operator")