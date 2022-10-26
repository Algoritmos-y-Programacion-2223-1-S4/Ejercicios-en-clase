from Vehicle import Vehicle


def main():
    vehicle = Vehicle("Toyota","Yaris","Green",2022)
    vehicle.set_brand("FORD")
    print(vehicle.get_brand())
    

main()