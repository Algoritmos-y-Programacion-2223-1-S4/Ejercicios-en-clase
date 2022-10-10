number = int(input("Please enter a number"))
isPronic = False
aux= 1

while aux < number:
    if aux*(aux+1)==number:
        isPronic = True
        break
    aux+=1

if isPronic:
    print("The number is pronic")
else:
    print("The number is not pronic")