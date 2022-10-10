def main():
    ma = [
        (1, 2, 3),
        (4, 5, 6)
        ]
    mb = [
        (-1, 0),
        (0, 1),
        (1,1)
        ]
    lista=[]
    acum =0
    
    for ia in range(2):
        for j in range(len(ma[ia])):
            acum+=ma[ia][j]*mb[j][ia]
            print(acum)
        acum=0



main()