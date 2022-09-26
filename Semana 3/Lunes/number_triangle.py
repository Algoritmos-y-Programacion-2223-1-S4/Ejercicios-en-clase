number = input("Please enter a number: ")
aux2=1

if number.isnumeric():
    number = int(number)
    while aux2 < number:
        aux = aux2
        while aux >= 1:
            if aux == 1:
                print(aux)
            else:
                print(aux, end=" ")
            aux-=2
        aux2+=2
else:
    print("Invalid Input")