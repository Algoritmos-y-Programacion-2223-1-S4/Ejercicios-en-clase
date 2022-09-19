float("hahsahshs")

number1 = input("Please enter the first number: ")
number2 = input("Please enter the second number: ")
is_valid = True

if number1.isnumeric():
    number1 = float(number1)
else:
    is_valid = False

if number2.isnumeric():
    number2 = float(number2)
else:
    is_valid = False

if is_valid:
    if number2 == 0: 
        print("Error")
    else:
        print(number1/number2)
else:
    print("Invalid numbers")
