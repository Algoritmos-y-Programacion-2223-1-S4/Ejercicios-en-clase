number = input("Please enter one number: ")
if number.isnumeric():
    if number%2==0:
        print(f"The number {number} is even")
    else:
        print("The number {} is odd".format(number))
else:
    print("Invalid nmber")