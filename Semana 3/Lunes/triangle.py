number = input("Please enter a number: ")

if number.isnumeric():
    number = int(number)
    for number_for in range(1,number+1):
        print("*"*number_for)
        
else:
    print("Invalid Input")