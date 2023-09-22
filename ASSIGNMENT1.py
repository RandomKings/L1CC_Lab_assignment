while True:
    calculator = input("would u like to use math/bmi calculator: ")

    if calculator == "math":
        print("WELCOME TO MATH CALCULATOR")
        x,calc,y = input("Enter your problem(ex: 3 * 3 - use a space): ").split(" ")

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
            else:
                print("Wrong logical operator")
                break
        except ValueError:
            print("enter a numeric value")  
    elif calculator == "bmi":
        print("WELCOME TO BMI CALCULATOR")
        weight,height = input("Enter your weight(kg) and height(m) seperated by a space: ").split(" ")

        try:
            weight = float(weight)
            height = float(height)
            
            print(f"{weight}/({height} * {height}) = ",weight/ height**2)

        except ValueError: 
             print()                                               
