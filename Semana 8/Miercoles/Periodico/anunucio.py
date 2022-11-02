class AnuncioComercial:
    def __init__(self,imagen,seccion):
        self.imagen = imagen
        self.seccion = seccion

class AnuncioClasificado:
    def __init__(self,precio, fecha_pub, dias, tipo):
        self.precio = precio
        self.fecha_pubicacion = fecha_pub
        self.cantidad_dias = dias
        self.tipo = tipo 

class AnuncioClasificadoVehiculo(AnuncioClasificado):
    def __init__(self, precio, fecha_pub, dias,marca,modelo,año,color, km):
        super().__init__(precio, fecha_pub, dias, "Vehiculo")
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.km = km

class AnuncioClasificadoVivienda(AnuncioClasificado):
    def __init__(self, precio, fecha_pub, dias,m2, cuartos,baños,puesto,politica):
        super().__init__(precio, fecha_pub, dias, "Vivienda")
        self.m2 = m2
        self.cantidad_cuartos = cuartos
        self.cantidad_baños = baños
        self.cantidad_puestos = puesto
        self.acepta_poltica = politica