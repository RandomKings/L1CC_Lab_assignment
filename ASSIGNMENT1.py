x = float(input("Enter the first value: "))
calc = input("Enter the logical operator: ")
y = float(input("Enter the second value: "))

if type(x) == float & type(y) == float:
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
else:
    print("enter proper values")
    

