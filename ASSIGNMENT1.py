while True:
    x,calc,y = input("Enter your problem(ex: 3 * 3 - use a space)(for bmi : 52.6 b 1.72) height must be in meters: ").split(" ")

    try:
        x = float(x)
        y = float(y)


        
        if calc == "+":
            print(f"{x} + {y} = ",x+y )
        elif calc == "-":
            print(f"{x} - {y} = ",x - y)
        elif calc == "*":
            print(f"{x} * {y} = ",x * y)
        elif calc == "/":
            if y != 0:
                print(f"{x} / {y} = ",x / y)
            else:
                print("Division by zero is not allowed.")
        elif calc == "**":
            print(f"{x} ** {y} = ",x ** y)
        elif calc == "bmi":
            print(f"{x}/({y} * {y}) = ",x/ y**2)
        else:
            print("Wrong logical operator")


    except ValueError:
        print("enter a numeric value")                                                                                       
        
