x,calc,y = input("Enter your problem(ex: 3 * 3 - use a space) : ").split(" ")

try:
    x = float(x)
    y = float(y)


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
