number = int(input("Please enter a number: "))
aux = number-1
cont = 0
if number <= 1:
    print(f"The number {number} is not prime")
else:
    while aux > 1:
        print("aux",aux)
        print("operation",number%aux)
        if number%aux == 0:
            print("IN if operation")
            cont +=1
            break
        aux-=1

    if cont == 0:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")
        
