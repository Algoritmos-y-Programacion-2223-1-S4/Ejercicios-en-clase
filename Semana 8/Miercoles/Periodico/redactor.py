import random
from article import Articulo

class Redactor:
    def __init__(self, nombre,ci):
        self.nombre = nombre
        self.cedula = ci
    
    def escribir_articulo(self):
        print("Empece a escribir un articulo")
        articulo = Articulo(
            input("Titulo: "),
            input("Resumen: "),
            input("Cuerpo: "),
            input("Imagenes: "),
            input("Fecha Creacion: "),
            self.nombre
        )
        print("Termine de escribie el articulo",articulo.titulo)
        return articulo

class JefeRedactor(Redactor):
    def __init__(self, nombre, ci, redactores):
        super().__init__(nombre, ci)
        self.grupo_de_redactores = redactores

    def supervisar(self):
        print("Todo esta bien")

    def decidir(self,articulo):
        if random.random() > 0.5:
            print("El articulo",articulo.titulo,"fue aprobado")
            return True
        else:
            print("El articulo",articulo.titulo,"fue aprobado")
            return False
