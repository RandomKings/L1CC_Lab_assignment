x = input("Enter the first value: ")
calc = input("Enter the logical operator: ")
y = input("Enter the second value: ")

try:
    x=float(x)
    y = float(y)

    if type(x,y) == float:
        if calc == "+":
            print(x + y)
        elif calc == "-":
            print(x - y)
        elif calc == "*":
            print(x * y)
        elif calc == "/":
            if y != 0:
                print(x / y)
            else:
                print("Division by zero is not allowed.")
        elif calc == "**":
            print(x ** y)
        else:
            print("Wrong logical operator")

except ValueError:
    print("enter a numeric value")

