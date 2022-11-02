class Articulo:
    def __init__(self,titulo,resumen,cuerpo,imagenes,fecha_creacion,redactor):
        self.titulo = titulo
        self.resumen = resumen
        self.cuerpo = cuerpo
        self.imagenes = imagenes
        self.fecha_creacion = fecha_creacion
        self.fecha_aprobacion = None
        self.redactor = redactor
        