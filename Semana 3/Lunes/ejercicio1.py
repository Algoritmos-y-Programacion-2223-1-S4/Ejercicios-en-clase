number = input("Please enter a number: ")
aux = 1
if number.isnumeric():
    number = int(number)
    while aux <= number:
        if aux+2 >=number:
            print(aux)
        else:
            print(aux, end=",")
        aux+=2
else:
    print("Invalid Input")