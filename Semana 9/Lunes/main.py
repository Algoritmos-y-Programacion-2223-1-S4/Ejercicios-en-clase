def main():
    archivo = open('archivo.txt','r')
    datos = archivo.read()
    archivo.close()
    print(datos)

main()