from Vehicle import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad,cc):
        Vehiculo.__init__(color, ruedas)
        self.velocidad = velocidad 
        self.cc = cc

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cc, carga):
        super().__init__(color, ruedas, velocidad, cc)
        self.carga = carga
