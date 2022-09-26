number = input("Please enter a number: ")

if number.isnumeric():
    number = int(number)
    for number_for in range(1,number+1,2):
        if number_for >= number-1:
            print(number_for)
        else:
            print(number_for, end=",")
    
else:
    print("Invalid Input")