from Vehicle import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad,cc):
        Bicicleta.__init__(color, ruedas, tipo)
        self.velocidad = velocidad 
        self.cc = cc